a = [int(i) for i in input().split()]
s = []
if len(a) % 2 == 0:
    for i in range(0,len(a),2):
        a[i],a[i+1] =a[i+1],a[i]
else:
    for i in range(0,len(a)-1,2):
        a[i],a[i+1] =a[i+1],a[i]
print(' '.join([str(i) for i in a]))
        
Dev solution:
a = [int(i) for i in input().split()]
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))
