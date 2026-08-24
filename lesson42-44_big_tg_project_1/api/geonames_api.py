import requests

from models.city import City

GEONAMES_USERNAME = "a.m.smyslov2808"
GEONAMES_SEARCH_URL = "https://secure.geonames.org/searchJSON"
GEONAMES_NEARBY_URL = "https://secure.geonames.org/findNearbyPlaceNameJSON"


def find_city_by_name(city_name: str) -> City | None:
    """Ищет город по названию и возвращает его координаты."""

    # Отправляем название города в GeoNames.
    response = requests.get(
        GEONAMES_SEARCH_URL,
        params={
            "q": city_name,
            "maxRows": 1,
            "featureClass": "P",
            "lang": "ru",
            "username": GEONAMES_USERNAME,
            "countryCode": "RU",
        },
        timeout=10,
    )

    # Если API вернул ошибку, программа создаст исключение.
    response.raise_for_status()

    # В ключе geonames находится список найденных городов.
    cities_data = response.json()["geonames"]
    if len(cities_data) == 0:
        return None

    # Берём первый город и превращаем словарь API в объект City.
    city_data = cities_data[0]
    return City(
        name=city_data["name"],
        latitude=float(city_data["lat"]),
        longitude=float(city_data["lng"]),
    )


def find_nearby_cities(city: City) -> list[City]:
    """Ищет ближайшие крупные города в доступном радиусе GeoNames."""

    # Просим API найти населённые пункты в радиусе 300 километров.
    response = requests.get(
        GEONAMES_NEARBY_URL,
        params={
            "lat": city.latitude,
            "lng": city.longitude,
            "radius": 300,
            "maxRows": 500,
            "cities": "cities15000",
            "lang": "ru",
            "username": GEONAMES_USERNAME,
            "countryCode": "RU",
        },
        timeout=10,
    )
    response.raise_for_status()

    cities_data = response.json()["geonames"]
    output_cities = []

    for current_city in cities_data:
        distance = float(current_city["distance"])
        population = int(current_city["population"])

        if distance >= 50 and population >= 250000:
            output_cities.append(
                City(
                    name=current_city["name"],
                    latitude=float(current_city["lat"]),
                    longitude=float(current_city["lng"]),
                    distance=distance,
                )
            )

    output_cities = sorted(
        output_cities,
        key=lambda city: city.distance,
    )

    return output_cities[:5]
