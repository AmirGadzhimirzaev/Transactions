import logging
import os

mask_log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "mask_logger.log")

mask_logger = logging.getLogger("mask_logger")
mask_file_handler = logging.FileHandler(mask_log_path)
mask_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
mask_file_handler.setFormatter(mask_formatter)
mask_logger.addHandler(mask_file_handler)
mask_logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: int | str) -> str:
    """Функция возвращает маску номера по правилу XXXX XX** **** XXXX"""

    texted_number = str(card_number)

    try:
        mask_logger.debug("DEBUG: success")

        if card_number is None:
            return "Номер карты не должен быть None!"
        elif len(texted_number) != 16:
            return "Номер карты должен содержать 16 цифр!"
        elif not texted_number.isdigit():
            return "Номер карты должен содержать только цифры!"
        else:
            return f"{texted_number[:4]} {texted_number[4:6]}** **** {texted_number[-4:]}"

    except Exception as ex:
        mask_logger.error(f"ERROR: {ex}")

        return "Что то пошло не так"


def get_mask_account(account_number: int | str) -> str:
    """Функция возвращает маску номера по правилу **XXXX"""

    str_account_number = str(account_number)

    try:
        mask_logger.debug("DEBUG: success")

        if account_number is None:
            return "Номер аккаунта не должен быть None!"
        elif len(str_account_number) != 20:
            return "Номер аккаунта должен содержать 20 цифр!"
        elif not str_account_number.isdigit():
            return "Номер аккаунта должен содержать только цифры!"
        else:
            return f"**{str_account_number[-4:]}"

    except Exception as ex:
        mask_logger.error(f"ERROR: {ex}")

        return "Что то пошло не так"
