from pathlib import Path

path = Path("input.txt")
contents = path.read_text()
lines = contents.splitlines()

min = {"red": 0, "green": 0, "blue": 0}
min_possible = []

for line in lines:
    game, cubes = line.split(":")
    cubes = cubes.replace(";", ",")
    game_id = game.removeprefix("Game ")
    game_id = int(game_id)

    hand = cubes.split(",")
    for x in hand:
        x = x.lstrip()
        quantity, color = x.split(" ")
        quantity = int(quantity)

        if quantity > min[color]:
            min[color] = quantity
            

    min_possible.append(min)
    min = {"red": 0, "green": 0, "blue": 0}

product_list = []
result = 1

print(min_possible)

for x in min_possible:
    for quant in x.values():
        result *= quant
    product_list.append(result)
    result = 1

print(product_list)

sum = sum(product_list)

print(sum)