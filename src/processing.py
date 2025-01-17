def filter_by_state(list_of_dict: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция возвращает новый список словарей,
    содержащий только те словари,
    у которых ключ 'state' соответствует указанному значению.
    """

    return list(filter(lambda x: x["state"] == state, list_of_dict))
