stroka = input('Введите строку из нескольких слов, разделяя слова пробелами ')
count = stroka.count(' ')
new_stroka = stroka.split()
num = 1
for el in range(count + 1):
    if len(new_stroka[el]) <= 10:
        print(f'{num} {new_stroka[el]}')
    else:
        print(f'{num} {new_stroka[el][:10]}')
    num += 1



