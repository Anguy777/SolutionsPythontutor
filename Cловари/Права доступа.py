#Задача «Права доступа»
#Условие
В файловую систему одного суперкомпьютера проник вирус, который сломал контроль за правами доступа к файлам. Для каждого файла известно, с какими действиями можно к нему обращаться:
#запись W,
#чтение R,
#запуск X.
#В первой строке содержится число N — количество файлов содержащихся в данной файловой системе. В следующих N строчках содержатся имена файлов и допустимых с ними операций, разделенные пробелами. Далее указано чиcло M — количество запросов к файлам. В последних M строках указан запрос вида Операция Файл. К одному и тому же файлу может быть применено любое колличество запросов.
#Вам требуется восстановить контроль над правами доступа к файлам (ваша программа для каждого запроса должна будет возвращать OK если над файлом выполняется допустимая операция, или же Access denied, если операция недопустима.
n = int(input())
d={}
a=[]
for i in range(n):
    for w in input().split():
        a.append(w)
    d[i] = a
    a = []
n = int(input())
for i in range(n):
    op,f = [str(i) for i in input().split()]
    for val in d.values():
        if f in val:
            if op == 'write' and 'W' in val:
                print('OK')
            elif op == 'read' and 'R' in val:
                print('OK')
            elif op == 'execute' and 'X' in val:
                print('OK')
            else:
                print('Access denied')

#Решение разрабов:
ACTION_PERMISSION = {
    'read': 'R',
    'write': 'W',
    'execute': 'X',
}

file_permissions = {}
for i in range(int(input())):
    file, *permissions = input().split()
    file_permissions[file] = set(permissions)

for i in range(int(input())):
    action, file = input().split()
    if ACTION_PERMISSION[action] in file_permissions[file]:
        print('OK')
    else:
        print('Access denied')
