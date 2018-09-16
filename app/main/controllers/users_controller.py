from flask import jsonify, make_response

import re


class users(object):

    def __init__(self):
        self.users = []

    def validate_password(self, password):
        if len(password) < 6:
            response_object = {
                "status": "fail",
                "message": "Password length is less than 6"
            }
            return(make_response(jsonify(response_object)))
        elif len(password) > 12:
            response_object = {
                "status": "fail",
                "message": "Password length must be less than 12"
            }
            return(make_response(jsonify(response_object)))
        else:
            return True

    def validate_email(self, email):
        match = re.match(
            '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
        if match == None:
            response_object = {
                "status": "fail",
                "message": "Please enter a valid email"
            }
            return(make_response(jsonify(response_object)))
        else:
            return True

    def validate_username(self, username):
        if len(username) < 4 or len(username) > 10:
            response_object = {
                "status": "fail",
                "message": "username should be between 4 and 10 characters"
            }
            return(make_response(jsonify(response_object)))
        else:
            return True

    def create_user(self, data):
        password = self.validate_password(data['password'])
        username = self.validate_username(data['username'])
        email = self.validate_email(data['email'])
        if password and username and email is True:
            user_id = len(self.users) + 1
            user = {"id": user_id, "email": email,
                    "password": password, "username": username}
            self.users.append(user)
            response_object = {
                "status": "success",
                "message": "Registered successfully"
            }
            return(make_response(jsonify(response_object)))
        else:
            if password is not True:
                return password
            elif email is not True:
                return email
            elif username is not True:
                return username

    def user_signin(self, data):
        email = self.validate_email(data['email'])
        password = self.validate_password(data['password'])
        if email and password is True:
            user = self.check_if_user_exists(data)
            if user is True:
                credentials = self.check_credentials(
                    email=data['email'], password=data['password'])
            else:
                return("fail")
        else:
            if password is not True:
                return password
            elif email is not True:
                return email

    def check_if_user_exists(self, data):
        if len(self.users) > 0:
            for user in self.users:
                if user['email'] == data['email']:
                    return True
                else:
                    response_object = {
                        "status": "fail",
                        "message": "Email does not exist"
                    }
                    return(make_response(jsonify(response_object)))
        else:
            response_object = {
                "status": "fail",
                "message": "User does no exist"
            }
            return(make_response(jsonify(response_object)))

    def check_credentials(self, email, password):
        for user in self.users:
            if email in dict.values(user):
                if password == user[password]:
                    return True
                else:
                    response_object = {
                        "status": "fail",
                        "message": "Check your email or password"
                    }
                    return(make_response(jsonify(response_object)))
