import json
import logging
import os

utils_log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", "utils_logger.log")

utils_logger = logging.getLogger("utils_logger")
utils_file_handler = logging.FileHandler(utils_log_path)
utils_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
utils_file_handler.setFormatter(utils_formatter)
utils_logger.addHandler(utils_file_handler)
utils_logger.setLevel(logging.DEBUG)


def get_json_trans_list(
    json_dir: str = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "operations.json"
    )
) -> list[dict]:
    """Функция принимает на вход путь до файла .json и возвращает поочереди список транзакций"""

    try:
        with open(json_dir, "r", encoding="utf-8") as f:
            data = json.load(f)
            if len(data) == 0 or type(data) is not list:
                raise Exception("Пустой файл или неверный путь")

    except Exception as ex:
        utils_logger.error(f"ERROR: {ex}")

        return []
    else:
        utils_logger.debug("DEBUG: success")

        return data
