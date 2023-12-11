from scipy.spatial import distance

with open('J11data.txt') as f:
# with open('datatest.txt') as f:
    lines = f.readlines()

galaxies_pos = []
all_rows = []
all_cols = []
for row,line in enumerate(lines):
    for col,char in enumerate(line):
        if char == "#":
            galaxies_pos.append((row,col))
            all_rows.append(row)
            all_cols.append(col)

all_rows = set(all_rows)
x2_rows = all_rows.symmetric_difference(list(range(len(lines))))
all_cols = set(all_cols)
x2_cols = all_cols.symmetric_difference(list(range(len(lines[0]))))

result = 0
for i,galaxie in enumerate(galaxies_pos):
    for j,other_galaxie in enumerate(galaxies_pos[i+1:]):
        min_row = min(galaxie[0],other_galaxie[0])
        max_row = max(galaxie[0],other_galaxie[0])
        min_col = min(galaxie[1],other_galaxie[1])
        max_col = max(galaxie[1],other_galaxie[1])
        dist_row = max_row - min_row
        dist_col = max_col - min_col
        additionnal_rows = len(set(range(min_row,max_row+1)).intersection(x2_rows))
        additionnal_cols = len(set(range(min_col,max_col+1)).intersection(x2_cols)) 
        dist_row += additionnal_rows * 999999 # Multiplication is the difference for the 2nd part
        dist_col += additionnal_cols * 999999 # Multiplication is the difference for the 2nd part
        # print(f"Galaxies {i+1} et {i+1+j+1} : ",dist_row+dist_col)
        result += dist_row+dist_col
print(result)