def user_profile(name='', surname='', year_beth='', city='', email='', phone=''):
    """Функция выводит данные пользователя"""

    name = input('Введите имя пользователя - ')
    surname = input('Введите фамилию пользователя - ')
    year_beth = int(input('Введите год рождения пользователя - '))
    city = input('Введите город проживания пользователя - ')
    email = input('Введите адресс электронной почты - ')
    phone = input('Введите номер телефона - ')
    print(f'{name} {surname} {year_beth} {city} {email} {phone}')


user_profile()
