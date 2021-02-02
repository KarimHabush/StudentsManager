from flask import Flask, request, Response,jsonify
from flask import jsonify
from flaskext.mysql import MySQL
from db_connection import db_cursor
import json 
app = Flask(__name__)


@app.route('/students', methods = ['GET'])
def students():
    db_cursor.execute("SELECT * from students")
    data = db_cursor.fetchall()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response
@app.route('/students/show_data')
def note():
   db_cursor.execute('SELECT * FROM students')
   data = db_cursor.fetchall()
   response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
   return response

@app.route('/students/add', methods = ['POST'])
def add_student():
    args = request.get_json()
    response = app.response_class(
        response=json.dumps(args),
        status=200,
        mimetype='application/json'
    )
    
    return response
	

