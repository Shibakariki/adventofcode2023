from collections import defaultdict

with open('J7data.txt') as f:
# with open('datatest.txt') as f:
    lines = f.readlines()

def get_pos(char):
    if char == "A":
        return 0
    elif char == "K":
        return 1
    elif char == "Q":
        return 2
    elif char == "J":
        return 99
    elif char == "T":
        return 4
    elif char.isdigit():
        return int(char)-2*(int(char)-7)

def get_char(int):
    if int == 0:
        return "A"
    elif int == 1:
        return "K"
    elif int == 2:
        return "Q"
    elif int == 99:
        return "J"
    elif int == 4:
        return "T"
    else:
        return str(int-2*(int-7))

def sort_hands(hands):
    hands_list = []
    for hand in hands:
        hand_list = [*hand]
        new_hand_list = []
        for char in hand_list:
            new_hand_list.append(get_pos(char))
        hands_list.append(new_hand_list)
    hands_list = sorted(hands_list)
    new_hands_list = []
    for hand in hands_list:
        new_hand = ""
        for card in hand:
            new_hand += get_char(card)
        new_hands_list.append(new_hand)
    return new_hands_list

hand_bid = {}
for line in lines:
    hand,bid = line.replace("\n","").split(" ")
    hand_bid[hand] = bid

five_of_kind = []
four_of_kind = []
full_house = []
three_of_kind = []
two_pair = []
one_pair = []
high_card = []

for hand in hand_bid.keys():
    count_char = defaultdict(lambda:0)
    joker_count = 0
    for c in hand:
        if c == "J":
            joker_count += 1
        else:
            count_char[c] += 1
    count_val = [0]
    if len(count_char.values()) > 0:
        count_val = count_char.values()
    max_val = max(count_val)
    if max_val+joker_count == 5:
        five_of_kind.append(hand)
    elif max_val+joker_count == 4:
        four_of_kind.append(hand)
    elif max_val+joker_count == 3:
        if min(count_char.values()) == 2:
            full_house.append(hand)
        else:
            three_of_kind.append(hand)
    elif max_val+joker_count == 2:
        if len(count_char.values()) == 3:
            two_pair.append(hand)
        else:
            one_pair.append(hand)
    else:
        high_card.append(hand)

sorted_five_of_kind = sort_hands(five_of_kind)
sorted_five_of_kind.reverse()
sorted_four_of_kind = sort_hands(four_of_kind)
sorted_four_of_kind.reverse()
sorted_full_house = sort_hands(full_house)
sorted_full_house.reverse()
sorted_three_of_kind = sort_hands(three_of_kind)
sorted_three_of_kind.reverse()
sorted_two_pair = sort_hands(two_pair)
sorted_two_pair.reverse()
sorted_one_pair = sort_hands(one_pair)
sorted_one_pair.reverse()
sorted_high_card = sort_hands(high_card)
sorted_high_card.reverse()


def compute_result(sorted_list,result,rank):
    for sorted_hand in sorted_list:
        print(sorted_hand)
        result += int(hand_bid[sorted_hand]) * rank
        rank += 1
    return result, rank

result = 0
rank = 1
result,rank = compute_result(sorted_high_card,result,rank)
result,rank = compute_result(sorted_one_pair,result,rank)
result,rank = compute_result(sorted_two_pair,result,rank)
result,rank = compute_result(sorted_three_of_kind,result,rank)
result,rank = compute_result(sorted_full_house,result,rank)
result,rank = compute_result(sorted_four_of_kind,result,rank)
result,rank = compute_result(sorted_five_of_kind,result,rank)

print(result)


