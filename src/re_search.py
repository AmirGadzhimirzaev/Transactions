import re
from collections import Counter


def get_data_by_str(list_of_dict_data: list, search_str: str) -> list | str:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка"""
    if list_of_dict_data is not None and isinstance(list_of_dict_data, list) and len(list_of_dict_data) > 0:
        return [
            dct
            for dct in list_of_dict_data
            if re.search(rf"{search_str}", dct["description"] if isinstance(dct["description"], str) else "")
        ]
    else:
        return "Ошибка в get_data_by_str"


def get_data_by_category(list_of_dict_data: list, category_list: list | None = None) -> dict | str:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций, а возвращает
    словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории"""

    if list_of_dict_data is not None and isinstance(list_of_dict_data, list) and len(list_of_dict_data) > 0:
        return dict(Counter([dct["description"] for dct in list_of_dict_data if isinstance(dct["description"], str)]))
    else:
        return "Ошибка в get_data_by_category"
