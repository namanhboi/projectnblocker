from flask import Flask, render_template, request
from multiprocessing import connection
import sqlite3

app = Flask(__name__)
db_locale = 'nblocker.db'
@app.route('/')
@app.route('/domain_rules/')

def domain_rules_page():
    domain_data= query_domain_data()
    return render_template("domain_rules.html", domain_data = domain_data)

def query_domain_data():
    connection = sqlite3.connect(db_locale)
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM domain_rules
    """)
    domain_data = cursor.fetchall()
    connection.close()
    return domain_data

if __name__ == '__main__':
    app.run(debug = True)