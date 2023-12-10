import numpy as np

with open('J10data.txt') as f:
# with open('datatest.txt') as f:
    lines = f.readlines()

def get_neighbors(pos,pipe_map):
    pipe_type = pipe_map[pos]
    print("type :",pipe_type)
    if pipe_type == "|":
        return [(pos[0]+1,pos[1]),(pos[0]-1,pos[1])]
    elif pipe_type == "-":
        return [(pos[0],pos[1]+1),(pos[0],pos[1]-1)]
    elif pipe_type == "F" or pipe_type == "S":
        return [(pos[0]-1,pos[1]),(pos[0],pos[1]+1)]
    elif pipe_type == "7":
        return [(pos[0]-1,pos[1]),(pos[0],pos[1]-1)]
    elif pipe_type == "L":
        return [(pos[0]+1,pos[1]),(pos[0],pos[1]+1)]
    elif pipe_type == "J":
        return [(pos[0]+1,pos[1]),(pos[0],pos[1]-1)]
    else:
        return []

pipe_map = np.empty((len(lines),len(lines[0])), dtype='str')
start_pos = ()
for row,line in enumerate(lines):
    line = line.replace("\n","")
    for col,char in enumerate(line):
        pipe_map[row][col] = char
        if char == "S":
            start_pos = (row,col)

step = 0
already_passed = [start_pos,(22, 115)]
neighbors = [start_pos]
while len(neighbors) != 0:
    for n in neighbors:
        print('--------')
        print("neighbor : ",n)
        new_neighbors = get_neighbors(n,pipe_map)
        print("nneighbor : ",new_neighbors)
        # new_neighbors = get_neighbors(n,pipe_map)
        step += 1
        neighbors = []
        for nn in new_neighbors:
            if nn not in already_passed:
                neighbors.append((nn))
        already_passed.extend(neighbors)
        print("rneighbor : ",neighbors)

# print(step)