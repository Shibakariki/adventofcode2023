with open('J3data.txt') as f:
    lines = f.readlines()

def is_int_pos_rounded_by_symbol(pos, symbol_pos):
    x, y = pos
    if (x, y + 1) in symbol_pos:
        return True
    elif (x, y - 1) in symbol_pos:
        return True
    elif (x + 1, y - 1) in symbol_pos:
        return True
    elif (x + 1, y) in symbol_pos:
        return True
    elif (x + 1, y + 1) in symbol_pos:
        return True
    elif (x - 1, y - 1) in symbol_pos:
        return True
    elif (x - 1, y) in symbol_pos:
        return True
    elif (x - 1, y + 1) in symbol_pos:
        return True
    else:
        return False
    
def is_int_pos_previous_is_int(pos, all_char):
    x, y = pos
    return all_char[x - 1, y].isdigit()

import numpy as np

result = 0

# init np array with string data type with size 140 * 141
all_char = np.empty((len(lines[0]),len(lines)), dtype='str')
int_pos = []
symbol_pos = []
for line_index,line in enumerate(lines):
    for column_index, c in enumerate(line):
        all_char[column_index, line_index] = c
        if c.isdigit():
            int_pos.append((column_index, line_index))
        elif not c.isdigit() and c != '\n' and c != '.' and c != ' ':
            symbol_pos.append((column_index, line_index))
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
            is_number_is_good = False
            for current_int_pos in current_ints_pos:
                if is_int_pos_rounded_by_symbol(current_int_pos, symbol_pos):
                    is_number_is_good = True
            if is_number_is_good:
                print(number)
                result += int(number)
            current_ints_pos = [pos]
            number = all_char[pos]

print(result)