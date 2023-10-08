#Задача «Встречалось ли число раньше»
#Условие
#Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в #последовательности или NO, если не встречалось.
A = [int(s) for s in input().split()]
i = 0
for num in A:
    if num in set(A[0:i]):
        print('YES')
    else:
        print('NO')
    i += 1

#Решение разрабов:
  numbers = [int(s) for s in input().split()]
occur_before = set()
for num in numbers:
    if num in occur_before:
        print('YES')
    else:
        print('NO')
        occur_before.add(num)
