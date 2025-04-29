import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "typed_data, expected",
    [
        (None, "Неверный формат!"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счёт 64686473678894779589", "Счёт **9589"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Visa Gold 599941422842635311", "Неверный формат!"),
        (123345525, "Неверный формат!"),
        (123345525.12, "Неверный формат!"),
    ],
)
def test_mask_account_card(typed_data: str, expected: str):
    assert mask_account_card(typed_data) == expected


@pytest.mark.parametrize(
    "test_date, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        (None, "Неверный формат даты!"),
        (123, "Неверный формат даты!"),
        (123.3, "Неверный формат даты!"),
        ("WDMOPNWNNWCCWввdwqdqdv,.../", "Неверный формат даты!"),
    ],
)
def test_get_date(test_date: str, expected: str) -> None:
    assert get_date(test_date) == expected
