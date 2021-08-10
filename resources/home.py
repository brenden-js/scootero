from flask import render_template, make_response
from flask_restful import Resource
from schemas.user import UserSchema

user_schema = UserSchema()


class Home(Resource):
    @classmethod
    def get(cls):
        return make_response(render_template("home.html"))
