def _get_fstring(day_num, test=False):
    if test:    return f"inputs/day{day_num:02d}/day{day_num:02d}_test.txt"
    else:       return f"inputs/day{day_num:02d}/day{day_num:02d}.txt"

def read_input(day_num: int, test=False):
    fstring = _get_fstring(day_num, test)
    with open(fstring, "r") as f:
        for line in f:
            yield line

def get_input(day_num: int, test=False):
    fstring = _get_fstring(day_num, test)
    with open(fstring, "r") as f:
        return f.readlines()

def aoc_open(day_num, test=False):
    try:
        return open(_get_fstring(day_num, test), "r")
    except FileNotFoundError as e:
        if test:
            print(f"Test file for day {day_num:02d} not found.")
        else:
            print(f"Input file for day {day_num:02d} not found.")
    except Exception as e:
        exit(1)