from flask import Flask, request, Response,jsonify
from flask import jsonify
from flaskext.mysql import MySQL
from db_connection import db_cursor, get_students, add_student
import json 
app = Flask(__name__)


@app.route('/students', methods = ['GET'])
def students():
    data = get_students()
    print(data)
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/students/add', methods = ['POST'])
def add():
    args = request.get_json()
    result = add_student(args['name'],args['mark'])
    response = app.response_class(
        response=json.dumps(result),
        status=200,
        mimetype='application/json'
    )
    
    return response
	

