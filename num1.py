with open('text.txt', 'w') as f:
    line = input('Введите текст - \n')
    while line:
        f.writelines(line)
        line = input('Введите текст - \n')
        if not line:
            break

