calendar_list = ['зима', 'весна', 'лето', 'осень']
calendar_dict = dict(key_1='зима', key_2='весна', key_3='лето', key_4='осень')

month = int(input('Введите месяц от 1 до 12 '))
if month < 1 or month > 12:
    print('Нет такого месяца!')
if month == 12 or month == 1 or month == 2:
    print(calendar_list[0])
    print(calendar_dict.get('key_1'))
if month == 3 or month == 4 or month == 5:
    print(calendar_list[1])
    print(calendar_dict.get('key_2'))
if month == 6 or month == 7 or month == 8:
    print(calendar_list[2])
    print(calendar_dict.get('key_3'))
if month == 9 or month == 10 or month == 11:
    print(calendar_list[3])
    print(calendar_dict.get('key_4'))


