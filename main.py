from dataclasses import dataclass
from flask import Flask, request, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

@dataclass
class UserModel(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), nullable=False)
    age: int = db.Column(db.Integer, nullable=False)
    gender: str = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'User(name={name}, age={age}, gender={gender})'

@app.route('/', methods=['GET'])
def get_all_users():
    users = UserModel.query.all()
    return jsonify(users)

@app.route('/', methods=['POST'])
def create_user():
    user = UserModel(name="Modi", age=22, gender="male")
    db.session.add(user)
    db.session.commit()
    return jsonify(user), 201

@app.route('/', methods=['PUT'])
def update_user():
    return {'data': 'This is still under development'}

if __name__ == "__main__":
    app.run(debug=True)