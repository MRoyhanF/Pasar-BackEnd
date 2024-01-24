from app import app, response
from app.controller import UserController
from app.controller import AuthController
from app.controller import ProductController
from flask import request, render_template
from flask_jwt_extended import get_jwt_identity, jwt_required

@app.route ('/')
def index():
    return 'Hello Flask App testing'


# USER ROUTES

@app.route("/user/detail", methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return response.success(current_user, 'Success')


@app.route('/user', methods= ['GET', 'POST'])
def users():
    if request.method == 'GET':
        return UserController.index()
    else:
        return UserController.save()


@app.route('/user/<id>', methods= ['GET', 'PUT', 'DELETE'])
@jwt_required()
def userDetail(id):
    if request.method == 'GET':
        return UserController.detail(id)
    elif request.method == 'PUT':
        return UserController.edit(id)
    else:
        return UserController.delete(id)
        

# AUTH ROUTE

@app.route('/login', methods=['POST'])
def logins():
   return AuthController.login()


# PRODUCT ROUTE

@app.route('/product', methods=['GET', 'POST'])
def products():
    if request.method == 'GET':
        return ProductController.index()
    else :
        current_user = get_jwt_identity()
        print(current_user)
    

@app.route('/product/<id>', methods=['GET'])
@jwt_required()
def productDetail(id):
    if request.method == 'GET':
        return ProductController.detail(id)
    else :
        print('testing')