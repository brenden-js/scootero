from flask_restful import Resource
from flask import jsonify, request
from schemas.user import UserSchema
from models.user import UserModel
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token, create_refresh_token

user_schema = UserSchema()


class UserRegister(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        user = user_schema.load(user_json)
        user.save_to_db()

        return jsonify({"message": f"User {user.username} added to db"})


class User(Resource):
    @classmethod
    def get(cls, username):
        user = UserModel.find_by_username(username)
        return user_schema.dump(user)


class UserLogin(Resource):
    @classmethod
    def post(cls):
        user_json = request.get_json()
        user_data = user_schema.load(user_json, partial=("email",))

        user = UserModel.find_by_username(user_data.username)

        if user and safe_str_cmp(user.password, user_data.password):
            access_token = create_access_token(user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {"access_token": access_token, "refresh_token": refresh_token}

        return {"message": "dat aint wight"}
