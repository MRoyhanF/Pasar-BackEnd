from app import app, response
from app.controller import UserController
from app.controller import AuthController
from app.controller import ProductController
from app.controller import TransactionController
from flask import request, render_template
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.model.user import User

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
@jwt_required()
def products():
    if request.method == 'GET':
        return ProductController.index()
    else :
        return ProductController.save()
    

@app.route('/product/<id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def productDetail(id):
    if request.method == 'GET':
        return ProductController.detail(id)
    elif request.method == 'PUT':
        return ProductController.edit(id)
    else :
        return ProductController.delete(id)


# TRANSACTION ROUTE
@app.route('/transaction', methods=['GET', 'POST'])
@jwt_required()
def transaction():
    if request.method == 'GET':
        return TransactionController.index()
    else :
        return TransactionController.save()


@app.route('/transaction/<id>', methods=['GET', 'PUT', 'DELETE'])
# @jwt_required()
def transactionDetail(id):
    return TransactionController.detail(id)