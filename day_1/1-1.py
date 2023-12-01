"""The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

Consider your entire calibration document. What is the sum of all of the calibration values?"""

from pathlib import Path

path = Path("1-1_puzzle_input.txt")

contents = path.read_text().rstrip()
words_numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def convert_to_digits(text, number_dict):
    output = ""
    for line in text.splitlines():
        test_line = ""
        x = 0
        while x < len(line):
            test_line += line[x]
            for word in words_numbers:
                if word in test_line:
                    line = line.replace(word, word + word[len(word) - 1])
                    line = line.replace(word, number_dict[word])
                    test_line = ""
                    break
            x += 1
        output += f"{line}\n"
    return output

def convert_to_digits_loop(input, number_dict):
    """not proud of this at all..."""
    for x in range(1, 5):
        input = convert_to_digits(input, number_dict)
    return input
    
    
def find_first_digits(text):
    first_digits = []
    for line in text.splitlines():
        for x in line:
            if x.isdigit():
                first_digits.append(int(x))
                break
    return first_digits

def find_last_digits(text):
    last_digits = []
    for line in text.splitlines():
        line = line[::-1]
        for x in line:
            if x.isdigit():
                last_digits.append(int(x))
                break
    return last_digits

def zip_digits(first, last):
    zip_list = [f"{x[0]}{x[1]}" for x in zip(first, last)]
    return zip_list

result = convert_to_digits_loop(contents, words_numbers)

print(result)

first_digits = find_first_digits(result)
last_digits = find_last_digits(result)

list = zip_digits(first_digits, last_digits)

final_list = []

for x in list:
    final_list.append(int(x))

total = sum(final_list)

print(total)

