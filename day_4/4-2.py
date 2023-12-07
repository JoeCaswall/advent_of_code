from pathlib import Path

path = Path("example_input.txt")
contents = path.read_text()
cards = contents.splitlines()

enumerated = {}

for index, card in enumerate(cards):
    points = 0
    irrelevant, all_numbers = card.split(": ")
    winning_numbers, my_numbers = all_numbers.split(" | ")
    winning_numbers = winning_numbers.replace("  ", " ")
    winning_numbers = winning_numbers.lstrip()
    my_numbers = my_numbers.replace("  ", " ")
    my_numbers = my_numbers.lstrip()
    winning_numbers = winning_numbers.split(" ")
    my_numbers = my_numbers.split(" ")
    enumerated[index + 1] = [winning_numbers, my_numbers]

# print(enumerated)



def num_of_wins(game):
    num_of_matches = 0
    for x in game[1]:
        if x in game[0]:
            num_of_matches += 1
    return num_of_matches

wins_list = []

for x in range(1, len(enumerated)):
    num_wins_for_that_game = num_of_wins(enumerated[x])
    for y in range(x + 1, x + num_wins_for_that_game):
        enumerated[y].append([enumerated[y][1]])

# print(enumerated)

for each_game in enumerated:
    enumerated[each_game].remove(enumerated[each_game][0])

print(len(enumerated.values()))