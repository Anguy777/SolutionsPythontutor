#Задача «Самое частое слово»
#Условие
#Дан текст: в первой строке задано число строк, далее идут сами строки. Выведите слово, которое в этом тексте встречается чаще всего. Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
words = {}
for i in range(int(input())):
    for word in input().split():
        words[word] = words.get(word, 0) + 1
Max = max(words.values())
for key in sorted(words):
    if words[key] == Max:
        Max = key
print(Max)

#Решение разрабов:
counter = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        counter[word] = counter.get(word, 0) + 1
        
max_count = max(counter.values())
most_frequent = [k for k, v in counter.items() if v == max_count]
print(min(most_frequent))
