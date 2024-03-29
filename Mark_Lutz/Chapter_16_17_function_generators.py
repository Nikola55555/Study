"""Functions"""

othername = func   # Присваивание объекта функции
othername()        # Вызов функции


def func(): ....   # Создание объекта функции
func()             # Вызов объекта функции
func.attr = value  # Присваивание атрибутов

def times(x, y):   # Создание  и присваивание функции
    return x * y   # Тело выполняется при вызове

times(2, 4)  # Аргументы в круглых скобках
# 8

x = times(3.14, 4)   # Сохранение результирующего объекта
print(x) >>> 12.56

times('Ni', 4) >>>> 'NiNiNiNi'    # Функции "лишены типов"

def intersect(seq1, seq2):
    res = []                 # Начать с пустого результата
    for x in seq1:           # Просмотр seq1
        if x in seq2:        # Общий элемент?
            res.append()     # Добавить в конец результата
    return res
#///////////////////////////////////////////////////

# Глобальная область видимости
X = 99                # имена X и func присваиваются в модуле: глобальные
def func(Y):         # имена Y и Z присваиваются в функции: локальные
    Z = X + Y           # имя X является глобальным
    return Z
func(1)   # Имя func  в модуле: result=100


X = 88             # Глобальная переменная X
def func():
    global X
    X = 99          # Глобальная переменная X: снружи def
func()
print(X)   # 99

y, z = 1, 2         # Глобальные переменные в модуле
def all_global():
    global x        # Объявление присваиваемой глобальной переменной
    X = z + y       # Объявлять z, y не нужно: правило LEGB

# ///////Другие способы доступа к глобальным переменным\\\\\\\\\\

# thismod.py

var = 99      # Глобальнвая переменная == атрибут модуля

def local():
    var = 0     # Изменение локальной переменной

def glob1():
    global var     # Объявление глобальной переменной
    var += 1       # Изменение глобальной переменной

def glob2():
    var = 0            # Изменение локальной переменной
    import thismod     # Импортирование самого себя
    thismod.var += 1   # Изменение глобальной переменной

def glob3():
    var = 0             # Изменение локальной переменной
    import  sys         # Импортирование системной таблицы
    glob = sys.modules['thismod']    # Получение объекта модуля  (либо использовать __name__)
    glob.var += 1        # Изменение глобальной переменной

def test():
    print(var)
    local(), glob1(), glob2(), glob3()
    print(var)
 # 99
 # 102
 print(thismod.var)   # 102

#//////////////////////////////////// Примеры вложенных областей видимости/////////////////////////////////

X = 99               # Имя в глобальной области видимости: не используется
def f1():
    X = 88           # Локальная область видимости объемлющего def
    def f2():
        print(X)      #  Ссылка во вложенои def
    f2()
f1()                  #  Выводит 88: локальное имя объемлющего def

# /////////////////////////////////////////

def f1():
    X = 88
    def f2():
        print(X)         # Помнит имя X из области видимости объемлющего def
    return f2            # Возвращает объект функции f2, но не вызывает функцию

action = f1()            # Создает и возвращает объект функции
action()                 # Вызов функции: выведет 88

# //////////////////////////////////////////// Замыкания   //////////

def maker(N):
    def action(X):             # Создание и возвращение функции action
        return X * N           # action сохраняет N из объемлющей области видимости
    return action

f = maker (2)                   # Передача 2 аргументу N
print(f)
# <function maker.<locals>.action at 0x0000000002A4A158>

print(f(3))   # 9                # Передача 3 аргументу X, в N запоминается 2: 3 *★ 29

print(maker(f(4)))  # 16         # 4 ** 2

g = maker (3)                    # g запоминает 3, f запоминает 2
print(g(4))  # 64                # 4 ** 3

print(f(4) #  16                 # 4 ** 2

def maker(N):
    return lambda X: X ** N      # Функция lambda сохраняет состояние

h = maker(3)
h(4)   # 64                      # Снова 4 ** 3


# ///// Сохранение состояния из объемлющей области видимости с помощью стандартных значений /////////

def f1():
    X = 88
    def f2(X=X):           # запоминает X из объемлющей зоны видимости
        print(X)
    f2()
f1()                       # выводит 88

#////////////////////////////////////////////
def f1():
    х = 88                    # Передача х вместо вложения
    f2(х)                     # Опережающая ссылка допустима
def f2(х):
    print(х)                  # Плоский код все еще нередко лучше вложенного!
f1()   # 88

#////////////////////////

def func():
    x = 4
    action = (lambda n: x ** n)    # X запоминается из объемлющего def
    return action

x = func()
print(x()2))                      # Выводит 16,  4 ** 2

