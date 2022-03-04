from models.route import RouteModel
from time import time
from flask_restful import Resource
from flask import jsonify, request
from schemas.route import RouteSchema
from flask_jwt_extended import get_jwt_identity, jwt_required

route_schema = RouteSchema()


class Route(Resource):
    @classmethod
    @jwt_required(optional=False)
    def get(cls):
        user_id = get_jwt_identity()
        if user_id:
            return jsonify({"message": "Click the button to start your route"})
        else:
            return jsonify({"message": "You must be logged in to create a new route"})

    @classmethod
    @jwt_required(optional=False)
    def post(cls):
        user_id = get_jwt_identity()
        user_json = request.get_json()
        user_json["user_id"] = user_id
        user_json["start_time"] = time()
        new_route = route_schema.load(user_json)
        new_route.start_route()

        return jsonify({"message": f"Route: {user_json['route_name']} has started"})

    @classmethod
    @jwt_required(optional=False)
    def put(cls):
        user_json = request.get_json()
        route = RouteModel.end_route(user_json["route_id"],
                                     user_json["end_latitude"],
                                     user_json["end_longitude"])

        return jsonify({"route_length": route.miles_travelled,
                        "co2_saved": route.co2_saved,
                        "usd_saved": route.usd_saved})


class ViewRoute(Resource):
    @classmethod
    @jwt_required(optional=False)
    def get(cls, route_id):
        user_id = get_jwt_identity()
        route = RouteModel.find_by_id(route_id)
        if user_id == route.user_id:
            return route_schema.dump(route)
        else:
            return jsonify({"message": "You must be signed in"})
