with open('J5data.txt') as f:
    lines = f.readlines()

def parse_mapping_data(lines):
    seed_ids = []
    mappings = {}
    current_map = None

    for i,line in enumerate(lines):
        print(i,"-----",line)
        if "seeds" in line:
            seeds_list = line.split("seeds: ")[1].replace("\n","").split(" ")
            seed_ids = [int(s) for s in seeds_list]
        elif 'map:' in line:
            current_map = line.split(':')[0]
            mappings[current_map] = []
        elif "\n" == line or " " == line:
            pass
        else:
            parts = line.split()
            if len(parts) == 3:
                mappings[current_map].append(tuple(map(int, parts)))
    return seed_ids,mappings

seeds,mappings = parse_mapping_data(lines)

# check mapping
for map in mappings.items():
    for m in map[1]:
        if len(m) != 3:
            print("ratio")

for seed in seeds:
    seed_life = seed
    for map_index, map in mappings.items():
        for val in map:
            destination_start, source_start, range = val
            if seed in range(source_start,source_start + range):
                seed_life = destination_start + ()
