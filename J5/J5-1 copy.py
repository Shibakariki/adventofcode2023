with open('test_data.txt') as f:
    lines = f.readlines()

def get_dest(dest_start, source_start, range_num, source):
    source_diff = source - source_start
    res = source
    if source_diff >= 0 and source_diff < range_num :
        res = dest_start + source_diff
    return res

seed_ids = []
seed_ranges = []
seed_changed = []
# destination_range = []
source_range = []
shift = []
for i,line in enumerate(lines):
    if "seeds" in line:
        seed_ids = list(map(int,line.split("seeds: ")[1].replace("\n","").split(" ")))
        seed_ids_1 = seed_ids[::2]
        seed_ids_2 = seed_ids[1::2]
        for s_index in range(len(seed_ids_1)):
            list_of_range = range(seed_ids_1[s_index],seed_ids_1[s_index] + seed_ids_2[s_index])
            seed_ranges = seed_ranges + [list_of_range]
    else:
        if "map" in line and source_range != []:
            print(line)
            for i,seed_range in enumerate(seed_ranges):
                for s,s_range in enumerate(source_range):
                    inter_range = set(seed_range).intersection(s_range)
                    if len(inter_range) > 0:
                        new_inter = list(map(lambda x : x+shift[s],inter_range))
                        seed_ranges[i] = new_inter + list(set(seed_range).difference(inter_range))
                        # print(seed_ranges[i])
        if line[0].isdigit():
            dest, source, range_num = list(map(int,line.replace("\n","").split(" ")))
            # destination_range.append(range(dest,dest+range_num))
            source_range.append(range(source,source+range_num))
            shift.append(dest-source)


# Intersection : set(range(79,93)).intersection(range(80,90))