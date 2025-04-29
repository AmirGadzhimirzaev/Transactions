from src.format_reader import csv_reader, xlsx_reader
from src.processing import filter_by_state, sort_by_date
from src.re_search import get_data_by_str
from src.utils import get_json_trans_list
from src.widget import get_date, mask_account_card

FILE_TYPES = ["JSON", "CSV", "XLSX"]
STATUS_TYPES = ["EXECUTED", "CANCELED", "PENDING"]

prog_text_dict = {
    "Привет! Добро пожаловать в программу работы с банковскими транзакциями.": "",
    "Выберите необходимый пункт меню:\n"
    f"1. Получить информацию о транзакциях из {FILE_TYPES[0]}-файла\n"
    f"2. Получить информацию о транзакциях из {FILE_TYPES[1]}-файла\n"
    f"3. Получить информацию о транзакциях из {FILE_TYPES[2]}-файла": ["1", "2", "3"],
    "Введите статус, по которому необходимо выполнить фильтрацию.\n"
    "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING": ["EXECUTED", "CANCELED", "PENDING"],
    "Отсортировать операции по дате? Да/Нет": ["да", "нет"],
    "Отсортировать по возрастанию или по убыванию?": ["по убыванию", "по возрастанию"],
    "Выводить только рублевые транзакции? Да/Нет": ["да", "нет"],
    "Отфильтровать список транзакций по определенному слову в описании? Да/Нет": ["да", "нет"],
    "Распечатываю итоговый список транзакций...": "",
    "Всего банковских операций в выборке: ": "",
}

user_text_dict = {
    "user_1": "Для обработки выбран *-файл.",
    "user_2": "Операции отфильтрованы по статусу *",
    "user_3": "Введите слово",
}

warning_test_dict = {
    "warning_1": "Выбран неверный пункт меню",
    "warning_2": "Статус операции * недоступен",
    "warning_3": "Неверный ввод",
    "warning_4": "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации",
}


def main():
    user_answers = []

    for key, value in prog_text_dict.items():

        while key:

            if "Отсортировать по возрастанию или по убыванию?" in key and user_answers[-1] is False:
                user_answers.append(False)
                break

            if "Отфильтровать список транзакций по определенному слову в описании? Да/Нет" in key:
                print(key)
                user_ans = input().lower()
                if user_ans in "да":
                    user_answers.append(True)
                    user_answers.append(input(user_text_dict["user_3"] + "\n").lower())
                    break
                elif user_ans in "нет":
                    user_answers.append(False)
                    break
                else:
                    print(warning_test_dict["warning_3"])
                    continue

            if "Всего банковских операций в выборке: " in key:
                print(key, end="")
            else:
                print(key)

            if value:
                user_ans = input()
                user_ans = (
                    user_ans.lower()
                    if user_ans.lower() in ["да", "по убыванию", "нет", "по возрастанию"]
                    else user_ans.upper()
                )

                if user_ans in value:
                    if user_ans in ["да", "по убыванию"]:
                        user_answers.append(True)
                        break
                    elif user_ans in ["EXECUTED", "CANCELED", "PENDING"]:
                        print(user_text_dict["user_2"].replace("*", f'"{user_ans}"'))
                        user_answers.append(user_ans)
                        break
                    elif user_ans in ["1", "2", "3"]:
                        print(user_text_dict["user_1"].replace("*", f"{FILE_TYPES[int(user_ans) - 1]}"))
                        user_answers.append(int(user_ans) - 1)
                        break
                    else:
                        user_answers.append(False)
                        break
                else:
                    if "Выберите необходимый пункт меню" in key:
                        print(warning_test_dict["warning_1"])
                    elif "Введите статус" in key:
                        print(warning_test_dict["warning_2"].replace("*", f'"{user_ans}"'))
                    else:
                        print(warning_test_dict["warning_3"])
                    continue
            else:
                break

    # Выбор типа файла для обработчика JSON[0], CSV[1], XLSX[2]
    choose_file = [get_json_trans_list, csv_reader, xlsx_reader]

    first_file_type = choose_file[user_answers[0]]()

    second_filter_by_state = filter_by_state(first_file_type, user_answers[1])

    if user_answers[2] is True and len(second_filter_by_state) > 0:
        third_filter_by_date = sort_by_date(second_filter_by_state, user_answers[3])
    else:
        third_filter_by_date = second_filter_by_state

    if user_answers[4] is True and len(third_filter_by_date) > 0:
        fourth_only_rub_trans = [x for x in third_filter_by_date if x["operationAmount"]["currency"]["code"] == "RUB"]
    else:
        fourth_only_rub_trans = third_filter_by_date

    if user_answers[5] is True and len(fourth_only_rub_trans) > 0:
        fifth_sort_by_word = get_data_by_str(fourth_only_rub_trans, user_answers[6])
    else:
        fifth_sort_by_word = fourth_only_rub_trans

    print(len(fifth_sort_by_word))

    if len(fifth_sort_by_word) <= 0:
        print(warning_test_dict["warning_4"])

    for ans in fifth_sort_by_word:
        # Номера и названия аккаунтов
        from_account, to_account = map(mask_account_card, (ans.get("from", ""), ans.get("to", "")))

        # Только счет при открытии в остальных случаях 'from' -> 'to'
        new_account_info = f"{to_account}" if from_account == "" else f"{from_account} -> {to_account}"

        # Описание операции 'description'
        operation_description = ans["description"]

        # Преобразование даты в формат дд.мм.гггг 'date'
        data_pattern = get_date(ans["date"])

        # Сумма 'amount' и наименование валюты 'name'
        operation_int = ans["operationAmount"]["amount"]
        operation_name = ans["operationAmount"]["currency"]["name"]

        final_answer = (
            f"{data_pattern} {operation_description}\n"
            f"{new_account_info}\n"
            f"Сумма: {operation_int} {operation_name}\n"
        )
        print(final_answer)


if __name__ == "__main__":
    main()
