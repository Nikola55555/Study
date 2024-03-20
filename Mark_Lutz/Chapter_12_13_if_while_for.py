

'''Глава 13'''

# Присваивание кортежей в циклах for

T = [(1,2), (3, 4), (5, 6)]
for (a, b) in T:                  # Присваивание кортежей в действии
    print(a, b)

# 1 2
# 3 4
# 5 6

"""Создание словарей с помощью dict"""


keys = ['spam', 'eggs', 'bacon']
vals = [1, 3, 5]
D3 = dict(zip(keys, vals))
print(D3)    # {'spam': 1, 'eggs': 3, 'bacon': 5}

{k: v for (k, v) in zip(keys, vals)}    #  {'spam': 1, 'eggs': 3, 'bacon': 5}

################ enumerate    ######################

S = 'spam'
for (offset, item) in enumerate(S):
    print(item, offset)
# s 0
# p 1
# a 2
# m 3

E = enumerate(S)
print(E)    #  <enumerate object at 0x0000023171ED8100>
print(next(E))   #  (0, 's')
print(next(E))   #  (1, 'p')
print(next(E))  #   (2, 'a')

[c * i for (i, c) in enumerate(S)]   #  ['', 'p', 'aa', 'mmm']

