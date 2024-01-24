from app.model.user import User
from app.model.product import Product

from flask import render_template, jsonify
from flask_jwt_extended import get_jwt_identity

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
    own = User.query.filter(id == data.id_user).first()
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


# get detail data product
def detail(id):
    try:
        product = Product.query.filter_by(id=id).first()

        if not product:
            return response.badRequest([], 'Tidak ada data product')

        owner = get_owner_name(product.id_user)
        data = singleDetailProduct(product, owner)

        return response.success(data, "success")

    except Exception as e:
        print(e)

def get_owner_name(user_id):
    user = User.query.get(user_id)
    return user.name if user else None

def singleDetailProduct(user, owner=None):
    data = {
        'id' : user.id,
        'type' : user.type,
        'name' : user.name,
        'description' : user.description,
        'set' : user.set,
        'quantity' : user.qty,
        'price' : user.price,
        'owner': owner,
    }

    return data

#create product
def save():
    try :
        current_user = get_jwt_identity()
        # print("Current User:", current_user)
        
        if not isinstance(current_user, dict):
            return response.badRequest([], 'Invalid user identity in JWT')

            # Pastikan atribut 'name' tersedia di dalam objek current_user
        if 'id' not in current_user:
            return response.badRequest([], 'Field "id" not found in current_user')

        id_user = current_user['id']
        # print("id user :", id_user)

        type = request.form.get('type')
        name = request.form.get('name')
        description = request.form.get('description')
        set = request.form.get('set')
        quantity = request.form.get('quantity')
        price = request.form.get('price')

        input = [
            {
                'typpe' : type,
                'name' : name,
                'description' : description,
                'set' : set,
                'quantity' : quantity,
                'price' : price,
                'id_user' : id_user,
            }
        ]

        product = Product(type=type, name=name, description=description, set=set, qty=quantity, price=price, id_user=id_user)

        db.session.add(product)
        db.session.commit()

        return response.success(input, 'create product successfully')
        
    except Exception as e:
        print(e)
        return response.badRequest([], 'Failed to create product')

#hapus data user
def delete(id):
    try:
        product = Product.query.filter_by(id=id).first()
        if not product:
            return response.badRequest([], 'Data Prodcut Kosong...!!')
        
        db.session.delete(product)
        db.session.commit()

        return response.success('', 'Berhasil Menghapus Data Product...!')

    except Exception as e:
        print(e) 