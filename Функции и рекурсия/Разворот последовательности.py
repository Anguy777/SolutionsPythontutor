#Задача «Разворот последовательности»
#Дана последовательность целых чисел, заканчивающаяся числом 0. Выведите эту последовательность в обратном порядке.
#При решении этой задачи нельзя пользоваться массивами и прочими динамическими структурами данных. Рекурсия вам поможет.

def reverse():
    x = int(input())
    if x != 0:
        reverse()
    print(x)

reverse()
