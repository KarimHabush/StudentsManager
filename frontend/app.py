from flask import Flask, render_template, request,redirect
import requests
import json

app = Flask(__name__, template_folder='.')
@app.route('/')
def homepage():
    r = requests.get(
        'http://localhost:5000/students')
    return render_template('./templates/index.html',students=r.json()['result'])

@app.route('/delete',methods=['POST'])
def delete():
    data = {
        "id": request.form['id']
    } 
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    requests.post('http://localhost:5000/students/delete', json=data, headers=headers)
    return redirect("/")

@app.route('/update',methods=['POST'])
def update():
    data = {
        "id": request.form['id'],
        "name": request.form['name'],
        "mark": request.form['mark'],
    } 
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    requests.post('http://localhost:5000/students/update', json=data, headers=headers)
    return redirect("/")

@app.route('/add',methods=['POST'])
def add():
    data = {
        "name": request.form['name'],
        "mark": request.form['mark'],
    } 
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    requests.post('http://localhost:5000/students/add', json=data, headers=headers)
    return redirect("/")


if __name__ == '__main__':
  app.run(host='localhost', port=3000)
