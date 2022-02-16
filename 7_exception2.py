"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.

"""
from typing import Any


def discounted(price: Any, discount: Any, max_discount: Any = 20) -> float:
    """The function calculates the cost taking into account the discount.

    Args:
        price (Any): phone price
        discount (Any): current discount
        max_discount (Any): max discount for phone

    Raises:
        ValueError: Always.
        TypeError: Always.

    Returns:
        float: finish price with discount
    """
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
    except (ValueError, TypeError):
        print('Введены некорректные данные')
        return None

    if max_discount >= 100:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount:
        return price
    return price - (price * discount / 100)


if __name__ == '__main__':
    print(discounted(100, 2))
    print(discounted(100, '3'))
    print(discounted('100', '4.5'))
    print(discounted('five', 5))
    print(discounted('сто', 'десять'))
    print(discounted(100.0, 5, '10'))
