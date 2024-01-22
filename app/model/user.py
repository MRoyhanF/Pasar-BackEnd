from app import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    email = db.Column(db.String(60), index=True, unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return'<User {}>'.format(self.name)