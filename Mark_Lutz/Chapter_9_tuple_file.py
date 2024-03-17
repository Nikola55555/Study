'''Кортежи (tuple)'''


T = ('Bob', ('dev', 'mgr'))  # Вложенный кортеж
T = tuple('spam')            # Кортеж из элементов итерируемого объекта
T[i]  # index
T[i][j]  # Индекс индекса
T[i:j]   # Срез
len(T)   # Длина
T1 + T2   # Конкатенация
T1*3   # повторение

for i in T: print(i)  # Итерация
'spam' in T    # Членство
[x ** 2 for x  in T]
T.index('Ni')   # Поиск
T.count('Ni')   # Подсчет

T = ('cc', 'aa', 'dd', 'bb')
tmp = list(T)  # Создание списка из элементов кортежа
tmp.sort()   # Сортировка списка
T = tuple(tmp)   # Создание кортежа из элементов списка
sorted(T)  # Использование встроенной функции sorted и экономия 2х шагов

'''File'''

output = open(r'C:\spam', 'w')     # Создает выходной файл. 'w'  означает write - запись
input = open('data', 'r')          # Создает входной файл. 'r'  означает read - чтение
input = open('data')               # То же, что и в предыдущей строке. 'r'  выбирается по умолчанию
aString = input.read()             # Читаем цклый файл в одиночную строку
aString = input.read(N)            # Читает до N следующих символов (или байтов) в строку
aString = input.readline()         # Читает следующую строку файла (считая символ новой строки \n) в строку
aList = input.readlines()          # Читает целый файл в список строк (с символами \n)
output.write(aString)              # Записывает строку символов (или байтов) в файл
output.write(aList)                # Записывает все строки из списка в файл
output.close()                     # Вручную закрывает файл (это делается автоматически, когда файловый объект подвергается сборке мусора)
output.flush()                     # Сбрасывает буфер вывода на диск, не закрывая файл
anyFile.seek(N)                    # Изменяет позицию на N для следующей операции

for line in open('data'):          # Файловые итераторы, читающиестроку за строкой
    line = line.strip()

open('f.txt', encoding='latin-1')
open('f.bin', 'rb')                # Байтовые файлы (строки bytes)

"""JSON"""////////////////////////////////////////////////////////////////////////////////

name = dict(first='Bob', last='Smith')
rec = dict(name=name, job=['dev', 'mgr'], age=40.5)
print(rec)    # {'name': {'first': 'Bob', 'last': 'Smith'}, 'job': ['dev', 'mgr'], 'age': 40.5}

import json

json.dumps(rec)
S = json.dumps(rec)
print(S)  # '{"name": {"first": "Bob", "last": "Smith"}, "job": ["dev", "mgr"], "age": 40.5}'

O = json.loads(S)
print(O)  # {'name': {'first': 'Bob', 'last': 'Smith'}, 'job': ['dev', 'mgr'], 'age': 40.5}
O == rec # True

json.dump(rec, fp=open('testjson.txt', 'w'), indent=4)
print(open('testjson.txt').read())
'''{
    "name": {
        "first": "Bob",
        "last": "Smith"
    },
    "job": [
        "dev",
        "mgr"
    ],
    "age": 40.5
}
'''

P = json.load(open('testjson.txt'))
P  # {'name': {'first': 'Bob', 'last': 'Smith'}, 'job': ['dev', 'mgr'], 'age': 40.5}

