from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.models import Tour

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///booking.db'
app.config['SECRET_KEY'] = 'sqliteFlask'

db = SQLAlchemy(app)

with app.app_context():
    from app import models, routes
    db.create_all()
    initial_books = [
        Tour(title='Catalonia', description='Visit Barcelona, Catalonia, Spain', price=1000),
        Tour(title='France', description='Visit Paris, France', price=5000),
        Tour(title='England', description='Visit London, England, UK', price=10000)
    ]
    db.session.bulk_save_objects(initial_books)
    db.session.commit()