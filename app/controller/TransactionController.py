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

# add transaction
def save():
    try:
        current_user = get_jwt_identity()
        # print("Current User:", current_user)
        
        if not isinstance(current_user, dict):
            return response.badRequest([], 'Invalid user identity in JWT')

            # Pastikan atribut 'name' tersedia di dalam objek current_user
        if 'id' not in current_user:
            return response.badRequest([], 'Field "id" not found in current_user')

        id_user = current_user['id']
        # print("id user :", id_user)

        id_product = request.form.get('id_product')
        quantity = request.form.get('quantity')
        amount = request.form.get('amount')

        input = [
            {
                'id_user' : id_user,
                'id_product' : id_product,
                'quantity' : quantity,
                'amount' : amount
            }
        ]

        transaction = Transaction(id_user=id_user, id_product=id_product, qty=quantity, Amount=amount)

        db.session.add(transaction)
        db.session.commit()

        return response.success(input, 'Create Transaction Successfully..')

    except Exception as e:
        print(e)


