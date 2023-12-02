with open('J1-1_data.txt') as f:
    lines = f.readlines()

all_nums = []
for line in lines:
    nums = []
    for l in line:
        if l.isdigit():
            nums.append(l)
    all_nums.append(int(nums[0])*10 + int(nums[-1]))

sum(all_nums)