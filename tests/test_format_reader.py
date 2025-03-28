from unittest.mock import patch

import pandas as pd

from src.format_reader import csv_reader, xlsx_reader


@patch("pandas.read_csv")
def test_csv_reader_mocked(mock_read_csv):
    mock_df = pd.DataFrame({"col_1": [1, 2]})
    mock_read_csv.return_value = mock_df

    assert csv_reader()
    mock_read_csv.assert_called_once()


@patch("pandas.read_excel")
def test_xlsx_reader_mocked(mock_read_xlsx):
    mock_df = pd.DataFrame({"col_1": [1, 2]})
    mock_read_xlsx.return_value = mock_df

    assert xlsx_reader()
    mock_read_xlsx.assert_called_once()


def test_csv_xlsx_reader():
    assert csv_reader('') == []
    assert xlsx_reader('') == []
    assert csv_reader(123) == []
    assert xlsx_reader(123) == []