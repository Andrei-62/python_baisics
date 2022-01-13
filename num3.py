with open('salary.txt', 'r') as f:
    sum = 0
    count = 0
    for line in f:
        surname = line.split()[0]
        sal = line.split()[1]
        if int(sal) < 20000:
            print(f'Зарплата {surname} меньше 20 тысяч')
        sum += int(sal)
        count += 1
    print(f'Средняя зарплата сотрудников {sum / count}')