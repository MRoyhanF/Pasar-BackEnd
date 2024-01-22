from app import app
from app.controller import UserController
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

@app.route('/user/<id>', methods= ['GET'])
def userDetail(id):
    return UserController.detail(id)

#@app.route('login'. methods=['POST'])
#def logins():
#    return UserController.