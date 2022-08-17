from flask import Flask, render_template, request
import sqlite3
import psutil

app = Flask(__name__)
db_locale = 'processes.db'


@app.route('/')
@app.route('/processes/')
def processes_page():
    process_data = query_display_running_process()
    return render_template("processes.html", process_data = process_data)

def update_running_process():
    listOfProcessNames = list()

    for proc in psutil.process_iter():
        
        pInfoDict = proc.as_dict(attrs = ['name', 'pid', 'exe'])
        listOfProcessNames.append(pInfoDict)

    db_locale = 'processes.db'

    connection = sqlite3.connect(db_locale)
    cursor = connection.cursor()
    cursor.execute("drop table all_processes;")
    cursor.execute("create table if not exists all_processes (pid integer primary key, name text not null, absolute_path text);")


    connection.commit()
    cursor.execute("delete from all_processes;")
    connection.commit()

    for proc in listOfProcessNames:
        proc_name = proc['name']
        proc_pid =  proc['pid']
        proc_path = proc['exe']
        cursor.execute("insert into all_processes(pid, name, absolute_path) values(?, ?, ?);", (proc_pid, proc_name, proc_path))
        

    connection.commit()
    connection.close()  

def query_display_running_process():    
    update_running_process()

    connection = sqlite3.connect(db_locale)
    cursor = connection.cursor()
    cursor.execute("""
    select * from all_processes;
    """)
    process_data = cursor.fetchall()
    connection.close()
    return process_data




@app.route('/processrules/')
def processrules_page():

    processrules_data = query_display_process_rules()
    return render_template("processRules.html", processrules_data = processrules_data)


def query_display_process_rules():
    connection = sqlite3.connect(db_locale)
    cursor = connection.cursor()
    cursor.execute("""
        select * from process_rules;
    """)
    processrules_data = cursor.fetchall()
    connection.close()
    return processrules_data



@app.route('/processrules/addprocess', methods = ['GET', 'POST'])
def add_process():
    if request.method == 'GET':
        return render_template('addprocess.html')
    else:
        exe_to_block_details = (
            request.form['exeRuleInput'],
            request.form['exeInput']
        )
        add_to_process_rules(exe_to_block_details[0], exe_to_block_details[1])
        return render_template("addprocess.html")


def add_to_process_rules(rule_name, process_name):
    connection = sqlite3.connect(db_locale)
    cursor = connection.cursor()
    cursor.execute("""
    insert into process_rules (rule_name, exe_name)
    values(?, ?)
    """, (rule_name, process_name))

    connection.commit()
    connection.close()

if __name__ == '__main__':
    app.run()