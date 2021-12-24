def int_func(word):
    """Функция делает первую букву заглавной"""
    big_first = chr(ord(word[0]) - 32)
    return big_first + word[1:]


word = input('Введите слово из маленьких латинских букв - ')
print(int_func(word))
stroka = input('Введите строку из латинских букв разделяя их пробелами - ')
count = stroka.count(' ')
new_stroka = stroka.split()
for i in range(count + 1):
    print(int_func(new_stroka[i]), end=' ')
