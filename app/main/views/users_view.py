from flask import Blueprint, request, json
from flask_restful import reqparse, request
from app.main.controllers.users_controller import users

mod_users = Blueprint('users', __name__, url_prefix='/api/v1')

usr = users()


@mod_users.route('/signin', methods=['GET', 'POST'])
def signin():
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True,
                        help='Email Required', location="json")
    parser.add_argument('password', type=str, required=True,
                        help='Password Required', location="json")
    data = parser.parse_args()
    return usr.user_signin(data)


@mod_users.route('/signup', methods=['GET', 'POST'])
def signup():
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True,
                        help='Username Required', location="json")
    parser.add_argument('email', type=str, required=True,
                        help='Email Required', location="json")
    parser.add_argument('password', type=str, required=True,
                        help='Password Required', location="json")
    data = parser.parse_args()
    return usr.create_user(data)


@mod_users.route('/', methods=['GET'])
def root():
    return ("FOOD API V1 .An api service for the First-food-fast project")



