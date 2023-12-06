with open('J5data.txt') as f:
    lines = f.readlines()

seed_ids = []
tmp_ids = []
for i,line in enumerate(lines):
    if "seeds" in line:
        seed_ids = list(map(int,line.split("seeds: ")[1].replace("\n","").split(" ")))
        tmp_ids = seed_ids.copy()

    elif line[0].isdigit():
        dest, source, range_num = list(map(int,line.replace("\n","").split(" ")))
        for i,seed in enumerate(seed_ids):
            if seed >= source and seed < source + range_num:
                new_dest = dest + (seed - source)
                if new_dest != seed_ids[i]:
                    tmp_ids[i] = new_dest

    elif not line[0].isdigit() and line[0] != "\n":   
        seed_ids = tmp_ids.copy()
      
    else:
        pass
