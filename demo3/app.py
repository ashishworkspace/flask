from flask import  Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask("demo3")

#URL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///root/flask/demo3/mydb/data.sqlite'

#ORM
db = SQLAlchemy(app)

class Students(db.Model):
        index = db.Column(db.Integer, primary_key=True)
        name = db.Column(db.Text)
        age = db.Column(db.Integer)
        character = db.Column(db.Text)
        def __init__(self, name, age, character):
            self.name = name
            self.age = age
            self.character = character

db.create_all()
