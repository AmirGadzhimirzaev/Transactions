import pytest

from src.processing import filter_by_state, sorted_by_state


@pytest.fixture
def test_list_of_dict() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def test_list_of_dict_with_same_date() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.mark.parametrize(
    "state_argument, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            ],
        ),
        ("", "Возникла ошибка!"),
        (None, "Возникла ошибка!"),
        (123445, "Возникла ошибка!"),
    ],
)
def test_filter_by_state(test_list_of_dict: list[dict], state_argument: str, expected: str) -> None:
    assert filter_by_state(test_list_of_dict, state_argument) == expected


def test_filter_by_no_state(test_list_of_dict: list[dict]) -> None:
    assert filter_by_state(test_list_of_dict) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.mark.parametrize(
    "state, expected",
    [
        (
            True,
            [
                {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
                {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
                {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
                {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
            ],
        ),
        (
            False,
            [
                {"date": "2018-06-30T02:08:58.425572", "id": 939719570, "state": "EXECUTED"},
                {"date": "2018-09-12T21:27:25.241689", "id": 594226727, "state": "CANCELED"},
                {"date": "2018-10-14T08:21:33.419441", "id": 615064591, "state": "CANCELED"},
                {"date": "2019-07-03T18:35:29.512364", "id": 41428829, "state": "EXECUTED"},
            ],
        ),
        ("", "Что-то пошло не так!"),
        (None, "Что-то пошло не так!"),
        ([], "Что-то пошло не так!"),
    ],
)
def test_sorted_by_state(test_list_of_dict: list[dict], state: bool, expected: str) -> None:
    assert sorted_by_state(test_list_of_dict, state) == expected


def test_sorted_by_state_with_same_date(test_list_of_dict_with_same_date: list[dict]) -> None:
    assert sorted_by_state(test_list_of_dict_with_same_date) == test_list_of_dict_with_same_date
