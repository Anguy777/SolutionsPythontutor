#Задача «Продажи»
#Условие
#Дана база данных о продажах некоторого интернет-магазина. Каждая строка входного файла представляет собой запись вида Покупатель товар количество, где Покупатель — имя покупателя (строка без пробелов), товар — название товара (строка без пробелов), количество — количество приобретенных единиц товара.
#Создайте список всех покупателей, а для каждого покупателя подсчитайте количество приобретенных им единиц каждого вида товаров. Список покупателей, а также список товаров для каждого покупателя нужно выводить в лексикографическом порядке.

from collections import defaultdict

def calculate_heights(parents):
    heights = {}

    def dfs(node, height):
        heights[node] = height
        for child in parents[node]:
            dfs(child, height + 1)

    dfs(root, 0)  # это родоначальник

    return heights

n = int(input())  # Число элементов древа
parents = defaultdict(list)

# Чтение входных данных и заполнение словаря parents
for _ in range(n - 1):
    child, parent = input().split()
    parents[parent].append(child)
#находим родоначальника
roots = set(parents.keys())
for children in parents.values():
    roots -= set(children)
root = roots.pop()
# Вычисление высоты для каждого элемента древа
heights = calculate_heights(parents)

# Вывод элементов древа в лексикографическом порядке и их высоты
for node, height in sorted(heights.items()):
    print(node,height)

#Решение разрабов:
def height(man):
    if man not in p_tree:
        return 0
    else:
        return 1 + height(p_tree[man])

p_tree = {}
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    p_tree[child] = parent

heights = {}
for man in set(p_tree.keys()).union(set(p_tree.values())):
    heights[man] = height(man)

for key, value in sorted(heights.items()):
    print(key, value)

