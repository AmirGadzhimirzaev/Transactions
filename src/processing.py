def filter_by_state(list_of_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция возвращает новый список словарей,
    содержащий только те словари,
    у которых ключ 'state' соответствует указанному значению.
    """

    return list(filter(lambda x: x["state"] == state, list_of_dict))


def sorted_by_state(list_of_dict: list[dict], in_descending_order: bool = True) -> list[dict]:
    """Функция возвращает новый список словарей отсортированных по дате."""

    return sorted(list_of_dict, key=lambda x: x["date"], reverse=in_descending_order)
