from flask import Flask, render_template
import random
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'LiadY',
    'password': '!2804Berber13579',
    'database': 'first_db'
}

connection = mysql.connector.connect(**db_config)


@app.route('/')
def index():
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM strings_table ORDER BY RAND() LIMIT 9')
    results = cursor.fetchall()
    cursor.close()
    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
