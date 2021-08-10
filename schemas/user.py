from ma import ma
from models.user import UserModel
from schemas.route import RouteSchema


class UserSchema(ma.SQLAlchemyAutoSchema):
    routes = ma.Nested(RouteSchema, many=True)

    class Meta:
        model = UserModel
        load_only = ("password",)
        dump_only = ("id", "total_co2_saved", "total_usd_saved")
        load_instance = True
        include_fk=True
