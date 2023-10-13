#Задача «Частотный анализ»
#Условие
#Дан текст: в первой строке записано количество строк в тексте, а затем сами строки. Выведите все слова, встречающиеся в тексте, по одному на каждую строку. Слова должны быть отсортированы по убыванию их количества появления в тексте, а при одинаковой частоте появления — в лексикографическом порядке.
#Указание. После того, как вы создадите словарь всех слов, вам захочется отсортировать его по частоте встречаемости слова. Желаемого можно добиться, если создать список, элементами которого будут кортежи из двух элементов: частота встречаемости слова и само слово. Например, [(2, 'hi'), (1, 'what'), (3, 'is')]. Тогда стандартная сортировка будет сортировать список кортежей, при этом кортежи сравниваются по первому элементу, а если они равны — то по второму. Это почти то, что требуется в задаче.

n = int(input()) 
words = {}
for _ in range(n):
    line = input().split()
    for word in line:
        words[word] = words.get(word, 0) + 1
word_freq = [(freq, word) for word, freq in words.items()]
#до этих пор я самостоятельно нашёл такое же решение, сортировал по убыванию частоту так: sorted(value, reverse=True), но так и не понял как отсортировать по лексикографическому порядку слова.
#В итоге попросил помощи у chatGPT. 

word_freq.sort(key=lambda x: (-x[0], x[1]))
for freq, word in word_freq:
    print(word)

#Решение разрабов:
from collections import Counter

words = []
for _ in range(int(input())):
    words.extend(input().split())

counter = Counter(words)
pairs = [(-pair[1], pair[0]) for pair in counter.most_common()]
words = [pair[1] for pair in sorted(pairs)]
print('\n'.join(words))

#Альтернативное решение (была попытка такого решения, но что-то помешало и я не допёр):
dicts = {}
n = int(input())
for i in range(n):
    for j in input().split():
        dicts[j] = dicts.get(j, 0) + 1
for v in (sorted(dicts.values(), reverse=True)):
    for key, val in sorted(dicts.items()):
        if val == v:
            print(key)
