from typing import Generator


def filter_by_currency(transactions: list[dict], currency: str | None = None) -> Generator | str:
    """Функция поочереди возвращает итератор со словарями в зависимости от валюты"""

    if isinstance(transactions, list) and len(transactions) > 0:
        if currency == "RUB":
            return (data for data in transactions if data["operationAmount"]["currency"]["code"] == "RUB")
        elif currency == "USD":
            return (data for data in transactions if data["operationAmount"]["currency"]["code"] == "USD")
        else:
            return (data for data in transactions)
    else:
        return "Что-то пошло не так!"


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """Функция-генератор поочереди возвращает описание входящих операций"""

    for data in transactions:
        yield data["description"]

    while True:
        yield "Данных больше нет!"


def card_number_generator(start_value: int = 0, end_value: int = 1) -> Generator:
    """Функция-генератор номеров банковских карт в заданном диапазоне в формате XXXX XXXX XXXX XXXX"""

    for card_nuber in range(start_value, end_value + 1):
        if card_nuber >= 10000000000000000:
            break
        formated_cn = str(card_nuber).zfill(16)
        yield f"{formated_cn[0:4]} {formated_cn[4:8]} {formated_cn[8:12]} {formated_cn[12:17]}"

    while True:
        yield "Достигнут предел диапазона!"
