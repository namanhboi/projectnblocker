import psutil
import sqlite3
    
def run():    
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
if __name__ == '__main__':
    
    run()