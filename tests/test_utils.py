from src.utils import get_json_trans_list


def test_get_json_trans_list():
    not_exist_file = get_json_trans_list("file.json")
    not_str_filename = get_json_trans_list("31221")
    normal_exec = get_json_trans_list()

    assert next(not_exist_file) == []
    assert next(not_str_filename) == []
    assert next(normal_exec) == {'date': '2019-08-26T10:50:58.294041',
                                 'description': 'Перевод организации',
                                 'from': 'Maestro 1596837868705199',
                                 'id': 441945886,
                                 'operationAmount': {'amount': '31957.58',
                                                     'currency': {'code': 'RUB', 'name': 'руб.'}},
                                 'state': 'EXECUTED',
                                 'to': 'Счет 64686473678894779589'}
