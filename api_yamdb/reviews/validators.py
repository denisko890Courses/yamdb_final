from datetime import datetime


def year_validator(year):
    """Проверка, что год не может быть больше текущего."""
    if year > datetime.now().year:
        raise ValueError(
            "Машина времени ещё не изобретена! Произведение ещё не вышло!")
