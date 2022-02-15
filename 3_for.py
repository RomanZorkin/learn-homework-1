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
from glom import glom

def summ_for_each(sales_information):
    for phone in sales_information:
        print(sum(phone['items_sold']))

def average_for_each(sales_information):
    for phone in sales_information:
        print(
            sum(phone['items_sold'])/len(phone['items_sold'])
        )

def summ_for_all(sales_information):
    new_dict = {'target': sales_information}
    result = glom(new_dict, ('target', ['items_sold'], sum))
    print(result)

def average_for_all(sales_information):
    pass

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

    summ_for_each(sales_information)
    print(average_for_each(sales_information))
    print(summ_for_all(sales_information))
    print(average_for_all(sales_information))

if __name__ == "__main__":
    main()
