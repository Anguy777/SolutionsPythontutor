#Задача «Длина отрезка»

#Даны четыре действительных числа: x1, y1, x2, y2. Напишите функцию distance(x1, y1, x2, y2), вычисляющая расстояние между точкой (x1,y1) и (x2,y2). Считайте четыре действительных числа и выведите результат работы этой функции.
#Если вы не знаете, как решить эту задачу, то вы, возможно, не изучали в школе теорему Пифагора. Попробуйте прочитать о ней на Википедии.

args = [float(input()) for x in range(4)]

def distance(x1, y1, x2, y2):
    from math import sqrt
    return(sqrt((x2-x1)**2 + (y2-y1)**2))

print(distance(*args))

#Решение разрабов:
from math import sqrt

def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(distance(x1, y1, x2, y2))
