import numpy as np

with open('J10data.txt') as f:
# with open('datatest.txt') as f:
    lines = f.readlines()

def get_neighbors(pos,pipe_map):
    pipe_type = pipe_map[pos]
    #print("type :",pipe_type)
    neighbors = []
    if pipe_type == "|":
        first_pipe_type,second_pipe_type = pipe_map[pos[0]-1][pos[1]],pipe_map[pos[0]+1][pos[1]]
        if first_pipe_type == "|" or first_pipe_type == "F" or first_pipe_type == "7":
            #print("first : ",first_pipe_type)
            neighbors.append((pos[0]-1,pos[1]))
        if second_pipe_type == "|" or second_pipe_type == "L" or second_pipe_type == "J":
            #print("second : ",second_pipe_type)
            neighbors.append((pos[0]+1,pos[1]))
    elif pipe_type == "-":
        first_pipe_type,second_pipe_type = pipe_map[pos[0]][pos[1]-1],pipe_map[pos[0]][pos[1]+1]
        if first_pipe_type == "-" or first_pipe_type == "L" or first_pipe_type == "F":
            #print("first : ",first_pipe_type)
            neighbors.append((pos[0],pos[1]-1))
        if second_pipe_type == "-" or second_pipe_type == "7" or second_pipe_type == "J":
            #print("second : ",second_pipe_type)
            neighbors.append((pos[0],pos[1]+1))
    elif pipe_type == "F":
        first_pipe_type,second_pipe_type = pipe_map[pos[0]+1][pos[1]],pipe_map[pos[0]][pos[1]+1]
        if first_pipe_type == "|" or first_pipe_type == "L" or first_pipe_type == "J":
            #print("first : ",first_pipe_type)
            neighbors.append((pos[0]+1,pos[1]))
        if second_pipe_type == "-" or second_pipe_type == "7" or second_pipe_type == "J":
            #print("second : ",second_pipe_type)
            neighbors.append((pos[0],pos[1]+1))
    elif pipe_type == "7":
        first_pipe_type,second_pipe_type = pipe_map[pos[0]+1][pos[1]],pipe_map[pos[0]][pos[1]-1]
        if first_pipe_type == "|" or first_pipe_type == "J" or first_pipe_type == "L":
            #print("first : ",first_pipe_type)
            neighbors.append((pos[0]+1,pos[1]))
        if second_pipe_type == "-" or second_pipe_type == "F" or second_pipe_type == "L":
            #print("second : ",second_pipe_type)
            neighbors.append((pos[0],pos[1]-1))
    elif pipe_type == "L":
        first_pipe_type,second_pipe_type = pipe_map[pos[0]-1][pos[1]],pipe_map[pos[0]][pos[1]+1]
        if first_pipe_type == "|" or first_pipe_type == "7" or first_pipe_type == "F":
            #print("first : ",first_pipe_type)
            neighbors.append((pos[0]-1,pos[1]))
        if second_pipe_type == "-" or second_pipe_type == "J" or second_pipe_type == "7":
            #print("second : ",second_pipe_type)
            neighbors.append((pos[0],pos[1]+1))
    elif pipe_type == "J":
        first_pipe_type,second_pipe_type = pipe_map[pos[0]-1][pos[1]],pipe_map[pos[0]][pos[1]-1]
        if first_pipe_type == "|" or first_pipe_type == "F" or first_pipe_type == "7":
            #print("first : ",first_pipe_type)
            neighbors.append((pos[0]-1,pos[1]))
        if second_pipe_type == "-" or second_pipe_type == "F" or second_pipe_type == "L":
            #print("second : ",second_pipe_type)
            neighbors.append((pos[0],pos[1]-1))
    elif pipe_type == "S":
        first_pipe_type,second_pipe_type,third_pipe_type,fourth_pipe_type = pipe_map[pos[0]-1][pos[1]],pipe_map[pos[0]+1][pos[1]],pipe_map[pos[0]][pos[1]-1],pipe_map[pos[0]][pos[1]+1]
        if first_pipe_type == "|" or first_pipe_type == "F" or first_pipe_type == "7":
            #print("first : ",first_pipe_type)
            neighbors.append((pos[0]-1,pos[1]))
        if second_pipe_type == "|" or second_pipe_type == "L" or second_pipe_type == "J":
            #print("second : ",second_pipe_type)
            neighbors.append((pos[0]+1,pos[1]))
        if third_pipe_type == "-" or third_pipe_type == "F" or third_pipe_type == "L":
            #print("third : ",third_pipe_type)
            neighbors.append((pos[0],pos[1]-1))
        if fourth_pipe_type == "-" or fourth_pipe_type == "7" or fourth_pipe_type == "J":
            #print("fourth : ",fourth_pipe_type)
            neighbors.append((pos[0],pos[1]+1))
    return neighbors

pipe_map = np.empty((len(lines),len(lines[0])), dtype='str')
start_pos = ()
for row,line in enumerate(lines):
    line = line.replace("\n","")
    for col,char in enumerate(line):
        pipe_map[row][col] = char
        if char == "S":
            start_pos = (row,col)

step = -1
already_passed = [start_pos]
neighbors = [start_pos]
while len(neighbors) != 0:
    step += 1
    next_neighbors = []
    for n in neighbors:
        #print(f'----{step}----')
        #print("already_passed : ",already_passed)
        #print("n : ",n)
        new_neighbors = get_neighbors(n,pipe_map)
        tmp_neighbors = []
        for nn in new_neighbors:
            if nn not in already_passed:
                tmp_neighbors.append(nn)
        already_passed.extend(tmp_neighbors)
        next_neighbors.extend(tmp_neighbors)
        #print("rneighbor : ",tmp_neighbors)
    neighbors = next_neighbors
print(step)