def summation():
    """Функция выполняет суммирование чисел """
    flag = False
    result = 0
    while flag == False:
        numbers = input('Введите числа через пробел, если хотите выйти введите q ').split()
        for i in range(len(numbers)):
            if numbers[i] == 'q':
                flag = True
                break
            else:
                result += int(numbers[i])
        print(result)


summation()

