"""Формирование текстов для разделов, доступных из главного меню."""

from api.holidays_api import *
from models.visited_city import VisitedCity


def get_screen_3_holidays_text(holidays: list[Holiday]) -> str:
    """Преобразует модели праздников в готовое сообщение Telegram."""

    # Для пустого результата возвращаем отдельное понятное пользователю сообщение.
    if len(holidays) == 0:
        return (
            "К сожалению, ни одного праздника не найдено.\n"
            "Рекомендуем придумать себе праздник самостоятельно."
        )

    # Текст строится отдельно от обработчика, чтобы UI-логику было проще
    # тестировать без запуска Telegram-бота.
    output_text = "Список праздников:\n\n"

    # Нумеруем праздники и последовательно добавляем их данные в общий текст.
    for i in range(0, len(holidays)):
        output_text += f"{i+1}. {holidays[i].name}\n"
        output_text += f"Дата праздника: {holidays[i].date_to_str()}\n"
        output_text += f"Страна: {holidays[i].country}\n\n"

    return output_text


def get_screen_4_city_input_text() -> str:
    """Возвращает приглашение перейти к вводу исходного города."""
    return "Введите название города, из которого Вы хотите отправиться в путешествие на выходные."


def get_screen_7_visited_cities_text(visited_cities: list[VisitedCity]) -> str:
    """Формирует сообщение со всей историей поездок пользователя."""

    # Пустая история отображается отдельным сообщением без заголовка списка.
    if len(visited_cities) == 0:
        return "Список городов пуст."

    output_text = "Список посещённых городов:\n\n"

    # Репозиторий уже возвращает записи от новых к старым.
    for visited_city in visited_cities:
        output_text += (
            f"{visited_city.arrival_date_to_normal_str()} - {visited_city.name}\n\n"
        )

    return output_text
