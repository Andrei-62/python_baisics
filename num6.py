product = []
num = 1

while True:
    title = input('Введите название товара - ')
    price = input('Введите цену товара - ')
    amount = input('Введите количество товара - ')
    unit = input('Введите единицу измерения - ')

    product.append((num, {'название':title, 'цена':price, 'количество':amount, 'единицы':unit}))
    num +=1
    a = input('Продолжить формирование списка?(Если да нажмите - y, если нет нажмите - n)')
    if a == 'n':
        break
        
for el in range(len(product)):
    print(product[el])

#аналитику не могу сделать((


