from multiprocessing import connection
import sqlite3

db_locale = 'nblocker.db'

connection= sqlite3.connect(db_locale)
cursor=connection.cursor()


cursor.execute("""
SELECT * FROM domain_rules
""")

domain_data = cursor.fetchall()

print(domain_data)
connection.commit()
connection.close()