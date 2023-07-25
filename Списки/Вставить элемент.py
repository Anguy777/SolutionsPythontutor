a = [int(i) for i in input().split()]
a.append(0)
b = [int(i) for i in input().split()]
for i in range(len(a)-1,b[0],-1):
    a[i] = a[i-1]
a[b[0]] = b[1]
print(' '.join([str(i) for i in a]))


Решение разрабов:
a = [int(s) for s in input().split()]

# обратите внимание на множественное присваивание:
# справа от "=" стоит список из двух элементов,
# а слева -- две переменные,
# поэтому так делать можно
k, C = [int(s) for s in input().split()]

a.append(0)
for i in range(len(a) - 1, k, -1):
    a[i] = a[i - 1]
a[k] = C
print(' '.join([str(i) for i in a]))
