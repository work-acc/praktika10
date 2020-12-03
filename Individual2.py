#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Из лабораторной работы 8 необходимо дополнительно
# реализовать сохранение и чтение данных из файла формата JSON.
# Необходимо проследить за тем, чтобы файлы генерируемый этой
# программой не попадали в репозиторий лабораторной работы.

import sys
import json


def new_add():
    # Запросить данные о товаре.
    product = input("Название товара? ")
    shop = input("Название магазина? ")
    price = int(input("Стоимость товара в руб.? "))

    # Создать словарь.
    markets = {
        'product': product,
        'shop': shop,
        'price': price,
    }

    # Добавить словарь в список.
    market.append(markets)
    # Отсортировать список в случае необходимости.
    if len(market) > 1:
        market.sort(key=lambda item: item.get('name', ''))


def new_list():
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 20
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
            "No",
            "Товар",
            "Магазин",
            "Стоимость в руб."
        )
    )
    print(line)

    # Вывести данные о всех товарах.
    for idx, markets in enumerate(market, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                idx,
                markets.get('product', ''),
                markets.get('shop', ''),
                markets.get('price', 0)
            )
        )

    print(line)


def new_select():
    parts = command.split(' ', maxsplit=2)

    period = str(parts[1])

    # Инициализировать счетчик.
    count = 0
    # Проверить сведения товара из списка.
    for markets in market:
        if markets.get('shop') >= period:
            count += 1
            print(
                '{:>4}: {}'.format(count, markets.get('shop', ''))
            )
            print('Название товара:', markets.get('product', ''))
            print('Стоимость в руб.:', markets.get('price', ''))

    # Если счетчик равен 0, то работники не найдены.
    if count == 0:
        print("Магазин не найден.")


def new_load():
    # Разбить команду на части для выделения имени файла.
    parts = command.split(' ', maxsplit=1)

    # Прочитать данные из файла JSON.
    with open(parts[1], 'r') as f:
        market = json.load(f)
        return market


def new_save():
    # Разбить команду на части для выделения имени файла.
    parts = command.split(' ', maxsplit=1)

    # Сохранить данные в файл JSON.
    with open(parts[1], 'w') as f:
        json.dump(market, f)


def new_help():
    # Вывести справку о работе с программой.
    print("Список команд:\n")
    print("add - добавить продукт;")
    print("list - вывести список продуктов;")
    print("load <имя файла> - загрузить данные из файла;")
    print("save <имя файла> - сохранить данные в файл;")
    print("select <товар> - информация о товаре;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")


def error():
    print(f"Неизвестная команда {command}", file=sys.stderr)


if __name__ == '__main__':
    # Список работников.
    market = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            new_add()

        elif command == 'list':
            new_list()

        elif command.startswith('select '):
            new_select()

        elif command.startswith('load '):
            new_load()

        elif command.startswith('save '):
            new_save()

        elif command == 'help':
            new_help()

        else:
            error()
