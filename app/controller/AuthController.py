from app.model.user import User

from flask import render_template

from app import response, app, db
from flask import request
from flask_jwt_extended import JWTManager, create_access_token, create_refresh_token

import datetime

jwt = JWTManager(app)

#func tampil data login
def singleObject(data):
    data = {
        'id' : data.id,
        'name' : data.name,
        'role' : data.role,
        'email' : data.email,
        'phone' : data.phone,
        'address' : data.address,
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
        #return response.badRequest([], 'Failed to login')