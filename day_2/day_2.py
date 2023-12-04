"""the Elf shows you a small bag and some cubes which are either red, green, or blue. 
Each time you play this game, he will hide a secret number of cubes of each color in the bag, 
and your goal is to figure out information about the number of cubes."""

from pathlib import Path

path = Path("input.txt")
contents = path.read_text()
lines = contents.splitlines()

max = {"red": 12, "green": 13, "blue": 14}
possible_games = []

for line in lines:
    game, cubes = line.split(":")
    cubes = cubes.replace(";", ",")
    game_id = game.removeprefix("Game ")
    game_id = int(game_id)
    is_possible_game = True

    hand = cubes.split(",")

    for x in hand:
        x = x.lstrip()
        quantity, color = x.split(" ")
        quantity = int(quantity)

        if quantity > max[color]:
            is_possible_game = False
            break

    if is_possible_game:
        possible_games.append(game_id)

print(possible_games)
sum_of_possible_ids = sum(possible_games)
print(sum_of_possible_ids)
