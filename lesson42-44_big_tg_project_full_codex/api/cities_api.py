import requests

from models.city import City

# Учётная запись GeoNames для учебного проекта.
GEONAMES_USERNAME = "a.m.smyslov2808"
GEONAMES_SEARCH_URL = "https://secure.geonames.org/searchJSON"
GEONAMES_NEARBY_URL = "https://secure.geonames.org/findNearbyPlaceNameJSON"
WIKIPEDIA_API_URL = "https://ru.wikipedia.org/w/api.php"
# Википедия просит представлять приложение через понятный User-Agent.
WIKIPEDIA_HEADERS = {"User-Agent": "TravelHunterSchoolBot/1.0 (educational project)"}
# В бесплатном тарифе GeoNames максимальный радиус этого endpoint — 300 км.
NEARBY_CITIES_RADIUS = 300


def find_city(city_name: str) -> City | None:
    """Ищет город по названию и возвращает его координаты."""

    response = requests.get(
        GEONAMES_SEARCH_URL,
        params={"q": city_name, "maxRows": 1, "featureClass": "P", "username": GEONAMES_USERNAME},
        timeout=10,
    )
    response.raise_for_status()
    cities = response.json().get("geonames", [])
    if len(cities) == 0:
        return None

    city_data = cities[0]
    return City(
        name=city_data["name"],
        latitude=float(city_data["lat"]),
        longitude=float(city_data["lng"]),
        country=city_data.get("countryName", ""),
    )


def find_nearby_cities(city: City) -> list[City]:
    """Ищет до пяти ближайших городов в доступном радиусе GeoNames."""

    response = requests.get(
        GEONAMES_NEARBY_URL,
        params={
            "lat": city.latitude,
            "lng": city.longitude,
            "radius": NEARBY_CITIES_RADIUS,
            "maxRows": 20,
            "username": GEONAMES_USERNAME,
        },
        timeout=10,
    )
    response.raise_for_status()
    cities = []
    for city_data in response.json().get("geonames", []):
        if city_data.get("name", "").lower() == city.name.lower():
            continue
        cities.append(
            City(
                name=city_data["name"],
                latitude=float(city_data["lat"]),
                longitude=float(city_data["lng"]),
                country=city_data.get("countryName", ""),
                distance=float(city_data.get("distance", 0)),
            )
        )
    return cities[:5]


def get_city_info(city_name: str) -> tuple[str, str | None]:
    """Получает краткое описание города и ссылку на его изображение из Википедии."""

    response = requests.get(
        WIKIPEDIA_API_URL,
        params={
            "action": "query",
            "format": "json",
            "prop": "extracts|pageimages",
            "exintro": 1,
            "explaintext": 1,
            "piprop": "original",
            "titles": city_name,
        },
        headers=WIKIPEDIA_HEADERS,
        timeout=10,
    )
    response.raise_for_status()
    pages = response.json().get("query", {}).get("pages", {})
    page = next(iter(pages.values()), {})
    description = page.get("extract", "")
    image_url = page.get("original", {}).get("source")
    return description, image_url
