"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
from typing import List

from glom import Iter, glom


def summ_for_each(sales_information: List) -> None:
    """Function for determining the total number of sales for each product.

    Args:
        sales_information (List): list with condition
    """
    for phone in sales_information:
        print(
            'Cуммарное количество продаж для "{0}" = {1}'.format(
                phone['product'],
                sum(phone['items_sold']),
            ),
        )


def average_for_each(sales_information: List) -> None:
    """A function to determine the average number of sales for each product.

    Args:
        sales_information (List): list with condition
    """
    for phone in sales_information:
        print(
            'Cреднее количество продаж для "{0}" = {1}'.format(
                phone['product'],
                round(
                    sum(phone['items_sold']) / len(phone['items_sold']),
                    2,
                ),
            ),
        )


def summ_for_all(sales_information: List) -> List:
    """The function generates a list with sales figures for all products.

    The function generates a single list with sales figures
    from the lists for each product

    Args:
        sales_information (List): list with condition

    Returns:
        List: single list with sales figures
    """
    my_dict = {'phones': sales_information}
    glom_obj = glom(my_dict, ('phones', ['items_sold']))
    return list(glom(glom_obj, Iter().flatten()))


def sales_for_all(sales_information: List) -> None:
    """Function for determining sales figures for all products.

    The function informs about the total and average number
    of sales of all products

    Args:
        sales_information (List): list with condition
    """
    sold_list = summ_for_all(sales_information)
    print('Cуммарное количество продаж всех товаров {summ_sales}'.format(
        summ_sales=sum(sold_list),
    ))
    print(
        'Среднее количество продаж всех товаров {average}'.format(
            average=sum(sold_list) / len(sold_list),
        ),
    )

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    sales_information = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]
    function_list = [
        summ_for_each,
        average_for_each,
        sales_for_all,
    ]

    for my_fun in function_list:
        my_fun(sales_information)


if __name__ == '__main__':
    main()
