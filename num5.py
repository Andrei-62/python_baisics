revenue = int(input('Введите выручку '))
cost = int(input('Введите издержки '))

if revenue > cost:
    print('Фирма работает с прибылью')
    print(f'Рентабельность выручки составила {(revenue - cost) / revenue * 100} %')
    worker = int(input('Введите количество человек фирмы '))
    print(f'Прибыль в расчете на одного сотрудника составила {(revenue - cost) / worker} у.е.')
else:
    print('Фирма работает в убыток')



