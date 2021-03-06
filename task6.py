# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь
# с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }


products = []
product_analytics = {'название': [], 'цена': [], 'количество': [], 'ед.': 'шт'}
user_answer = input('Хотите добавить товар? ')
i = 1

while user_answer.lower() == 'да':
    product_name = input('Название: ')
    product_price = int(input('Цена: '))
    product_quantity = int(input('Количество: '))
    unit = 'шт.'
    product = (i, {'название': product_name, 'цена': product_price, 'количество': product_quantity, 'ед.': unit})
    products.append(product)
    product_analytics['название'].append(product_name)
    product_analytics['цена'].append(product_price)
    product_analytics['количество'].append(product_quantity)
    i += 1
    user_answer = input('Хотите внести еще один товар? ')



print(products)

print(product_analytics)
