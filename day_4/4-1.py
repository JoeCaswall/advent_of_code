from pathlib import Path

path = Path("input.txt")
contents = path.read_text()
cards = contents.splitlines()

points_list = []


for card in cards:
    print(card)
    points = 0
    irrelevant, all_numbers = card.split(": ")
    winning_numbers, my_numbers = all_numbers.split(" | ")
    winning_numbers = winning_numbers.replace("  ", " ")
    winning_numbers = winning_numbers.lstrip()
    my_numbers = my_numbers.replace("  ", " ")
    my_numbers = my_numbers.lstrip()
    winning_numbers = winning_numbers.split(" ")
    my_numbers = my_numbers.split(" ")
    for x in my_numbers:
        if x in winning_numbers:
            if points == 0:
                points = 1
            else:
                points *= 2

    points_list.append(points)

print(len(points_list))

sum = sum(points_list)
print(sum)