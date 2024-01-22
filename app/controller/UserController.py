from app.model.user import User

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