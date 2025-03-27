import src.mask as m


def mask_account_card(typed_card_number: str) -> str:
    """Функция возвращает строку с замаскированным номером"""

    if typed_card_number[:4] == "Счет":
        return f"{typed_card_number[:-21]} {m.get_mask_account(typed_card_number[-20:])}"
    else:
        return f"{typed_card_number[:-17]} {m.get_mask_card_number(typed_card_number[-16:])}"


def get_date(date: str) -> str:
    """Функция возвращает строку с датой в формате ДД.ММ.ГГГГ"""

    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
