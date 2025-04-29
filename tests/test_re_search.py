import pytest

from src.re_search import get_data_by_category, get_data_by_str


@pytest.mark.parametrize(
    "test_list_of_dict, test_search_str, expected",
    [
        (
            [
                {"description": "Перевод организации"},
                {"description": "Перевод с карты на карту"},
                {"description": "Открытие вклада"},
                {"description": "Перевод со счета на счет"},
            ],
            "Открытие",
            [{"description": "Открытие вклада"}],
        ),
        (None, "Открытие счета", "Ошибка в get_data_by_str"),
        (123, "Открытие вклада", "Ошибка в get_data_by_str"),
        ("", "Открытие вклада", "Ошибка в get_data_by_str"),
    ],
)
def test_get_data_by_str(test_list_of_dict, test_search_str, expected):
    assert get_data_by_str(test_list_of_dict, test_search_str) == expected


@pytest.mark.parametrize(
    "test_list_of_dict, expected",
    [
        (
            [
                {"description": "Перевод организации"},
                {"description": "Перевод с карты на карту"},
                {"description": "Открытие вклада"},
                {"description": "Перевод со счета на счет"},
            ],
            {
                "Перевод организации": 1,
                "Перевод с карты на карту": 1,
                "Открытие вклада": 1,
                "Перевод со счета на счет": 1,
            },
        ),
        (None, "Ошибка в get_data_by_category"),
        (123, "Ошибка в get_data_by_category"),
        ("", "Ошибка в get_data_by_category"),
    ],
)
def test_get_data_by_category(test_list_of_dict, expected):
    assert get_data_by_category(test_list_of_dict) == expected
