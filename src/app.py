from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():

    connection = mysql.connector.connect(
        host="db",
        user="root",
        password="root",
        database="testdb"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT 'Hola Mundo desde MySQL'")
    result = cursor.fetchone()

    connection.close()

    return result[0]

app.run(host='0.0.0.0', port=5000)