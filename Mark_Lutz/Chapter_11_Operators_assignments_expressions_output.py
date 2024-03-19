"""Операторы присваивания, выражений и вывода"""

spam = "Spam" # Базовая форма присваивания
spam, ham = "yum", "YUM"   #  Присваивание кортежа (позиционное)
[spam, ham] = ["yum", "YUM"]  # Присваивание списка (позиционное)
a, b, c, d = 'spam'  # Присваивание последовательности (обобщенное)
a, *b = 'spam'  #  Расширенная распаковка последовательности
spam = ham = 'lunch'  # Групповое присваивание
spams += 42    # spams = spams + 42

[a, b, c] = (1, 2, 3) #Присваивание кортежа значений списку имен
print(a, c)   # (1, 3)
(a, b, c) = 'ABC' #  Присваивание строки символов кортежу
print(a, c)    # ('A', 'C')

string = 'SPAM'
a, b, c, d = string    # Одинаковое количество с обеих сторон
print(a, d)   #  ('A', 'M')
a, b, c = string   # вызовет ошибку (слишком много значений для распаковки, ожидалось 3)
 a, b, c = string[0], string[1], string[2:]  #  ('S', 'P', 'AM')      Индексация и нарезание
 a, b, c = list(string[:2]) + [string[2:]]   #   ('S', 'P', 'AM')   Нарезание и конкатенация

 a, b = string[:2]
 c = string[2:]
print(a, b, c)   # ('S', 'P', 'AM')  То же самое, но проще

(a, b), c = string[:2], string[2:]
print(a, b, c)   # ('S', 'P', 'AM')   Вложенные последовательности

list(range(3))   # [0, 1, 2]

L = [1, 2, 3, 4]    # Разбиение последовательности на её голову и остальное в цикле
while L:
    front, L = L[0], L[1:]
    print(front, L)

    # 1 [2, 3, 4]
    # 2 [3, 4]
    # 3 [4]
    # 4 []

seq = [1, 2, 3, 4]
a, b, c, d = seg
print(a, b, c, d)  #  1, 2, 3, 4

a, b = seg   # ошибка - слишком много значений для распаковки

a, *b = seg  # ошибки не будет
print(a)  # 1
print(b)  # [2, 3, 4]

*a, b =seg
print(a)  #  [1, 2, 3]
print(b)  #  4

a, *b, c = seg
print(a)   # 1
print(b)   # [2, 3]
print(c)   # 4

a, b, *c = seg
print(a)   # 1
print(b)   # 2
print(c)   # [3, 4]

L = [1, 2, 3, 4]
while L:
    front, *L = L # Получение первого и остальных элементов без нарезания
    print(front, L)
#  1 [2, 3, 4]
#  2 [3, 4]
#  3 [4]
#  4 []

"""Групповое присваивание"""

a = b = 0
b = b + 1
print(а, b)  # (О, 1)

a = b = []
b.append(42)
print(а, b)   # ([42], [42])

a = []
b = [] # а и b не разделяют тот же самый объект
b.append(42)
print(а, b)   #  ([], [42])

a, b = [], [] # а и b не разделяют тот же самый объект


"""Функция print"""

print(x, y)   # Эквивалентно >>>
import sys
sys.stdout.write(str(x) + ' ' + str(y) + '\n')

import sys
sys.stdout = open('log.txt', 'a')   # Перенаправление вывода в файл
print(x, y, z)   # Отправляется в log.txt

"""Автоматическое перенаправление потока"""

import sys
temp = sys.stdout   # Сохранение с целью восстановления в будущем
sys.stdout = open('log.txt', 'a')  # Перенапрвление вывода в файл
print('spam')
print(1, 2, 3)
sys.stdout.close()    # Сброс выводва на диск
sys.stdout = temp   # Восстановление исходного потока
print('back here')   # 'back here'  # Теперь вывод снова виден
print(open('log.txt').read())  # Результат предшествующих выводов
# 'spam'
# 1 2 3

log = open('log.txt', 'a')
print(x, y, z, file=log)   # Вывод в объект подобный файлу
print(a, b, c)  # Вывод в исходный stdout

log = open('log.txt', 'w')
print(1, 2, 3, file=log)
print(4, 5, 6, 7, file=log)
log.close()
print(7, 8, 9) >>>> 7 8 9
print(open('log.txt').read()) >>>>>> 1 2 3
                                     4 5 6

X = 1; Y = 2
print(X, Y)  # Вывод: легкий способ
# 1 2

import sys
sys.stdout.write(str(X) + ' ' + str(Y) + '\n')  # Вывод: сложный способ
# 1 2
#4

print(X, Y, file=open('temp1.txt', 'w'))  # Перенаправление вывода в файл

open('temp2.txt').write(str(X) + ' ' + str(Y) + '\n')  # Отправка в файл вручную

print(open('temp1.txt', 'rb').read())   # Двоичны режим для вывода байтов
# b'1 2\r\n'
print(open('temp2.txt', 'rb').read())
# b'1 2\r\n'

