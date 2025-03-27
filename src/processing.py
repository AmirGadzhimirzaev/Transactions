def filter_by_state(list_of_dict: list[dict], state: str = "EXECUTED") -> list[dict] | str:
    """
    Функция возвращает новый список словарей,
    содержащий только те словари,
    у которых ключ 'state' соответствует указанному значению.
    """

    if state in ["EXECUTED", "CANCELED"] and isinstance(list_of_dict, list):
        return list(filter(lambda x: x["state"] == state, list_of_dict))
    else:
        return "Возникла ошибка!"


def sorted_by_state(list_of_dict: list[dict], in_descending_order: bool = True) -> list[dict] | str:
    """Функция возвращает новый список словарей отсортированных по дате."""

    if isinstance(list_of_dict, list) and len(list_of_dict) != 0 and isinstance(in_descending_order, bool):
        return sorted(list_of_dict, key=lambda x: x["date"], reverse=in_descending_order)
    else:
        return "Что-то пошло не так!"
