with open('dataJ2.txt') as f:
    lines = f.readlines()

max_red = 12
max_green = 13
max_blue = 14

def get_max_number_color(set_items,number_color):
    for item in set_items:
        number,color = item.replace("\n","").split(" ")[1:]
        number = int(number)
        if number_color[color] < number:
            number_color[color] = number
    return number_color

def get_power(max_number_color:dict):
    power = 1
    for color in max_number_color:
        power *= max_number_color[color]
    return power

power_counter = 0
for line in lines:
    game_number = line.split(":")[0].split("Game ")[1]
    bag_sets = line.split(":")[1].split(";")
    max_number_color = {"red":0,"green":0,"blue":0}
    print('----------{}----------'.format(game_number))
    print(bag_sets)
    for set in bag_sets:
        set_items = set.split(",")
        max_number_color = get_max_number_color(set_items,max_number_color)
    power_counter += get_power(max_number_color)

print(power_counter)
    