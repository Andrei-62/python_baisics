with open('Test.txt', 'w') as f:
    numer = input('Введите числа через пробел - ')
    f.write(numer)
    my_num = numer.split()

sum = 0
for i in range(len(my_num)):
    sum += int(my_num[i])
print(sum)

