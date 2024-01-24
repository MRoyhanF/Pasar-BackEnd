from app.model.user import User
from app.model.product import Product
from app.model.transaction import Transaction

from flask import render_template, jsonify
from flask_jwt_extended import get_jwt_identity

from app import response, app, db
from flask import request

# get all transaction
def index():
    try:
        transaction = Transaction.query.all()
        data = formatArray(transaction)
        return response.success(data, "success")
    except Exception as e:
        print(e)

# buat array kosong untuk menampung data
def formatArray(datas):
    array = []
    for i in datas:
        array.append(singleObject(i))

    return array

def singleObject(data):
    data = {
        'id' : data.id,
        'id_user' : data.id_user,
        'id_product' : data.id_product,
        'quantity' : data.qty,
        'amount' : data.Amount,
    }

    return data