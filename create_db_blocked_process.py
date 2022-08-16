
import sqlite3

db_locale = 'processes.db'

connection = sqlite3.connect(db_locale)
cursor = connection.cursor()

cursor.execute("drop table blocked_processes;")
cursor.execute("create table if not exists blocked_processes (rule_name text, exe_name text not null)")

connection.commit()

connection.execute("""
insert into blocked_processes (exe_name)
select name from all_processes
where status = 'blocked';
""")

connection.commit()
connection.close()
