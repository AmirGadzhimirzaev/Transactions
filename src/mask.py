def get_mask_card_number(card_number: int | str) -> str:
    """Функция возвращает маску номера по правилу XXXX XX** **** XXXX"""

    texted_number = str(card_number)

    if card_number is None:
        return "Номер карты не должен быть None!"
    elif len(card_number) != 16:
        return "Номер карты должен содержать 16 цифр!"
    elif not card_number.isdigit():
        return "Номер карты должен содержать только цифры!"
    else:
        return f"{texted_number[:4]} {texted_number[4:6]}** **** {texted_number[-4:]}"


def get_mask_account(account_number: int | str) -> str:
    """Функция возвращает маску номера по правилу **XXXX"""
    str_account_number = str(account_number)

    if account_number is None:
       return "Номер аккаунта не должен быть None!"
    elif len(str_account_number) != 20:
        return "Номер аккаунта должен содержать 20 цифр!"
    elif not str_account_number.isdigit():
        return "Номер аккаунта должен содержать только цифры!"
    else:
        return f"**{str_account_number[-4:]}"


