with open('J4data.txt') as f:
    lines = f.readlines()

import numpy as np

result = 0
for line in lines:
    streak=0
    win_list, have_list = line.split("|")
    win_list = win_list.split(":")[1].split(" ")
    have_list = have_list.replace("\n","").split(" ")
    for have_number in have_list:
        if have_number != "" and have_number in win_list:
            print(have_number)
            streak += 1
    result += np.floor(2 ** (streak - 1))