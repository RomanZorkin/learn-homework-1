"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""
from typing import Any


def string_control(first_value: Any, second_value: Any) -> int:
    """The function checks the arguments whether they are strings.

    Args:
        first_value (Any): first arg for control
        second_value (Any): second arg for control

    Returns:
        int: The result of the control in the form of a conditional digit
    """
    if not isinstance(first_value, str) or not isinstance(second_value, str):
        return 0
    elif first_value == second_value:
        return 1
    else:
        if len(first_value) > len(second_value):
            return 2
        elif second_value == 'learn':
            return 3


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    control_phrase = [
        (1, 'vasy'), ('pety', 'tany'), ('pety', 'pety'),
        ('python1', 'bee'), ('bee', 'python2'), ('learn', 'python3'),
        ('python', 'learn'), ('bee', 'learn'), (1, 2),
    ]

    for first_value, second_value in control_phrase:
        print(string_control(first_value, second_value))


if __name__ == '__main__':
    main()
