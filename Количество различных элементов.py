a = [int(i) for i in input().split()]
k = 0
for i in range(1,len(a)):
    if a[i-1] == a[i]:
        k += 1
print(len(a)-k)
