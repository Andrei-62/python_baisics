my_dict = {}
with open('object.txt', 'r') as f:
    for line in f.read().split('\n'):
        key = line.split(' ')[0]
        value = line.split(' ')[1:]
        my_dict[key] = value
        
    for i in my_dict:
        my_list = my_dict.get(i)
        sum = 0
        for j in range(len(my_list)):
            sum += int(my_list[j])
        key = i
        value = sum
        my_dict[key] = value
    print(my_dict)
