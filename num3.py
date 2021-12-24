def my_func(var_1, var_2, var_3):
    """ Функция возвращает сумму двух наибольших аргументов"""
    if var_1 >= var_2 & var_1 >= var_3:
        return var_1 + var_2
    if var_1 >= var_2 & var_3 >= var_2:
        return  var_1 + var_3
    else:
        return var_2 + var_3


print(my_func(7, 2, 3))




