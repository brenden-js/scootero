from time import time
from gmaps import Gmaps
from db import db


class RouteModel(db.Model):
    __tablename__ = 'routes'
    route_id = db.Column(db.Integer, primary_key=True, nullable=False)
    route_name = db.Column(db.String, unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    start_latitude = db.Column(db.Float, nullable=False)
    start_longitude = db.Column(db.Float, nullable=False)
    start_time = db.Column(db.Float, nullable=False)

    end_latitude = db.Column(db.Float, nullable=True)
    end_longitude = db.Column(db.Float, nullable=True)
    end_time = db.Column(db.Float, nullable=True)

    co2_saved = db.Column(db.Float, nullable=True)
    usd_saved = db.Column(db.Float, nullable=True)
    miles_travelled = db.Column(db.Float, nullable=True)

    def start_route(self):
        self.save_to_db()

    @classmethod
    def end_route(cls, route_id, end_latitude, end_longitude):
        route = cls.find_by_id(route_id)

        route.end_latitude = end_latitude
        route.end_longitude = end_longitude
        route.end_time = time()

        start_coords = {"lat": route.start_latitude,
                        "lng": route.start_longitude}

        end_coords = {"lat": route.end_latitude,
                      "lng": route.end_longitude}

        maps_data = Gmaps.get_maps_data(start_coords, end_coords)
        distance_meters = Gmaps.get_distance(maps_data)
        distance_miles = Gmaps.meters_to_miles(distance_meters)

        route.co2_saved = Gmaps.calculate_co2_savings(distance_miles)
        route.usd_saved = Gmaps.calculate_car_savings(distance_miles)
        route.miles_travelled = distance_miles
        route.save_to_db()
        return route

    @classmethod
    def find_by_id(cls, route_id):
        return cls.query.filter_by(route_id=route_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def calculate_co2(cls, route_distance):
        return route_distance

    @classmethod
    def calculate_usd(cls, route_distance):
        return route_distance
