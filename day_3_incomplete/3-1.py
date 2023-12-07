from pathlib import Path

path = Path("input.txt")
contents = path.read_text()
lines = contents.splitlines()

schematic = []

for line in lines:
    line = line.strip()
    schematic.append(line)

print(schematic)

final_list = []

symbols = ['#', '$', '%', '&', '*', '+', '-', '/', '=', '@']

# This is disgusting im very sorry
# I cannot stress how un proud of this i am
def find_symbols(schematic, symbols):
    sum = 0
    for line_index, line in enumerate(schematic):
        # print(line_index, line)
        for index, x in enumerate(line):
            if x in symbols:
                #horizontally adjacent 
                if line[index - 1].isdigit():
                    if line[index - 3].isdigit() and line[index - 2].isdigit():
                        print(int(f"{line[index - 3]}{line[index - 2]}{line[index - 1]}"))
                        sum += int(f"{line[index - 3]}{line[index - 2]}{line[index - 1]}")
                    elif line[index - 2].isdigit():
                        print(int(f"{line[index - 2]}{line[index - 1]}"))
                        sum += int(f"{line[index - 2]}{line[index - 1]}")
                    else:
                        sum += int(f"{line[index - 1]}")
                if line[index + 1].isdigit():
                    if line[index + 3].isdigit() and line[index + 2].isdigit():
                        print(int(f"{line[index + 3]}{line[index + 2]}{line[index + 1]}"))
                        sum += int(f"{line[index + 3]}{line[index + 2]}{line[index + 1]}")
                    elif line[index + 2].isdigit():
                        print(int(f"{line[index + 2]}{line[index + 1]}"))
                        sum += int(f"{line[index + 2]}{line[index + 1]}")
                    else:
                        print(int(f"{line[index + 1]}"))
                        sum += int(f"{line[index + 1]}")
                # Deal with above and below separately from diagonals to avoid numbers being counted twice
                if schematic[line_index - 1][index].isdigit() or schematic[line_index + 1][index].isdigit():
                    #Directly above
                    if schematic[line_index - 1][index].isdigit():
                        #Three digit number with index in centre
                        if schematic[line_index - 1][index - 1].isdigit() and schematic[line_index - 1][index + 1].isdigit():
                            print(int(f"{schematic[line_index - 1][index - 1]}{schematic[line_index - 1][index]}{schematic[line_index - 1][index + 1]}"))
                            sum += int(f"{schematic[line_index - 1][index - 1]}{schematic[line_index - 1][index]}{schematic[line_index - 1][index + 1]}")
                        #Three digit number with index far right
                        elif schematic[line_index - 1][index - 2].isdigit() and schematic[line_index - 1][index - 1].isdigit():
                            print(int(f"{schematic[line_index - 1][index - 2]}{schematic[line_index - 1][index - 1]}{schematic[line_index - 1][index]}"))
                            sum += int(f"{schematic[line_index - 1][index - 2]}{schematic[line_index - 1][index - 1]}{schematic[line_index - 1][index]}")
                        #Three digit number with index far left
                        elif schematic[line_index - 1][index + 2].isdigit() and schematic[line_index - 1][index + 1].isdigit():
                            print(int(f"{schematic[line_index - 1][index]}{schematic[line_index - 1][index + 1]}{schematic[line_index - 1][index + 2]}"))
                            sum += int(f"{schematic[line_index - 1][index]}{schematic[line_index - 1][index + 1]}{schematic[line_index - 1][index + 2]}")
                        #Two digit number with index on right
                        elif schematic[line_index - 1][index - 1].isdigit():
                            print(int(f"{schematic[line_index - 1][index - 1]}{schematic[line_index - 1][index]}"))
                            sum += int(f"{schematic[line_index - 1][index - 1]}{schematic[line_index - 1][index]}")
                        #Two digit number with index on left
                        elif schematic[line_index - 1][index + 1].isdigit():
                            print(int(f"{schematic[line_index - 1][index]}{schematic[line_index - 1][index + 1]}"))
                            sum += int(f"{schematic[line_index - 1][index]}{schematic[line_index - 1][index + 1]}")
                        else:
                            #One digit number
                            print(int(f"{schematic[line_index - 1][index]}"))
                            sum += int(f"{schematic[line_index - 1][index]}")
                    #Directly below
                    if schematic[line_index + 1][index].isdigit():
                        #Three digit number with index in centre
                        if schematic[line_index + 1][index - 1].isdigit() and schematic[line_index + 1][index + 1].isdigit():
                            print(int(f"{schematic[line_index + 1][index - 1]}{schematic[line_index + 1][index]}{schematic[line_index + 1][index + 1]}"))
                            sum += int(f"{schematic[line_index + 1][index - 1]}{schematic[line_index + 1][index]}{schematic[line_index + 1][index + 1]}")
                        #Three digit number with index far right
                        elif schematic[line_index + 1][index - 2].isdigit() and schematic[line_index + 1][index - 1].isdigit():
                            print(int(f"{schematic[line_index + 1][index - 2]}{schematic[line_index + 1][index - 1]}{schematic[line_index + 1][index]}"))
                            sum += int(f"{schematic[line_index + 1][index - 2]}{schematic[line_index + 1][index - 1]}{schematic[line_index + 1][index]}")
                        #Three digit number with index far left
                        elif schematic[line_index + 1][index + 2].isdigit() and schematic[line_index + 1][index + 1].isdigit():
                            print(int(f"{schematic[line_index + 1][index]}{schematic[line_index + 1][index + 1]}{schematic[line_index + 1][index + 2]}"))
                            sum += int(f"{schematic[line_index + 1][index]}{schematic[line_index + 1][index + 1]}{schematic[line_index + 1][index + 2]}")
                        #Two digit number with index on right
                        elif schematic[line_index + 1][index - 1].isdigit():
                            print(int(f"{schematic[line_index + 1][index - 1]}{schematic[line_index + 1][index]}"))
                            sum += int(f"{schematic[line_index + 1][index - 1]}{schematic[line_index + 1][index]}")
                        #Two digit number with index on left
                        elif schematic[line_index + 1][index + 1].isdigit():
                            print(int(f"{schematic[line_index + 1][index]}{schematic[line_index + 1][index + 1]}"))
                            sum += int(f"{schematic[line_index + 1][index]}{schematic[line_index + 1][index + 1]}")
                        #One digit number
                        else:
                            print(int(f"{schematic[line_index + 1][index]}"))
                            sum += int(f"{schematic[line_index + 1][index]}")
                # Deal with diaginals in an else block so that numbers aren't counted twice
                # also don't have to deal with any number that would have a digit directly above
                # or below the symbol as that will have already been counted
                if not schematic[line_index - 1][index].isdigit():
                    #diagonally left above
                    if schematic[line_index - 1][index - 1].isdigit() and not schematic[line_index - 1][index].isdigit():
                        #Three digit number with index far right
                        if schematic[line_index - 1][index - 3].isdigit() and schematic[line_index - 1][index - 2].isdigit():
                            print(int(f"{schematic[line_index - 1][index - 3]}{schematic[line_index - 1][index - 2]}{schematic[line_index - 1][index - 1]}"))
                            sum += int(f"{schematic[line_index - 1][index - 3]}{schematic[line_index - 1][index - 2]}{schematic[line_index - 1][index - 1]}")
                        #Two digit number with index on right
                        elif schematic[line_index - 1][index - 2].isdigit():
                            print(int(f"{schematic[line_index - 1][index - 2]}{schematic[line_index - 1][index - 1]}"))
                            sum += int(f"{schematic[line_index - 1][index - 2]}{schematic[line_index - 1][index - 1]}")
                        else:
                            #One digit number
                            print(int(f"{schematic[line_index - 1][index - 1]}"))
                            sum += int(f"{schematic[line_index - 1][index - 1]}")
                    # diagonally left below
                    if schematic[line_index + 1][index - 1].isdigit() and not schematic[line_index + 1][index].isdigit():
                        #Three digit number with index far right
                        if schematic[line_index + 1][index - 3].isdigit() and schematic[line_index + 1][index - 2].isdigit():
                            print(int(f"{schematic[line_index + 1][index - 3]}{schematic[line_index + 1][index - 2]}{schematic[line_index + 1][index - 1]}"))
                            sum += int(f"{schematic[line_index + 1][index - 3]}{schematic[line_index + 1][index - 2]}{schematic[line_index + 1][index - 1]}")
                        #Two digit number with index on right
                        elif schematic[line_index + 1][index - 2].isdigit():
                            print(int(f"{schematic[line_index + 1][index - 2]}{schematic[line_index + 1][index - 1]}"))
                            sum += int(f"{schematic[line_index + 1][index - 2]}{schematic[line_index + 1][index - 1]}")
                        else:
                            #One digit number
                            print(int(f"{schematic[line_index + 1][index - 1]}"))
                            sum += int(f"{schematic[line_index + 1][index - 1]}")
                    # diagonally right above
                    if schematic[line_index - 1][index + 1].isdigit() and not schematic[line_index - 1][index].isdigit():
                        #Three digit number with index far left
                        if schematic[line_index - 1][index + 3].isdigit() and schematic[line_index - 1][index + 2].isdigit():
                            print(int(f"{schematic[line_index - 1][index + 1]}{schematic[line_index - 1][index + 2]}{schematic[line_index - 1][index + 3]}"))
                            sum += int(f"{schematic[line_index - 1][index + 1]}{schematic[line_index - 1][index + 2]}{schematic[line_index - 1][index + 3]}")
                        #Two digit number with index on left
                        elif schematic[line_index - 1][index + 2].isdigit():
                            print(int(f"{schematic[line_index - 1][index + 1]}{schematic[line_index - 1][index + 2]}"))
                            sum += int(f"{schematic[line_index - 1][index + 1]}{schematic[line_index - 1][index + 2]}")
                        else:
                            #One digit number
                            print(int(f"{schematic[line_index - 1][index + 1]}"))
                            sum += int(f"{schematic[line_index - 1][index + 1]}")
                    # diagonally right below
                    if schematic[line_index + 1][index + 1].isdigit() and not schematic[line_index + 1][index].isdigit():
                        #Three digit number with index far left
                        if schematic[line_index + 1][index + 3].isdigit() and schematic[line_index + 1][index + 2].isdigit():
                            print(int(f"{schematic[line_index + 1][index + 1]}{schematic[line_index + 1][index + 2]}{schematic[line_index + 1][index + 3]}"))
                            sum += int(f"{schematic[line_index + 1][index + 1]}{schematic[line_index + 1][index + 2]}{schematic[line_index + 1][index + 3]}")
                        #Two digit number with index on left
                        elif schematic[line_index + 1][index + 2].isdigit():
                            print(int(f"{schematic[line_index + 1][index + 1]}{schematic[line_index + 1][index + 2]}"))
                            sum += int(f"{schematic[line_index + 1][index + 1]}{schematic[line_index + 1][index + 2]}")
                        else:
                            #One digit number
                            print(int(f"{schematic[line_index + 1][index + 1]}"))
                            sum += int(f"{schematic[line_index + 1][index + 1]}")
    return sum
                

print(find_symbols(schematic, symbols))