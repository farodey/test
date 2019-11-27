import sys
import numpy as np
import statistics


def average_val(lst):
    return sum(lst) / len(lst)


list_num = []
with open(sys.argv[1]) as file:
    for line in file:
        list_num.append(int(line))

print("%.2f" % np.percentile(np.array(list_num), 90))
print("%.2f" % statistics.median(list_num))
print("%.2f" % max(list_num))
print("%.2f" % min(list_num))
print("%.2f" % average_val(list_num))
