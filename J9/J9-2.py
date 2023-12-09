from collections import Counter

with open('J9data.txt') as f:
# with open('datatest.txt') as f:
    lines = f.readlines()

results = []
for line in lines:
    numbers = list(map(int,line.replace("\n","").split(" ")))
    first_numbers = [numbers[0]]
    while Counter(numbers)[0] != len(numbers):
        new_numbers = []
        for number_index in range(len(numbers)-1):
            new_numbers.append(numbers[number_index+1]-numbers[number_index])
        numbers = new_numbers
        first_numbers.append(numbers[0])
    first_numbers.reverse()
    res = 0
    for t in first_numbers[1:]:
        res = t - res
    results.append(res)
print(sum(results))