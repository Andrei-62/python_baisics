my_list = []
a = int(input('Введите количество элементов списка '))
for el in range(a):
    my_list.append(input('Введите содержимое списка '))
print(my_list)

count = 0
while count < a - 1:
    my_list[count], my_list[count + 1] = my_list[count + 1], my_list[count]
    count += 2 
print(my_list)


