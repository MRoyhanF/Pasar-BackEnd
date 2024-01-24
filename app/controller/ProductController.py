from app.model.user import User
from app.model.product import Product

from flask import render_template, jsonify

from app import response, app, db
from flask import request

## get all product
def index():
    try:
        product = Product.query.all()
        data = formatArray(product)
        return response.success(data, "Success Get All Product")
    except Exception as e:
        print(e)
        # return response.badRequest("terjadi kesalahan", 500)

# buat array kosong untuk menampung data
def formatArray(datas):
    array = []
    for i in datas:
        array.append(singleObject(i))

    return array


def singleObject(data):
    own = User.query.filter(User.id == data.id_user).first()
    owner = own.name if own else None
    data = {
        'id' : data.id,
        'type' : data.type,
        'name' : data.name,
        'description' : data.description,
        'set' : data.set,
        'quantity' : data.qty,
        'price' : data.price,
        'owner' : owner,
    }

    return data