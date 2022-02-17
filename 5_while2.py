"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую

"""
# As far as I know in python 3.10 it is possible to define
# types (list, dict) without importing typing module.
# But it`s a good idea for backward compatibility

questions_and_answers = {'Как дела': 'Хорошо!', 'Что делаешь?': 'Программирую'}


def ask_user(answers_dict: dict) -> None:
    """The function generates an answer to the given question.

    Args:
        answers_dict (dict): rule with pairs - question -> answer
    """
    question = ''
    while question != 'exit':
        question = input('Задайте мне вопрос - ')
        if answers_dict.get(question):
            print(answers_dict[question])
        else:
            print('Вашего вопроса нет в списке.')


if __name__ == '__main__':
    ask_user(questions_and_answers)
