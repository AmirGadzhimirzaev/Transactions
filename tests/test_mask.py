import pytest

from src.mask import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        (None, "Номер карты не должен быть None!"),
        ("7000792289606361", "7000 79** **** 6361"),
        ("70007922896063612", "Номер карты должен содержать 16 цифр!"),
        ("700079228960636", "Номер карты должен содержать 16 цифр!"),
        ("", "Номер карты должен содержать 16 цифр!"),
        ("7AC079228960EZ61", "Номер карты должен содержать только цифры!"),
    ],
)
def test_get_card_number(card_number: str | int, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        (None, "Номер аккаунта не должен быть None!"),
        ("87564345353999334531", "**4531"),
        ("875643453539993343123", "Номер аккаунта должен содержать 20 цифр!"),
        ("8756434535399933431", "Номер аккаунта должен содержать 20 цифр!"),
        ("", "Номер аккаунта должен содержать 20 цифр!"),
        ("31212LDLF1334134DE32", "Номер аккаунта должен содержать только цифры!"),
    ],
)
def test_get_mask_account(account_number: str, expected: str) -> None:
    assert get_mask_account(account_number) == expected
