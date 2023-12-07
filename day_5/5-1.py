from pathlib import Path

path = Path("example_input.txt")
contents = path.read_text()
cards = contents.splitlines()

"""Each line within a map contains three numbers: the destination 
range start, the source range start, and the range length."""

