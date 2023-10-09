#Задача «Угадай число»
#Условие
#Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n. Беатриса пытается угадать это число, для этого она называет некоторые множества натуральных чисел. Август отвечает Беатрисе YES, если среди названных ей чисел есть задуманное или NO в противном случае. После нескольких заданныъх вопросов Беатриса запуталась в том, какие вопросы она задавала и какие ответы получила и просит вас помочь ей определить, какие числа мог задумать Август.

#В первой строке задано n - максимальное число, которое мог загадать Август. Далее каждая строка содержит вопрос Беатрисы (множество чисел, разделенных пробелом) и ответ Августа на этот вопрос.

#Вы должны вывести через пробел, в порядке возрастания, все числа, которые мог задумать Август.
  
B = set()
A = set(range(1, int(input()) + 1))
while 'HELP' not in B:
    try:
        B = [int(i) for i in input().split()]
        if  str(input()) == 'YES':
            A.intersection_update(B)
        else:
            A.difference_update(B)
    except:
        break
print(*[int(item) for item in sorted(A)])
    

#Решение разработчиков:
n = int(input())
all_nums = set(range(1, n + 1))
possible_nums = all_nums
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(x) for x in guess.split()}
    answer = input()
    if answer == 'YES':
        possible_nums &= guess
    else:
        possible_nums &= all_nums - guess

print(' '.join([str(x) for x in sorted(possible_nums)]))
