with open('dataJ2.txt') as f:
    lines = f.readlines()

max_red = 12
max_green = 13
max_blue = 14

def get_number_color(set_items):
    number_color = {}
    for item in set_items:
        number,color = item.replace("\n","").split(" ")[1:]
        number_color[color] = number
    return number_color

def is_color_is_good():
    res = True
    for item in set_items:
        number,color = item.replace("\n","").split(" ")[1:]
        if color == "red":
            if int(number) > max_red:
                res = False
        elif color == "green":
            if int(number) > max_green:
                res = False
        elif color == "blue":
            if int(number) > max_blue:
                res = False
    return res

game_number_counter = 0 
for line in lines:
    game_number = line.split(":")[0].split("Game ")[1]
    bag_sets = line.split(":")[1].split(";")
    number_color_bag = []
    # print('----------{}----------'.format(game_number))
    # print(bag_sets)
    is_bag_good = True
    for set in bag_sets:
        set_items = set.split(",")
        if not is_color_is_good():
            is_bag_good = False
            break
    if is_bag_good:
        print('---------- Good : {}----------'.format(game_number))
        print(bag_sets)
        game_number_counter += int(game_number)
    else:
        print('---------- Bad : {}----------'.format(game_number))
        print(bag_sets)
print(game_number_counter)
    