#Задача «Большие буквы»
#Напишите функцию capitalize(), которая принимает слово из маленьких латинских букв и возвращает его же, меняя первую букву на большую.
#Например, print(capitalize('word')) должно печатать слово Word.
#На вход подаётся строка, состоящая из слов, разделённых одним пробелом. Слова состоят из маленьких латинских букв. Напечатайте исходную строку, сделав так, чтобы каждое слово начиналось с большой буквы. При этом используйте вашу функцию capitalize().
#Напомним, что в Питоне есть функция ord(), которая по символу возвращает его код в таблице ASCII, и функция chr(), которая по коду символа возвращает сам символ. Например, ord('a') == 97, chr(97) == 'a'.

s = input()
def capitalize(s):
    x = 0
    s1 = ('')
    for i in range(s.count(' ')+1):
        y = s.find(' ',x)+1
        if y > 0:
            l = s[x:y].replace(s[x],chr(ord(s[x])-32),1)
            s1 += l
            x = s.find(' ',x) + 1
        else:
            l = s[x:].replace(s[x],chr(ord(s[x])-32),1)
            s1 =s1 + l
    return s1
print(capitalize(s))

#Решение разрабов:
def capitalize(word):
    first_letter_small = word[0]
    first_letter_big = chr(ord(first_letter_small) - ord('a') + ord('A'))
    return first_letter_big + word[1:]

source = input().split()
res = []
for word in source:
    res.append(capitalize(word))
print(' '.join(res))
