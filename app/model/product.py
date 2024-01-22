from app import db
from app.model.user import User


class Product(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    type = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    set = db.Column(db.String(20), nullable=False)
    qty = db.Column(db.Integer(), nullable=False)
    price = db.Column(db.Integer(), nullable=False)
    id_user = db.Column(db.BigInteger, db.ForeignKey(User.id))


    def __repr__(self):
        return'<Product {}>'.format(self.name)