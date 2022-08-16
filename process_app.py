from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
db_locale = 'processes.db'


@app.route('/')
@app.route('/processes/')
def processes_page():
    process_data = query_display_unblocked_process()
    return render_template("processes.html", process_data = process_data)

def query_display_unblocked_process():
    connection = sqlite3.connect(db_locale)
    cursor = connection.cursor()
    cursor.execute("""
    select * from all_processes where status = 'unblocked'
    """)
    process_data = cursor.fetchall()
    connection.close()
    return process_data




@app.route('/processrules/')
def processrules_page():
    processrules_data = query_display_blocked_process()
    return render_template("processRules.html", processrules_data = processrules_data)


def query_display_blocked_process():
    connection = sqlite3.connect(db_locale)
    cursor = connection.cursor()
    cursor.execute("""
        select * from blocked_processes;
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
            request.form['exeInput']
        )
        return 'dddddd'

def block_a_process(process_name):
    connection = sqlite3.connect(db_locale)
    cursor = connection.cursor()
    cursor.execute("""
    update all_processes
    set status = 'blocked'
    where name = ?;
    """,(process_name))
    connection.commit()
    connection.close()

if __name__ == '__main__':
    app.run(debug = True)