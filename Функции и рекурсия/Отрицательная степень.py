#Задача «Отрицательная степень»
#Дано действительное положительное число a и целоe число n.
#Вычислите an. Решение оформите в виде функции power(a, n).
#Стандартной функцией возведения в степень пользоваться нельзя.

a = float(input())
n = int(input())
def power(a,n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return(res)
    else:
        return(1/res)
        
print(power(a,n))
