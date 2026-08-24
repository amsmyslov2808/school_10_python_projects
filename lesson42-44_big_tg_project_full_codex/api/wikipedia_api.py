import requests


WIKIPEDIA_API_URL = "https://ru.wikipedia.org/w/api.php"


def get_city_info(city_name: str) -> tuple[str, str | None]:
    """Получает описание города и ссылку на изображение из Википедии."""

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
