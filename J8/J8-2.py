import pandas as pd

with open('J8data.txt') as f:
# with open('datatest.txt') as f:
    lines = f.readlines()

instructions = []
df = pd.DataFrame(columns=["index","L","R"])
for i,line in enumerate(lines):
    if i == 0:
        instructions = [*line.replace("\n","")]
    elif line != "\n":
        index,instruction = line.replace("(","").replace(")","").replace("\n","").split(" = ")
        l,r = instruction.split(", ")
        df = pd.concat([df,pd.DataFrame({
            "index":[index],
            "L": [l],
            "R": [r]})])
    else:
        pass
df = df.set_index("index",drop=True)

current_indexs = []
for df_index in df.index:
    if df_index.endswith("A"):
        current_indexs.append(df_index)


results = []
for current_index in current_indexs:
    results_first = []
    counter = 0
    while len(results_first) < 3:
        for instruction in instructions:
            counter += 1
            current_index = df.loc[current_index][instruction]
            if current_index.endswith("Z"):
                results_first.append(counter)
                counter = 0          
            # if counter%10000 == 0:
                # print(counter)
    print(results_first)
    results.append(results_first[0])
print(results)

import functools
import math

def ppcm(a, b):
    return abs(a*b) // math.gcd(a, b)
ppcm_liste = functools.reduce(ppcm, results)
print(ppcm_liste)

