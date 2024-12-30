def get_mask_card_number(card_number: int | str) -> str:
    """Функция возвращает маску номера по правилу XXXX XX** **** XXXX"""
    texted_number = str(card_number)

    return f"{texted_number[:4]} {texted_number[4:6]}** **** {texted_number[-4:]}"


def get_mask_account(account_number: int | str) -> str:
    """Функция возвращает маску номера по правилу **XXXX"""
    last_four_digits = str(account_number)[-4:]

    return f"**{last_four_digits}"
