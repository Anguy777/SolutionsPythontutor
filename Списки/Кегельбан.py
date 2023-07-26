n,k = [int(i) for i in input().split()]
N = ['I'] * n
for i in range(k):
    l,r = [int(i) for i in input().split()]
    for j in range(l-1,r):
        N[j] = '.'
print(''.join(N))        


#моё изначальное решение:
n,k = [int(i) for i in input().split()]
N = []
for i in range(n):
    N.append('I')
count = 1
while count <= k:
    count += 1
    l,r = [int(i) for i in input().split()]
    for j in range(l-1,r):
        N[j] = '.'
print(''.join(N))   
