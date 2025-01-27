import src.mask as m


def mask_account_card(typed_card_number: str) -> str:
    """Функция возвращает строку с замаскированным номером"""

    list_of_payment_methods_names = ["maestro", "master card", "visa classic", "visa platinum", "visa gold"]

    if typed_card_number is None:
        return "Не может быть None!"
    elif isinstance(typed_card_number, str):
        return "Номер должен быть в строкой!"
    elif typed_card_number[:4].lower() in ["счёт", "счет"]:
        return f"{typed_card_number[:-21].capitalize()} {m.get_mask_account(typed_card_number[-20:])}"
    elif typed_card_number[:-17].lower() in list_of_payment_methods_names:
        return (f"{typed_card_number[:-17].split()[0].capitalize()} {typed_card_number[:-17].split()[1].capitalize()}"
                f" {m.get_mask_card_number(typed_card_number[-16:])}")
    else:
        return "Что-то пошло не так!"


def get_date(date: str) -> str:
    """Функция возвращает строку с датой в формате ДД.ММ.ГГГГ"""

    if date is not None and isinstance(date, str) and len(
            date) == 26 and f"{date[8:10]}{date[5:7]}{date[0:4]}".isdigit():
        return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
    else:
        return "Не правильный формат!"
