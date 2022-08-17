
import sqlite3

def run():
    db_locale = 'processes.db'

    connection = sqlite3.connect(db_locale)
    cursor = connection.cursor()

    cursor.execute("create table if not exists process_rules(rule_name text, exe_name text not null)")


    connection.commit()
    connection.close()

if __name__ == '__main__':
    run()