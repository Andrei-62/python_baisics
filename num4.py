a = int(input('Введите целое число'))

max = 0
while a > 0:
    if max < (a % 10):
       max = a % 10
    a = a // 10

print('Mаксимальное число ', max)
