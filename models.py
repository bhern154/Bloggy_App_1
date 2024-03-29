from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = 'user_tb'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    first_name = db.Column(db.String(30),
                     nullable=False)
    
    last_name = db.Column(db.String(30),
                     nullable=False)

    image_url = db.Column(db.String(30), default='https://cdn-icons-png.flaticon.com/512/9131/9131529.png')

                     


