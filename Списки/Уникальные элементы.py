a = [int(i) for i in input().split()]
for i in range(len(a)):
    if a[i] in a[i+1:len(a)] or a[i] in a[:i]:
        continue
    else:
        print(a[i],end=' ')
# мой код быстрее чем у разраба ( ͡° ͜ʖ ͡°) 

# Решение разрабов:
a = [int(s) for s in input().split()]
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i], end=' ')
