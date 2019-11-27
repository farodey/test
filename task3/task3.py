import sys
import os


cash_list_str = ['Cash1.txt', 'Cash2.txt', 'Cash3.txt', 'Cash4.txt', 'Cash5.txt', ]
cash_list = []
for cash in cash_list_str:
    with open(os.path.join(sys.argv[1], cash)) as file:
        c1 = []
        for line in file:
            c1.append(float(line))
        cash_list.append(c1)

result_list = []
for time in range(16):
    temp = 0
    for cash in range(5):
        temp += cash_list[cash][time]
    result_list.append(temp)

print(result_list.index(max(result_list)) + 1)

