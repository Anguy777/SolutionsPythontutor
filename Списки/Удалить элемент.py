a = [int(i) for i in input().split()]
k = int(input())
for i in range(k,len(a)-1):
    a[i] = a[i+1]
a.pop()
print(' '.join([str(i) for i in a]))
