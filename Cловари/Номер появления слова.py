#Задача «Номер появления слова»
#Условие
#В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в этом тексте ранее.
#Словом считается последовательность непробельных символов идущих подряд, слова разделены одним или большим числом пробелов или символами конца строки.

text = [str(i) for i in input().split()]
count = 0
j = 0
a = []
for word in text:
    for i in range(j):
        if word == text[i]:
            count += 1
        else:
            continue
    a.append(count)
    count = 0
    j += 1
print(' '.join([str(i) for i in a]))

counter = {}
for word in input().split():
    counter[word] = counter.get(word, 0) + 1
    print(counter[word] - 1, end=' ')
