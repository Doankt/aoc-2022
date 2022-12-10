def read_input(day_num: int, test=False):
    if test:    fstring = f"inputs/day{day_num}/day{day_num}_test.txt"
    else:       fstring = f"inputs/day{day_num}/day{day_num}.txt"

    with open(fstring, "r") as f:
        for line in f:
            yield line

def get_input(day_num: int, test=False):
    if test:    fstring = f"inputs/day{day_num}/day{day_num}_test.txt"
    else:       fstring = f"inputs/day{day_num}/day{day_num}.txt"
        
    with open(fstring, "r") as f:
        return f.readlines()

def aoc_open(day_num, test=False):
    try:
        if test:    return open(f"inputs/day{day_num}/day{day_num}_test.txt", "r")
        else:       return open(f"inputs/day{day_num}/day{day_num}.txt", "r")
    except FileNotFoundError as e:
        if test:
            print(f"Test file for day {day_num} not found.")
        else:
            print(f"Input file for day {day_num} not found.")
    finally:
        exit(1)