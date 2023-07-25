a = [int(i) for i in input().split()]
count = 0
for i in range(len(a)):
    for k in range(i+1,len(a)):
        if a[i] == a[k]:
            count += 1
print(count)
