from app import db
from app.model.user import User
from app.model.product import Product
from datetime import datetime


class Transaction(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    id_user = db.Column(db.BigInteger, db.ForeignKey(User.id))
    id_product = db.Column(db.BigInteger, db.ForeignKey(Product.id))
    qty = db.Column(db.Integer(), nullable=False)
    Amount = db.Column(db.Integer(), nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow)
    


    def __repr__(self):
        return'<Transaction {}>'.format(self.name)