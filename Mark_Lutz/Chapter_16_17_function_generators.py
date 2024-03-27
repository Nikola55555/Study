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