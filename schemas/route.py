from ma import ma
from models.route import RouteModel


class RouteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RouteModel
        load_instance = True
        include_fk = True
