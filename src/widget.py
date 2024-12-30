import src.mask as m


def mask_account_card(typed_card_number: str) -> str:
    """Функция возвращает строку с замаскированным номером"""

    if typed_card_number[:4] == "Счет":
        return f"{typed_card_number[:-21]} {m.get_mask_account(typed_card_number[-20:])}"
    else:
        return f"{typed_card_number[:-17]} {m.get_mask_card_number(typed_card_number[-16:])}"
