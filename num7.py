from itertools import count
from math import factorial

def fact():
    for el in count(1):
        yield factorial(el)

n = int(input('Введите число - '))

for el in fact():
    if n > 0:
        print(el)
        n -= 1
    else:
        break
