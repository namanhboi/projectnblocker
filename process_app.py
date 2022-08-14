from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)
db_locale = 'processes.db'


@app.route('/')
@app.route('/home')
def home_page():
    process_data = query_contact_details()
    return render_template("index.html", process_data = process_data)

def query_contact_details():
    connection = sqlite3.connect(db_locale)
    cursor = connection.cursor()
    cursor.execute("""
    select * from all_processes where status = 'unblocked'
    """)
    process_data = cursor.fetchall()
    return process_data

if __name__ == '__main__':

    app.run(debug = True)