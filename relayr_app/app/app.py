from flask import Flask, render_template
import os
from flask import Flask,render_template, request
from flask_mysqldb import MySQL
import MySQLdb
from flask import jsonify
app = Flask(__name__)
app.config['DEBUG'] = True

app.config['MYSQL_HOST'] = os.environ.get("RELAYR_MYSQL_SERVICE_HOST")
app.config['MYSQL_USER'] = os.environ.get("MYSQLDB_USER")
app.config['MYSQL_PASSWORD'] = os.environ.get("MYSQLDB_PASSWORD")
app.config['MYSQL_DB'] = os.environ.get("MYSQLDB_DATABASE")
mysql = MySQL(app)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/create_table')
def form1():
    return render_template('create_table.html')
@app.route('/create', methods = ['POST'])
def create_table():     
    if request.method == 'POST':
        cursor = mysql.connection.cursor()
        cursor.execute(" CREATE TABLE hello ( City varchar(255))")
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"


@app.route('/login')
def form():
    return render_template('login.html')

@app.route('/input', methods = ['POST'])
def login():     
    if request.method == 'POST':
        string = request.form['string']
        cursor = mysql.connection.cursor()
        cursor.execute(" INSERT INTO hello values (%s)", [string] )
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"


    

@app.route("/temp",methods = ['GET'])
def temp():
    cursor = mysql.connection.cursor()
    sql_select_Query = (" SELECT * from hello ")
    cursor.execute(sql_select_Query)
    return jsonify(data = cursor.fetchall())

if __name__ == "__main__":
    app.run(host="0.0.0.0")