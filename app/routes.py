from app import app
from app.controller import UserController
from app.controller import AuthController
from flask import request, render_template

@app.route ('/')
def index():
    return 'Hello Flask App testing'

@app.route('/user', methods= ['GET', 'POST'])
def users():
    if request.method == 'GET':
        return UserController.index()
    else:
        return UserController.save()

@app.route('/user/<id>', methods= ['GET', 'PUT', 'DELETE'])
def userDetail(id):
    if request.method == 'GET':
        return UserController.detail(id)
    elif request.method == 'PUT':
        return UserController.edit(id)
    else:
        return UserController.delete(id)
        

@app.route('/login', methods=['POST'])
def logins():
   return AuthController.login()