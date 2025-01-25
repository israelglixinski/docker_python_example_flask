from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI', 'postgresql://user:password@localhost:5432/database')
db = SQLAlchemy(app)

class ExampleModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