# //////////// Операторы nonlocal  \\\\\\\\\\\\\\\\\\\\\\\\\\

def func():
    nonlocal namel, name2, ... # Здесь нормально
>>> nonlocal X
SyntaxError: nonlocal declaration not allowed at module level
Синтаксическая ошибка: объявление nonlocal не разрешено на уровне модуля

def tester(start):
    state = start     # Ссылка не нелокальные переменные работает нормально
    def nested(label):
        print(label, state)    # Запоминает state из объемлющей области видимости
    return nested

F = tester(0)
print(F('spam'))  >>> spam 0
print(F('ham')) >>>>> ham 0

def tester(start):
    state = start
    def nested(label):
        print(label, state)
        state += 1          # По умолчанию изменять нельзя
    return nested

F = tester(0)
print(F('spam'))

UnboundLocalError: local variable ’state’ referenced before assignment
Ошибка несвязанной локальной переменной: ссылка на локальную переменную
state перед ее присваиванием

def tester(start):
    state = start            # Каждый вызов получает собственное значение state
    def nested(label):
        nonlocal state       # Запоминает из объемлющей области видимости
        print(label, state)
        state += 1          # Нелокальную переменную разрешено изменять
    return nested

F = tester(0)
print(F('spam'))              # При каждом вызове state инкрементируется
>>> spam 0
print(F('ham'))
>>> ham 1
print(F('eggs'))
>>> eggs 2

def tester (start) :
    def nested(label):
        nonlocal state               # Нелокальные переменные уже должны существовать в объемлющем def!
        state = О
        print(label, state)
    return nested
SyntaxError: no binding for nonlocal ’state' found
Синтаксическая ошибка: не найдена привязка для нелокальной переменной state
def tester (start) :
    def nested(label):
        global state             # Глобальные переменные не обязаны существовать до их объявления
        state = 0                # Создает имя в области видимости модуля
        print(label, state)
    return nested
F = tester (0)
F('abc’) >>>> abc 0
>>> state
0

////////////////////////////////////////

spam = 99
def tester () :
    def nested () :
        nonlocal spam                 # Должна быть в def, а не в модуле!
        print(’Current=', spam)
        spam += 1
    return nested
SyntaxError: no binding for nonlocal ’spam' found
Синтаксическая ошибка: не найдена привязка для нелокальной переменной spam

>>> def tester(start):
        state = start            # Каждый вызов получает собственное значение state
        def nested(label):
            nonlocal state        # Запоминает state из объемлющей области видимости
            print(label, state)
            state += 1            # Нелокальную переменную разрешено изменять
        return nested
>>> F == tester (0)
>>> F('spam')                    # Переменная state видима только внутри замыкания
spam 0
>>> F.state
AttributeError: 'function' object has no attribute 'state'
Ошибка атрибута: объект function не имеет атрибута state

# ////////////  Состояния с помощью классов  \\\\\\\\\\\\\

class tester:                     # Альтернатива на основе класса
    def __init__(self, start):    # При создании объектов состояние
        self.state = start        # явно сохраняется в новом объекте
    def nested (self, label):
        print(label, self.state)  # Явная ссылка на состояние
        self.state += 1           # Изменения также разрешены

F = tester(0)                     # Создание экземпляра, вызов__init__
F.nested('spam') >>> spam 0        # F передается аргументу self
F.nested('ham')  >>> ham 1


class tester:
    def __init__(self, start):
        self.state = start

    def __call__(self, label):    # Перехватывает прямые обращения к экземпляру
        print(label, self.state)  # Таким образом, .nested() не требуется
        self.state += 1

H = tester(99))
H('spam') >>> spam                  Вызывает __call__
H('pancakes') >>> pancakes 100

# ////////////////// exercises   \\\\\\\\\\\\\\\\\\\\\\\\\\\

X = 'spam'
def func():
    print(X)
func()   # spam


def func1():
    X = 'NI'
func1()
print(X)  # spam

X = 'spam'
def func():
    X = 'NI'
    print(X)
func()   # NI
print(X)  # spam

X = 'spam'
def func():
    global X
    X = 'NI'

func()
print(X)  # NI


X = 'spam'
def func():
    X = 'NI'
    def nested():
        print(X)
    nested()

func()    # NI
print(X)  # spam


X = 'spam'
def func():
    X = 'NI'
    def nested():
        nonlocal X
        X = 'spam'
    nested()
    print(X)

func()    # NI
