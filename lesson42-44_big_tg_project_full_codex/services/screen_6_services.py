"""Сервисы экрана 6: получение подробностей выбранного города."""

from api.wikipedia_api import get_city_info


def get_selected_city_info(city_name: str) -> tuple[str, str | None]:
    """Возвращает описание и изображение выбранного города."""

    return get_city_info(city_name)
