from collections import Counter

with open('J9data.txt') as f:
# with open('datatest.txt') as f:
    lines = f.readlines()

results = []
for line in lines:
    numbers = list(map(int,line.replace("\n","").split(" ")))
    last_numbers = [numbers[-1]]
    while Counter(numbers)[0] != len(numbers):
        new_numbers = []
        for number_index in range(len(numbers)-1):
            new_numbers.append(numbers[number_index+1]-numbers[number_index])
        numbers = new_numbers
        last_numbers.append(numbers[-1])
    results.append(sum(last_numbers))
print(sum(results))