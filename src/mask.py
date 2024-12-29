def get_mask_card_number(card_number: int | str) -> str:
    """Функция возвращает маску номера по правилу XXXX XX** **** XXXX"""
    mask_of_card = [str(card_number)[int(num, 16)] if num.isalnum() else num for num in "0123 45** **** CDEF"]

    return "".join(mask_of_card)


def get_mask_account(account_number: int | str) -> str:
    """Функция возвращает маску номера по правилу **XXXX"""
    last_four_digits = str(account_number)[-4:]

    return f"**{last_four_digits}"
