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


def new_add(market, product, shop, price):
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


def new_list(market):
    table = []
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 20
    )
    table.append(line)
    table.append(
        '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
            "No",
            "Товар",
            "Магазин",
            "Стоимость в руб."
        )
    )
    table.append(line)

    # Вывести данные о всех товарах.
    for idx, markets in enumerate(market, 1):
        table.append(
            '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                idx,
                markets.get('product', ''),
                markets.get('shop', ''),
                markets.get('price', 0)
            )
        )

    table.append(line)

    return '\n'.join(table)


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


if __name__ == '__main__':
    # Список товаров.
    market = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            product = input("Название товара? ")
            shop = input("Название магазина? ")
            price = int(input("Стоимость товара в руб.? "))

            new_add(market, product, shop, price)

        elif command == 'list':
            print(list(market))

        elif command.startswith('select '):
            new_select()

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить продукт;")
            print("list - вывести список продуктов;")
            print("select <товар> - информация о товаре;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
