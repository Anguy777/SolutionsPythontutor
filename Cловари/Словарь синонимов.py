#Задача «Словарь синонимов»
#Условие
#Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.
#Для слова из словаря, записанного в последней строке, определите его синоним.

A = {}
for i in range(int(input())):
    key,val=[str(i) for i in input().split()]
    A[key] = val
x = str(input())
for key,val in A.items():
    if x == key:
        print(val)
    elif x == val:
        print(key)
    else:
        continue

#Решение разрабов:
  n = int(input())
d = {}
for i in range(n):
    first, second = input().split()
    d[first] = second
    d[second] = first
print(d[input()])
