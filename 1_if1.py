"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь:
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
from glom import glom

age_limit = {
    'kindergarten': {
        'age': 7, 'text': 'Вы ходите в детский садик',
    },
    'school': {
        'age': 18, 'text': 'Вы учитесь в школе',
    },
    'college': {
        'age': 25, 'text': 'Вы учитесь в ВУЗе',
    },
    'work': {
        'age': 65, 'text': 'Вы работаете',
    },
    'pension': {
        'text': 'Вы пенсионер - поздравляю у вас все только начинается!',
    },
}


def age_profession(age: int) -> str:
    """Function for determining a person's occupation.

    Args:
        age (int): age of a person

    Returns:
        str: occupation of a person
    """
    if age < glom(age_limit, 'kindergarten.age'):
        return glom(age_limit, 'kindergarten.text')
    elif age < glom(age_limit, 'school.age'):
        return glom(age_limit, 'school.text')
    elif age < glom(age_limit, 'college.age'):
        return glom(age_limit, 'college.text')
    elif age < glom(age_limit, 'work.age'):
        return glom(age_limit, 'work.text')
    return glom(age_limit, 'pension.text')


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age = input('Здравствуйте, введи пожалуйста свой возраст ')
    profession = age_profession(int(age))
    print(profession)


if __name__ == '__main__':
    main()
