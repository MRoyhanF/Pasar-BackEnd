from app.model.user import User
from app.model.product import Product

from app import response, app, db
from flask import request
from flask_jwt_extended import create_access_token, create_refresh_token

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

#create user
def save():
    try :
        name = request.form.get('name')
        role = 'User'
        email = request.form.get('email')
        password = request.form.get('password')
        phone = request.form.get('phone')
        address = request.form.get('address')

        input = [
            {
                'name' : name,
                'role' : role,
                'email' : email,
                'password' : password,
                'phone' : phone,
                'address' : address,
            }
        ]

        users = User(name=name, role=role, email=email, password=password, phone=phone, address=address)
        db.session.add(users)
        db.session.commit()

        return response.success(input, 'create user successfully')
        
    except Exception as e:
        print(e)

#update data user
def edit(id):
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        phone = request.form.get('phone')
        address = request.form.get('address')

        input = [
            {
                'name' : name,
                'email' : email,
                'password' : password,
                'phone' : phone,
                'address' : address,
            }
        ]
        
        user = User.query.filter_by(id=id).first()

        user.name = name
        user.email = email
        user.password = password
        user.phone = phone
        user.address = address

        db.session.commit()

        return response.success(input, 'Success Update Data !')
    
    except Exception as e:
        print(e)

#hapus data user
def delete(id):
    try:
        user = User.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], 'Data User Kosong...!!')
        
        db.session.delete(user)
        db.session.commit()

        return response.success('', 'Berhasil Menghapus Data User...!')

    except Exception as e:
        print(e) 

def singleObject(data):
    data = {
        'id' : data.id,
        'name' : data.name,
        "email" : data.email,
        'level' : data.level
    }
    
    return data 

#login user
def login():
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if not user:
            return response.badRequest([],'Email tidak terdaftar')
        
        if not user.checkPassword(password):
            return response.badRequest([],'Kombinasi Password Salah')
        
        data = singleObject(user)
        
        expires = datetime.timedelta(days=7)
        expires_refresh = datetime.timedelta(days=7)
        
        access_token = create_access_token(data, fresh=True, expires_delta= expires)
        refresh_token = create_refresh_token(data, expires_delta= expires_refresh)
        
        return response.success({
            "data" : data,
            "access_token" : access_token,
            "refresh_token" : refresh_token,
        }, "Sukses Login!")
    except Exception as e:
        print(e)