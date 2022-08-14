import psutil
import sqlite3

from contextlib import closing
listOfProcessNames = list()



for proc in psutil.process_iter():
    
    pInfoDict = proc.as_dict(attrs = ['name', 'pid', 'exe'])
    listOfProcessNames.append(pInfoDict)

print(listOfProcessNames)
print()
print()

db_locale = 'processes.db'

connection = sqlite3.connect(db_locale)
cursor = connection.cursor()
cursor.execute("create table if not exists all_processes (pid integer primary key, name text not null, absolute_path text ,status text not null);")


connection.commit()
cursor.execute("delete from all_processes;")
connection.commit()

for proc in listOfProcessNames:
    proc_name = proc['name']
    proc_pid =  proc['pid']
    proc_status = 'unblocked'
    proc_path = proc['exe']
    cursor.execute("insert into all_processes(pid, name, absolute_path, status) values(?, ?, ?, 'unblocked');", (proc_pid, proc_name, proc_path))



connection.commit()
connection.close()      