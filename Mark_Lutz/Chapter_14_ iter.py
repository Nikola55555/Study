"""Итерации и включения"""

print(open('script2.py').read())    #  Входной файл для демонстрации
# import sys
# print(sys.path)
# x = 2
# print(x ** 32)

f = open('script2.py')  # Чтение четырехстрочного файла сценария в текущем каталоге
f.readline()  # 'import sys\n'   # При каждом вызове readline загружается одна строка
f.readline()  #  'print(sys.path)\n'
f.readline()  #  'x = 2\n'
f.readline()  #  'print(x ** 32)\n'  # Последние строки могут иметь или не иметь \n
f.readline()  #   ''      # При достижении конца файла, возвращается пустая строка

f = open('script2.py')  # При каждом вызове метод __next__ так же загружает одну строку
f.__next__() #  'import sys\n'
f.__next__() #   'print(sys.path)\n'
f.__next__() #   'x = 2\n'
f.__next__() #    'print(x ** 32)\n'
f.__next__() #                         # Но по достижении конца файла генерирует исключение
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# Stopiteration

"""Данный интерфейс является большей частью того, что мы называем протоколом 
итерации в Python. Любой объект с методом__ next__для перехода на следующий
результат, который генерирует исключение Stop Iteration при достижении конца 
серии результатов, в Python считается итератором."""


for line in open('script2.py'):
    print(line.upper(), end='')  # Использование итератора файлового
                                # объекта для чтения по строкам Вызывает__next__, перехватывает Stopiteration
# IMPORT SYS
# PRINT(SYS.PATH)
# X = 2
# PRINT(X ** 32)

f = open('script2.py')
f.__next__()   # Вызов итерационного метода напрямую
# 'import sys\n'
f.__next__()   #  'print(sys.path)\n'

f = open('script2.py')
next(f)   # Встроенная функция next(f) вызывает f.__next__()
# 'import sys\n'
next(f)
# 'print(sys.path)\n'


L = [1, 2, 3]
I = iter(L)     # Получение объекта итератора из  итерируемого объекта
I.__next__()    # Вызов метода next итератора для продвижения на следующий элемент
# 1
I.__next__()    #  Или применение next(I)
# 2
I.__next__()
# 3
I.__next__()
# StopIteration

"""Файлы сами по себе итераторы"""

f = open('script2.py')  # файловый объект имеет собственный метод
                        # _ next__и не нуждается в возвращении особого объекта, который предоставлял бы
                        # этот метод:
iter(f) is f   # True
iter(f) is f.__iter__()  # True
f.__next__()  # 'import sys\n'

"""списки и многие другие встроенные объекты не являются итераторами сами по себе"""

L = [1, 2, 3]
iter(L) is L  # False
L.__next__()  # AttributeError: 'list’ object has no attribute ’__next__'
              # Ошибка атрибута: объект list не имеет атрибута __next__
I = iter(L)
I.__next__()
# 1
next(I)   # то же сто и I.__next__()
# 2

"""Автоматическая и ручная итерация"""

L = [1, 2. 3]
for x in L:               # Автоматическая итерация
    print(x**2, end=' ')  # Получает iter, вызывает__next__, перехватывает исключения
# 1 4 9

I = iter(L)               # Ручная итерация: то, что обычно делают циклы for
while True:
    try:                  # Оператор try перехватывает исключения
        x = next(I)       # Или вызов I.__next__
    except StopIteration:
        break
    print(x**2, end=' ')
# 1 4 9

