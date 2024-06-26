# /////////////////   map  \\\\\\\\\\\\\\\\\\\\\\\\\\

counters = [1, 2, 3, 4]
updated = []
for x in counters:
    updated.append(x + 10)   # добавить 10 к каждому элементу
# [11, 12, 13, 14]

def inc(x): return x + 10     # функция подлежащая выполнению
list(map(inc,counters))       # накапливание результата
# [11, 12, 13, 14]

>>>list(map((lambda x: x + 3), counters))   # Выражение функции
# [4, 5, 6, 7]

||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
def mymap(func, iterable):     # Написали свою функцию, аналог map
    res =[]
    for x in iterable:
        res.append(func(x))
    return res

>>> list(map(inc, [1,2,3]))       # Встроенная функция является итерируемым объектом
# [11, 12, 13]
>>> mymap(inc, [1,2,3])    # Наша функция строит список (см. генераторы)
# [11, 12, 13]
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


>>> pow(3, 4) # 34**
# 81
>>> list(map(pow, [1, 2, 3], [2, 3, 4]))              # 1**2 2**3 3**4
# [1, 8, 81]

>>> list(map(inc, [1, 2, 3, 4]))
# [11, 12, 13, 14]
>>> [inc(x) for x in [1, 2, 3, 4]]               # Для генерации элементов взамен используйте ()
# [11, 12, 13, 14]

# /////////////// filter \\\\\\\\\\\\\\\\\\\

list(filter((lambda  x: x > 0), range(-5, 5)))
# [1, 2, 3, 4]

# res = []
# for х in range (-5, 5) : # Операторный эквивалент
#       if х > 0:
#       res.append(x)
# print(res)    >>>>  [1, 2, 3, 4]

[х for х in range(-5, 5) if х > 0]
# [1, 2, 3, 4]

# ///////////////  reduce \\\\\\\\\\\\\\\\\\\\

from functools import reduce
>>> reduce((lambda x, y: x + y), [1, 2, 3, 4])  # 10
>>> reduce((lambda x, y: x * y), [1, 2, 3, 4])  # 24

def myreduce(function, sequence):          # Самописная функция reduce
    tally = sequence[0]
    for next in sequence [1:]:
        tally = function(tally, next)
    return tally

>>> myreduce ((lambda x, у: x + у) , [1, 2, 3, 4, 5])
# 15
>>> myreduce ((lambda x, y: x * y) , [1, 2, 3, 4, 5])
# 120
