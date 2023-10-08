#Задача «Кубики»
#Условие
#Аня и Боря любят играть в разноцветные кубики, причем у каждого из них свой набор и в каждом наборе все кубики различны по цвету. Однажды дети заинтересовались, сколько #существуют цветов таких, что кубики каждого цвета присутствуют в обоих наборах. Для этого они занумеровали все цвета случайными числами от 0 до 108. На этом их энтузиазм #иссяк, поэтому вам предлагается помочь им в оставшейся части.

#В первой строке входных данных записаны числа N и M — число кубиков у Ани и Бори. В следующих N строках заданы номера цветов кубиков Ани. В последних M строках номера цветов #Бори.

#Найдите три множества: номера цветов кубиков, которые есть в обоих наборах; номера цветов кубиков, которые есть только у Ани и номера цветов кубиков, которые есть только у #Бори. Для каждого из множеств выведите сначала количество элементов в нем, а затем сами элементы, отсортированные по возрастанию.

N,M = [int(i) for i in input().split()]
A,B = set(),set()
for i in range(N):
    A.add(int(input()))
for i in range(M):
    B.add(int(input()))
print(len(sorted(set(A) & set(B))))
print(*[str(i) for i in sorted(set(A) & set(B))])
print(len(sorted(set(A) - set(B))))
print(*[str(i) for i in sorted(set(A) - set(B))])
print(len(sorted(set(B) - set(A))))
print(*[str(i) for i in sorted(set(B) - set(A))])

#Решение разрабов:
def print_set(some_set):
    print(len(some_set))
    print(*[str(item) for item in sorted(some_set)])

N, M = [int(s) for s in input().split()]
A_colors, B_colors = set(), set()
for i in range(N):
    A_colors.add(int(input()))
for i in range(M):
    B_colors.add(int(input()))
    
print_set(A_colors & B_colors)
print_set(A_colors - B_colors)
print_set(B_colors - A_colors)
