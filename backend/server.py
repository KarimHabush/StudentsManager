from flask import Flask, request, Response,jsonify
from flask import jsonify
from flaskext.mysql import MySQL
from db_connection import db_cursor

app = Flask(__name__)


@app.route('/students')
def students():
    

    db_cursor.execute("SELECT * from students")
    data = db_cursor.fetchall()

    return jsonify({
        'status':'success',
        'result':data
    })


@app.route('/students/add')
def add_student():

    db_cursor.execute("SELECT * from students")
    data = db_cursor.fetchall()

    return jsonify({
        'status':'success',
        'result':data
    })
	

