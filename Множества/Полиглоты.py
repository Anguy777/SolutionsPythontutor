#Задача «Полиглоты»
#Условие
#Каждый из некоторого множества школьников некоторой школы знает некоторое количество языков. Нужно определить сколько языков знают все школьники, и сколько языков знает хотя бы один из школьников.
#В первой строке задано количество школьников. Для каждого из школьников сперва записано количество языков, которое он знает, а затем - названия языков, по одному в строке.
#В первой строке выведите количество языков, которые знают все школьники. Начиная со второй строки - список таких языков. Затем - количество языков, которые знает хотя бы один школьник, на следующих строках - список таких языков. Языки нужно выводить в лексикографическом порядке, по одному на строке.
n = int(input())
pupils = set(range(1,n+1))
lang = set()
langAll = lang
langOne = set()
for k in range(n):
    m = int(input())
    for i in range(m):
        lang.add(str(input()))
    langAll &= lang
    langOne |= lang
    lang = set()
print(len(langAll))
print('\n'.join(sorted(langAll)))
print(len(langOne))
print('\n'.join(sorted(langOne)))

#Решение разрабов:
students = [{input() for j in range(int(input()))} for i in range(int(input()))]
known_by_everyone, known_by_someone = set.intersection(*students), set.union(*students)
print(len(known_by_everyone), *sorted(known_by_everyone), sep='\n')
print(len(known_by_someone), *sorted(known_by_someone), sep='\n')
