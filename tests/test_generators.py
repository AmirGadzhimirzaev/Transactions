import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def transaction_list():

    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_filter_by_currency(transaction_list):
    filter_by_cur = filter_by_currency(transaction_list)
    filter_by_cur_usd = filter_by_currency(transaction_list, "USD")
    filter_by_cur_rub = filter_by_currency(transaction_list, "RUB")
    filter_by_cur_with_empty_list = filter_by_currency([])
    assert next(filter_by_cur) == transaction_list[0]
    assert next(filter_by_cur) == transaction_list[1]
    assert next(filter_by_cur_usd) == transaction_list[0]
    assert next(filter_by_cur_usd) == transaction_list[1]
    assert next(filter_by_cur_rub) == transaction_list[2]
    assert filter_by_cur_with_empty_list == "Что-то пошло не так!"


def test_transaction_descriptions(transaction_list):

    trans_description = transaction_descriptions(transaction_list)
    assert next(trans_description) == "Перевод организации"
    assert next(trans_description) == "Перевод со счета на счет"
    assert next(trans_description) == "Перевод со счета на счет"
    assert next(trans_description) == "Перевод с карты на карту"
    assert next(trans_description) == "Перевод организации"
    assert next(trans_description) == "Данных больше нет!"


def test_card_number_generator():

    card_generator = card_number_generator()
    card_generator_with_parameters = card_number_generator(15, 64)
    card_generator_max_range = card_number_generator(9999999999999998, 10000000000000000)
    assert next(card_generator) == "0000 0000 0000 0000"
    assert next(card_generator) == "0000 0000 0000 0001"
    assert next(card_generator) == "Достигнут предел диапазона!"
    assert next(card_generator_with_parameters) == "0000 0000 0000 0015"
    assert next(card_generator_with_parameters) == "0000 0000 0000 0016"
    assert next(card_generator_with_parameters) == "0000 0000 0000 0017"
    assert next(card_generator_with_parameters) == "0000 0000 0000 0018"
    assert next(card_generator_max_range) == "9999 9999 9999 9998"
    assert next(card_generator_max_range) == "9999 9999 9999 9999"
    assert next(card_generator_max_range) == "Достигнут предел диапазона!"
