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

current_index = "AAA"
counter = 0
while current_index != "ZZZ":
    for instruction in instructions:
        counter += 1
        current_index = df.loc[current_index][instruction]
        if current_index == "ZZZ":
            break

print(counter)