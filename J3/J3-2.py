with open('J3data.txt') as f:
    lines = f.readlines()

def gear_round_int_pos(pos, gear_pos):
    x, y = pos
    res = False
    for gear in gear_pos:
        if (x, y + 1) == gear:
            return True,gear
        elif (x, y) == gear:
            return True,gear
        elif (x, y - 1) == gear:
            return True,gear
        elif (x + 1, y - 1) == gear:
            return True,gear
        elif (x + 1, y) == gear:
            return True,gear
        elif (x + 1, y + 1) == gear:
            return True,gear
        elif (x - 1, y - 1) == gear:
            return True,gear
        elif (x - 1, y) == gear:
            return True,gear
        elif (x - 1, y + 1) == gear:
            return True,gear
        else:
            pass
    return res,None
    
def is_int_pos_previous_is_int(pos, all_char):
    x, y = pos
    return all_char[x - 1, y].isdigit()

import numpy as np

result = 0

# init np array with string data type with size 140 * 141
all_char = np.empty((len(lines[0]),len(lines)), dtype='str')
int_pos = []
gear_pos = {}
for line_index,line in enumerate(lines):
    for column_index, c in enumerate(line):
        all_char[column_index, line_index] = c
        if c.isdigit():
            int_pos.append((column_index, line_index))
        elif c == '*':
            gear_pos[(column_index, line_index)] = []
        else:
            pass

current_ints_pos = []
number = ''
for pos in int_pos:
    if len(current_ints_pos) == 0:
        current_ints_pos.append(pos)
        number += all_char[pos]
    else:
        if is_int_pos_previous_is_int(pos, all_char):
            current_ints_pos.append(pos)
            number += all_char[pos]
        else:
            print(number)
            print(current_ints_pos)
            is_number_is_good = False
            current_gear = None
            for current_int_pos in current_ints_pos:
                res,gear = gear_round_int_pos(current_int_pos, gear_pos)
                if res:
                    is_number_is_good = True
                    current_gear = gear
            if is_number_is_good:
                print(current_gear)
                gear_pos[current_gear].append(number)
            current_ints_pos = [pos]
            number = all_char[pos]

for gear in gear_pos:
    near_number = gear_pos[gear]
    if len(near_number) == 2:
        result += int(near_number[0]) * int(near_number[1])

print(result)