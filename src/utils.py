import json
import os
from typing import Generator

print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def get_json_trans_list(
    json_dir: str = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "operations.json"
    )
) -> Generator:
    """Функция принимает на вход путь до файла .json и возвращает поочереди список транзакций"""

    try:
        with open(json_dir, "r", encoding="utf-8") as f:
            data = json.load(f)
            if len(data) == 0 or type(data) is not list:
                raise Exception

    except Exception:
        yield []
    else:
        for trans in data:
            yield trans
