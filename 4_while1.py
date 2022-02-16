"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает
  пользователя “Как дела?”, пока он не ответит “Хорошо”

"""


def hello_user() -> None:
    """Function asks user 'Как дела?'.

    The function asks a question, until user aswer - 'Хорошо'
    """
    answer = ''
    while answer != 'Хорошо':
        answer = input('Как дела? ')


if __name__ == "__main__":
    hello_user()
