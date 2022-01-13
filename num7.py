# -*- coding: utf8 -*-
import json

profit = {}
with open('firm.txt', 'r') as f:
    for line in f.read().split('\n'):
        name_firm = line.split()[0]
        my_list = line.split(' ')[2:]
        sum = 0
        count = 1
        for i in range(len(my_list)):
            prof = int(my_list[0])-int(my_list[1])
            if prof > 0:
                sum += prof
                key = name_firm
                value = prof
                profit[key] = value
                count += 1
        ave_profit = sum / count
    profit['average_profit'] = ave_profit

with open('my_file.json', 'w') as f:
    json.dump(profit, f)

json_str = json.dumps(profit)
print(json_str)
