with open('text.txt', 'r') as f:
    count_strok = 0
    count_wrd = 0
    for line in f:
        count_strok += 1
        count_wrd = line.count(' ')
        print(f'Количество слов в {count_strok} строке - {count_wrd + 1} слова')

print(f'Количество строк в файле - {count_strok}')
