#Задача «Страны и города»
#Условие
#Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.

d = {}
for _ in range(int(input())):
    country,*cities = input().split()
    d[country]= set(cities)
for _ in range(int(input())):
    for city in input().split():
        for k,v in d.items():
            if city in (v):
                print(k)

#Решение разрабов:
motherland = {}
for i in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        motherland[city] = country
        
for i in range(int(input())):
    print(motherland[input()])
