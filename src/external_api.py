import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("APILayer_KEY")


def get_convert(trans_data: dict) -> str:
    """Функция принимает на вход транзакцию и возвращает сумму транзакций в RUB"""

    trans_amount = trans_data["operationAmount"]["amount"]
    trans_currency_code = trans_data["operationAmount"]["currency"]["code"]

    if trans_currency_code != "RUB":
        url = (
            f"https://api.apilayer.com/exchangerates_data/convert?"
            f"to=RUB&from={trans_currency_code}&amount={trans_amount}"
        )
        headers = {"apikey": f"{API_KEY}"}
        response = requests.get(url, headers)
        return f"{response.json()['result']:.2f}"

    return trans_amount
