from app.model.user import User
from app.model.product import Product

from app import response, app, db
from flask import request

## function mengambil data dosen
def index():
    try:
        user = User.query.all()
        data = formatArray(user)
        #res = response.success(data, "success")
        #return data, res
        return response.success(data, "success")
        #return render_tamplate("dosen.html", )
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
        'name' : data.name,
        'role' : data.role,
        'email' : data.email,
        'phone' : data.phone,
        'address' : data.address
    }

    return data

#function mengambil data user by ID
def detail(id):
    try:
        user = User.query.filter_by(id=id).first()
        product = Product.query.filter(Product.id_user == id)

        if not user:
            return response.badRequest([], 'Tidak ada data user')

        dataproduct = formatProduct(product)

        data = singleDetailUser(user, dataproduct)

        return response.success(data, "success")

    except Exception as e:
        print(e)

def singleDetailUser(user, product):
    data = {
        'id' : user.id,
        'name' : user.name,
        'role' : user.role,
        'email' : user.email,
        'phone' : user.phone,
        'address' : user.address,
        'product' : product
    }

    return data


def singleProduct(product):
    data = {
        'id' : product.id,
        'type' : product.type,
        'name' : product.name,
        'descrption' : product.description,
        'set' : product.set,
        'quantity' : product.qty,
        'price' : product.price,
    }

    return data


def formatProduct(data):
    array = []
    for i in data:
        array.append(singleProduct(i))
    return array