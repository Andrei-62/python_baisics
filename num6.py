from itertools import count
from itertools import cycle
import random

def iter_generation1():
    num = int(input('Введите число начала счета - '))
    for el in count(num):
        if el > 10:
            break
        else:
            print(el, end=' ')


def iter_generetion2(my_list):
    count = 0
    for el in cycle(my_list):
        if count > 10:
            break
        print(el, end=' ')
        count += 1

my_list = [1, 2, 3]
iter_generation1()
iter_generetion2(my_list)
