my_dict = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}
list_num = []
with open('fig.txt', 'r') as f:
    for line in f:
        new_num = line.split()[0]
        list_num.append(new_num)

with open('new_fig.txt', 'w') as my_f:
    count = 0
    while count < 4:
        my_f.writelines(f'{my_dict.setdefault(list_num[count])} - {count + 1}\n')
        count += 1

