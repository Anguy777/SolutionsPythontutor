#Задача «Продажи»
#Условие
#Дана база данных о продажах некоторого интернет-магазина. Каждая строка входного файла представляет собой запись вида Покупатель товар количество, где Покупатель — имя покупателя (строка без пробелов), товар — название товара (строка без пробелов), количество — количество приобретенных единиц товара.
#Создайте список всех покупателей, а для каждого покупателя подсчитайте количество приобретенных им единиц каждого вида товаров. Список покупателей, а также список товаров для каждого покупателя нужно выводить в лексикографическом порядке.

from sys import stdin

sales_data = {}
for line in stdin.readlines():
    buyer, product, quantity = line.split()
    if buyer not in sales_data:
        sales_data[buyer] = {}
    if product not in sales_data[buyer]:
        sales_data[buyer][product] = 0
    sales_data[buyer][product] += int(quantity)
buyers = sorted(sales_data.keys())
# Выводим информацию о покупках
for buyer in buyers:
    print(buyer+':')
    # Сортируем список товаров для каждого покупателя
    products = sorted(sales_data[buyer].keys())
    for product in products:
        quantity = sales_data[buyer][product]
        print(product,quantity)

#Решение разрабов:
from collections import defaultdict
from sys import stdin

clients = defaultdict(lambda: defaultdict(int))
for line in stdin.readlines():
    client, thing, value = line.split()
    clients[client][thing] += int(value)
        
for client in sorted(clients):
    print(client + ':')
    for thing in sorted(clients[client]):
        print(thing, clients[client][thing])
