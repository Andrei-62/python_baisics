def div_number(number_1, number_2):
    """Функция выполняет деление двух чисел"""

    if number_2 == 0:
        print('Делить на ноль нельзя')
    else:
        print(number_1 / number_2)


number_1 = int(input('Введите первое число - '))
number_2 = int(input('Введите второе число - '))
div_number(number_1, number_2)

