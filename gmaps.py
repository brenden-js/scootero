import googlemaps
API_KEY = 'AIzaSyB58fU8MisvT4TJ0p7cYVB5hwaAz8RKfiw'
key = API_KEY

gmaps = googlemaps.Client(key=key)


class Gmaps():
    @classmethod
    def get_maps_data(cls, start_coords, end_coords):
        maps_data = gmaps.distance_matrix(start_coords, end_coords)
        return maps_data

    @classmethod
    def get_distance(cls, maps_data):
        distance = maps_data['rows'][0]['elements'][0]['distance']['value']
        return distance

    @classmethod
    def meters_to_miles(cls, meters):
        miles = meters * 0.000621371
        return miles

    @classmethod
    def calculate_car_savings(cls, miles):
        dollars = miles * .575
        return dollars

    @classmethod
    def calculate_co2_savings(cls, miles):
        grams_of_co2 = miles * 404
        return grams_of_co2

