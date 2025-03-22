from unittest.mock import patch

from src.external_api import get_convert


@patch("requests.get")
def test_get_convert(mock_get):
    mock_get.return_value.json.return_value = {
        "success": True,
        "query": {"from": "USD", "to": "RUB", "amount": 9824.07},
        "info": {"timestamp": 1742204651, "rate": 85.499741},
        "date": "2025-03-17",
        "result": 839955.440566,
    }
    assert get_convert({"operationAmount": {"amount": "1000", "currency": {"code": "USD"}}}) == "839955.44"
    mock_get.assert_called_once()
