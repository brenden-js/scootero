from flask import Flask
from flask_restful import Api
from resources.home import Home
from resources.user import User, UserRegister, UserLogin
from resources.route import Route, ViewRoute
from flask_jwt_extended import JWTManager

from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://anqjvxcg:PTCM_c1DuP8wd5DARTgi23IwASZ0C0qv@kashin.db.elephantsql.com:5432/anqjvxcg'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
api = Api(app)
app.config["JWT_SECRET_KEY"] = "so-secret"
jwt = JWTManager(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(Home, "/")
api.add_resource(User, "/u/<string:username>")
api.add_resource(UserRegister, "/register")
api.add_resource(UserLogin, "/login")
api.add_resource(Route, "/route")
api.add_resource(ViewRoute, "/view/<int:route_id>")


if __name__ == "__main__":
    db.init_app(app)
    app.run(debug=True)