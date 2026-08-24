import requests

from models.city import City

GEONAMES_USERNAME = "a.m.smyslov2808"
GEONAMES_SEARCH_URL = "https://secure.geonames.org/searchJSON"
GEONAMES_NEARBY_URL = "https://secure.geonames.org/findNearbyPlaceNameJSON"
WIKIPEDIA_API_URL = "https://ru.wikipedia.org/w/api.php"


def find_city(city_name: str) -> City | None:
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
        country=city_data["countryName"],
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
        },
        timeout=10,
    )
    response.raise_for_status()

    cities_data = response.json()["geonames"]
    output_cities = []

    for current_city in cities_data:
        distance = float(current_city["distance"])
        population = int(current_city["population"])

        # Отбрасываем исходный город, районы и маленькие города-спутники.
        if current_city["name"].lower() == city.name.lower():
            continue
        if distance < 50:
            continue
        if population < 250000:
            continue

        output_cities.append(
            City(
                name=current_city["name"],
                latitude=float(current_city["lat"]),
                longitude=float(current_city["lng"]),
                country=current_city["countryName"],
                distance=distance,
            )
        )

        # Для экрана бота достаточно семи городов.
        if len(output_cities) == 7:
            break

    return output_cities


def get_city_info(city_name: str) -> tuple[str, str | None]:
    """Получает краткое описание города и ссылку на его изображение из Википедии."""

    # formatversion=2 заставляет Wikipedia вернуть страницы обычным списком.
    response = requests.get(
        WIKIPEDIA_API_URL,
        params={
            "action": "query",
            "format": "json",
            "formatversion": 2,
            "prop": "extracts|pageimages",
            "exintro": 1,
            "explaintext": 1,
            "piprop": "original",
            "titles": city_name,
        },
        headers={"User-Agent": "TravelHunterSchoolBot/1.0 (educational project)"},
        timeout=10,
    )
    response.raise_for_status()

    pages_data = response.json()["query"]["pages"]
    if len(pages_data) == 0:
        return "", None

    page_data = pages_data[0]
    description = page_data.get("extract", "")

    image_url = None
    if "original" in page_data:
        image_url = page_data["original"]["source"]

    return description, image_url
