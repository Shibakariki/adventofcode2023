with open('J6data.txt') as f:
    lines = f.readlines()

time_data = ""
for time in lines[0].split()[1:]:
    time_data += time
time_data = int(time_data)
distance_data = ""
for distance in lines[1].split()[1:]:
    distance_data += distance
distance_data = int(distance_data)


number_of_win = 0
for speed in range(time_data):
    dist = (time_data - speed) * speed
    if distance_data < dist:
        number_of_win += 1
print(number_of_win)