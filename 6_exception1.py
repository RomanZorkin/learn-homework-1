"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""


def hello_user() -> None:
    """Function asks user 'Как дела?'.

    The function asks a question, until user aswer - 'Хорошо'
    or the buttons 'Ctrl+ C' are pressed.
    """
    answer = ''
    while answer != 'Хорошо':
        try:
            answer = input('Как дела? ')
        except KeyboardInterrupt:
            print('Пока')
            break


if __name__ == "__main__":
    hello_user()
