import re

from src import mask


def mask_account_card(typed_card_number: str) -> str:
    """Функция возвращает строку с замаскированным номером"""

    if typed_card_number is None or not isinstance(typed_card_number, str) or len(typed_card_number) <= 0:
        return "Неверный формат!"
    else:
        all_digits = re.search(r"\d+", typed_card_number).group()

    if len(all_digits) == 20:
        all_digits = mask.get_mask_account(all_digits)
    elif len(all_digits) == 16:
        all_digits = mask.get_mask_card_number(all_digits)
    else:
        return "Неверный формат!"

    return re.sub(r"\d+", all_digits, typed_card_number)


def get_date(date: str) -> str:
    """Функция возвращает строку с датой в формате ДД.ММ.ГГГГ"""

    if (
        date is not None
        and isinstance(date, str)
        and len(date) > 0
        and re.search(r"^\d{4}-\d{2}-\d{2}", date) is not None
    ):
        return re.sub(r".*(\d{4})-(\d{2})-(\d{2}).*", r"\3.\2.\1", date)
    else:
        return "Неверный формат даты!"
