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


@app.route('/students/add', methods = ['POST'])
def add_student():
<<<<<<< HEAD
    args = request.get_json()


    
=======
    request_data = request.get_json()
    nom_etudiant = request_data['nom_etudiant']
    note = request_data['note']
    print(nom_etudiant)
    print(note)
>>>>>>> d220e905ca1aa5cdfdadb3311301ef4e00f6ab8f
    response = app.response_class(
        response=json.dumps(nom_etudiant,note),
        status=200,
        mimetype='application/json'
    )
    
    return response
	

