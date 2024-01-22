from app import app
from app.controller import UserController

@app.route ('/')
def index():
    return 'Hello Flask App testing'

@app.route('/user', methods= ['GET'])
def users():
    return UserController.index()