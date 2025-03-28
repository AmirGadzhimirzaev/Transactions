import pandas as pd
import os


def csv_reader(
        csv_file_path: str = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "transactions.csv")):
    """ Функция для считывания финансовых операций из csv-файла, выдает список словарей с транзакциями """

    try:
        reader = pd.read_csv(csv_file_path, delimiter=';')

        data = []

        for x in range(reader.shape[0]):
            data.append(reader.iloc[x, :].to_dict())

        return data

    except Exception:
        return []


def xlsx_reader(xlsx_file_path: str = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data",
                                                   "transactions_excel.xlsx")):
    """ Функция для считывания финансовых операций из Excel, выдает список словарей с транзакциями """

    try:
        reader = pd.read_excel(xlsx_file_path)
        data = []

        for x in range(reader.shape[0]):
            data.append(reader.iloc[x, :].to_dict())

        return data

    except Exception:
        return []
