#Задача «Ферзи»

#Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
#Программа получает на вход восемь пар чисел, каждое число от 1 до 8 — координаты 8 ферзей. Если ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

X = []
Y = []
q = 0
n = 8
for i in range(n):
    x,y = [int(i) for i in input().split()]
    X.append(x)
    Y.append(y)
for i in range(n):
    for j in range(i+1,n):
        if i != j and (abs(X[i] - X[j]) == abs(Y[i] - Y[j]) or X[i] == X[j] or Y[i] == Y[j]):
            q = 1
            break
if q == 1:
    print('YES')
else:
    print('NO')
    
