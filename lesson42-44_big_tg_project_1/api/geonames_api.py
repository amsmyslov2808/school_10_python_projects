"""Функции для поиска российских городов через сервис GeoNames.

Модуль относится к слою внешних API: он формирует HTTP-запросы, проверяет
ответы сервера и преобразует JSON-словари GeoNames в объекты ``City``.
Остальные части приложения благодаря этому не зависят от формата ответа API.
"""

import requests

from models.city import City

# Имя пользователя служит ключом доступа к GeoNames. Для настоящего проекта
# его лучше получать из переменной окружения или конфигурационного файла.
GEONAMES_USERNAME = "a.m.smyslov2808"

# Разные операции GeoNames выполняются через разные адреса: первый ищет город
# по тексту, второй — населённые пункты около заданных координат.
GEONAMES_SEARCH_URL = "https://secure.geonames.org/searchJSON"
GEONAMES_NEARBY_URL = "https://secure.geonames.org/findNearbyPlaceNameJSON"


def find_city_by_name(city_name: str) -> City | None:
    """Ищет российский город по названию и возвращает его координаты.

    Если GeoNames не нашёл ни одного подходящего населённого пункта, функция
    возвращает ``None``. Сетевые и HTTP-ошибки намеренно не перехватываются:
    их обрабатывает UI-слой, где пользователю можно показать понятное сообщение.
    """

    # Отправляем название города в GeoNames.
    response = requests.get(
        GEONAMES_SEARCH_URL,
        params={
            "q": city_name,
            "maxRows": 1,  # Достаточно наиболее релевантного результата.
            "featureClass": "P",  # P — города и другие населённые пункты.
            "lang": "ru",
            "username": GEONAMES_USERNAME,
            "countryCode": "RU",  # Ограничиваем поиск территорией России.
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
    """Возвращает до пяти крупных городов рядом с исходным городом.

    Подходящим считается российский город с населением не менее 250 000
    человек, находящийся на расстоянии от 50 до 300 километров. Исходный город
    и его ближайшие пригороды тем самым исключаются из результата.
    """

    # Просим API найти населённые пункты в радиусе 300 километров.
    response = requests.get(
        GEONAMES_NEARBY_URL,
        params={
            "lat": city.latitude,
            "lng": city.longitude,
            "radius": 300,
            "maxRows": 500,
            # GeoNames сначала ограничивает выдачу городами от 15 000 жителей;
            # более строгий порог в 250 000 применяется ниже в Python.
            "cities": "cities15000",
            "lang": "ru",
            "username": GEONAMES_USERNAME,
            "countryCode": "RU",
        },
        timeout=10,
    )
    response.raise_for_status()

    # Накапливаем только города, удовлетворяющие условиям поездки выходного дня.
    cities_data = response.json()["geonames"]
    output_cities = []

    for current_city in cities_data:
        distance = float(current_city["distance"])
        population = int(current_city["population"])

        # Расстояние уже рассчитано GeoNames относительно координат city.
        if distance >= 50 and population >= 250000:
            output_cities.append(
                City(
                    name=current_city["name"],
                    latitude=float(current_city["lat"]),
                    longitude=float(current_city["lng"]),
                    distance=distance,
                )
            )

    # Сначала показываем пользователю самые близкие варианты.
    output_cities = sorted(
        output_cities,
        key=lambda city: city.distance,
    )

    # Интерфейс экрана рассчитан максимум на пять предложений.
    return output_cities[:5]
