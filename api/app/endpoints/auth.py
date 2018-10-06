# Signup, Sign In and Logout endpoints
# api/v1/auth/signup POST
# api/v1/auth/login POST
from app import API
from flask import request
from flask_restplus import Resource
from models.schema import Userschema, Loginschema
from models.user import NormalUser, LogInUser
# from models.revoked_token import RevokedTokenModel
from app.serializer import add_user, login_user

auth_ns = API.namespace('auth', description="Authentication/Authorization operations.")

@auth_ns.route('/signup')
class SignUp(Resource):
    """normal user signup resource """
    @API.expect(add_user)
    def post (self):
        signup_data = request.get_json()
        data, errors = Userschema.load(signup_data)
        if errors:
            return(errors),400
        else:
            new_user = NormalUser(
                data["username"],
                data["email"],
                data["password"],
                data["confirm_password"]
                )
        return new_user.save_user()

@auth_ns.route('/login')
class LogIn(Resource):
    """A user can login"""
    @API.expect(login_user)
    def post(self):
        login_data = request.get_json()
        data, errors =  Loginschema.load(login_data)
        if errors:
            return(errors),400
        else:
            if "username" in data.keys():
                Login_new_user = LogInUser(
                    username=data["username"],
                    password=data["password"]
                )
            elif "email" in data.keys():
                Login_new_user = LogInUser(
                    email=data["email"],
                    password=data["password"]
                )
        return Login_new_user.logging_in_normal_user()


# @auth_ns.route('/logout')
# class Logout(Resource):
#     """user can logout"""
#     def post(self):
#         jti = get_raw_jwt()['jti']
#         try:
#             revoked_token = RevokedTokenModel(jti = jti)
#             revoked_token.add()
#             return {'message': 'Access token has been revoked'}
#         except:
#             return {'message': 'Something went wrong'}, 500
