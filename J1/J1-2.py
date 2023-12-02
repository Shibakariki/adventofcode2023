import re

hard_converter = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9,
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
}

def transform_string_number_to_number(string_number,number_with_index):
    # print("----------")
    # print(string_number)
    init_len = len(number_with_index)
    for hc in hard_converter:
        if hc in string_number:
            iters = [m.start() for m in re.finditer(hc,string_number)]
            for iter in iters:
                number_with_index[iter] = hc
    if len(number_with_index) > init_len:
        # print(number_with_index)
        min_index = min(number_with_index.keys())
        max_index = max(number_with_index.keys())
        min_str = number_with_index[min_index]
        max_str = number_with_index[max_index]
        string_number = string_number[:min_index] + str(hard_converter[min_str]) + string_number[len(min_str)+min_index:]
        string_number = string_number[:max_index] + str(hard_converter[max_str]) + string_number[len(max_str)+max_index:]
        # print(string_number)
    return string_number

def get_digit_num(line,nums,number_with_index):
    for i,l in enumerate(line):
        if l.isdigit():
            nums.append(l)
            number_with_index[i] = l

with open('J1-2_data.txt') as f:
    lines = f.readlines()

result = 0
for line in lines:
    nums = []
    number_with_index = {}
    get_digit_num(line,nums,number_with_index)
    line = transform_string_number_to_number(line,number_with_index)
    nums = []
    get_digit_num(line,nums,number_with_index)
    num = int(nums[0])*10 + int(nums[-1])
    result += num
print(result)