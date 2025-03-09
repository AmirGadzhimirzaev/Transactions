# Проект *"Виджет для банковских операций"*

## Описание:

Проект *"Виджет для банковских операций"* - это набор модулей и пакетов для работы
с персональными данными клиентов банка.

## Где найти:

Репозиторий с проектом находится по адресу [Github/Transaction](https://github.com/AmirGadzhimirzaev/Transactions.git)

## Что внутри:

### Модули:

1. **[mask.py](src/mask.py)** - маскирует номер карты/аккаунта клиента
2. **[widget.py](src/widget.py)** - маскировка с проверкой входных данных и преобразование формата даты
3. **[processing.py](src/processing.py)** - фильтрует и сортирует данные о транзакциях
4. **[generators.py](src/generators.py)** - генерирует данные о транзакциях и номера карт
5. **[decorators.py](src/decorators.py)** - модуль содержащий декораторы: логирование

## Тесты:

1. Все функции в папке **src** протестированы
2. Модули тестов в папке **tests**
3. Отчет о тестировании: [tests_report](http://localhost:63342/Transactions/htmlcov/index.html?_ijt=h7glan3dd8im6u77lg6s4fu07&_ij_reload=RELOAD_ON_SAVE)