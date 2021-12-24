# 1 способ
def my_func(x, y):
    return x ** y


# 2 способ
def mi_func(x, y):
    result = 1
    for _ in range(abs(y)):
        result = result * x
    return 1 / result


print(my_func(2, -5))
print(mi_func(2, -5))
