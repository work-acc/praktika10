#!/usr/bin/evn python3
# -*- config: utf-8 -*-


def score():
    while True:
        a = int(input("a = "))
        b = int(input("b = "))

        if a == 0 or b == 0:
            break

        s = a * b
        print(s)


if __name__ == '__main__':
    score()
