#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант 17. Использовать словарь, содержащий следующие ключи: название товара; название
# магазина, в котором продается товар; стоимость товара в руб. Написать программу,
# выполняющую следующие действия: ввод с клавиатуры данных в список, состоящий из
# словарей заданной структуры; записи должны быть размещены в алфавитном порядке по
# названиям
# товаров; вывод на экран информации о товаре, название которого введено с клавиатуры;
# если таких товаров нет, выдать на дисплей соответствующее сообщение.

import sys


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
        if markets.get('product') >= period:
            count += 1
            print(
                '{:>4}: {}'.format(count, markets.get('product', ''))
            )
            print('Название магазина:', markets.get('shop', ''))
            print('Стоимость в руб.:', markets.get('price', ''))

    # Если счетчик равен 0, то работники не найдены.
    if count == 0:
        print("Продукт не найден.")


def new_help():
    # Вывести справку о работе с программой.
    print("Список команд:\n")
    print("add - добавить продукт;")
    print("list - вывести список продуктов;")
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

        elif command == 'help':
            new_help()

        else:
            error()
