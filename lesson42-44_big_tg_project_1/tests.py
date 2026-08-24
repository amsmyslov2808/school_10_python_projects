from api.geonames_api import *

from models.city import City

a = find_nearby_cities(find_city_by_name("Брянск"))

v = 10
