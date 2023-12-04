with open('J4data.txt') as f:
    lines = f.readlines()

import numpy as np
from collections import defaultdict

result = 0
nb_copy = {}
for card_number,line in enumerate(lines):
    streak = 0
    win_list, have_list = line.split("|")
    win_list = win_list.split(":")[1].split(" ")
    have_list = have_list.replace("\n","").split(" ")
    for have_number in have_list:
        if have_number != "" and have_number in win_list:
            streak += 1
    if not card_number in nb_copy.keys():
        nb_copy[card_number] = 0
    nb_copy[card_number] += 1
    for s in range(card_number + 1 ,card_number + 1 + streak):
        if not s in nb_copy.keys():
            nb_copy[s] = 0
        nb_copy[s] += 1*nb_copy[card_number]
    # print("-----------")
    # print(streak)
    # print(nb_copy)
    print(sum(nb_copy.values()))
