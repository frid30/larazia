from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
tables = db.metadata.tables.keys()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.Integer)
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    email = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))

    def __init__(self, phone_number,first_name,last_name,email,password):
        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
db.create_all()
print(tables)
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id','first_name','last_name','email','password')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class UserManager(Resource):
    @staticmethod
    def get():
        try:
            id = request.args['id']
        except Exception as _:
            id = None
        if not id:
            users = User.query.all()
            return jsonify(users_schema.dump(users))
        user = User.query.get(id)
        return jsonify(user_schema.dump(user))

    @staticmethod
    def post():
        phone_number = request.json['phone_number']
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        email = request.json['email']
        password = request.json['password']
        user = User(phone_number, first_name, last_name, email, password)
        db.session.add(user)
        db.session.commit()
        return jsonify({
            'Message': f'User {first_name} {last_name} inserted.'
        })

    @staticmethod
    def put():
        try:
            id = request.args['id']
        except Exception as _:
            id = None
        if not id:
            return jsonify({'Message': 'Must provide the user ID'})
        user = User.query.get(id)

        phone_number = request.json['phone_number']
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        email = request.json['email']
        password = request.json['password']

        user.phone_number = phone_number
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.password = password

        db.session.commit()
        return jsonify({
            'Message': f'User {first_name} {last_name} altered.'
        })

    @staticmethod
    def delete():
        try:
            id = request.args['id']
        except Exception as _:
            id = None
        if not id:
            return jsonify({'Message': 'Must provide the user ID'})
        user = User.query.get(id)

        db.session.delete(user)
        db.session.commit()

        return jsonify({
            'Message': f'User {str(id)} deleted.'
        })


api.add_resource(UserManager, '/api/users')

if __name__ == '__main__':
    app.run(debug=True)
