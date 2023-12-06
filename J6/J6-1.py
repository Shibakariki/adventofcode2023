with open('J6data.txt') as f:
    lines = f.readlines()

time_data = list(map(int,lines[0].split()[1:]))
distance_data = list(map(int,lines[1].split()[1:]))

result = 1
for course in range(len(time_data)):
    number_of_win = 0
    for speed in range(time_data[course]):
        dist = (time_data[course] - speed) * speed
        if distance_data[course] < dist:
            number_of_win += 1
    result *= number_of_win
print(result)