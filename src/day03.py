from aocparser import *

from string import ascii_letters

PRIO_DICT = {char: val for val, char in enumerate(ascii_letters, 1)}

def solution1():
    total = 0
    for line in read_input(3):
        strip_line = line.strip("\n")
        line_size = len(strip_line)

        # Split backpack
        left = strip_line[:line_size//2]
        right = strip_line[line_size//2:]

        # Create set for left side
        lset = {c for c in left}

        # Intersect right
        lset.intersection_update(right)
        assert len(lset) == 1
        total += PRIO_DICT[lset.pop()]
    return total

def solution2():
    total = 0

    lines = [line.strip("\n") for line in get_input(3)]
    groups = []
    tgroup = []

    # Create groups of 3
    for i, line in enumerate(lines, 1):
        tgroup.append(line)
        if i % 3 == 0:
            groups.append(tgroup)
            tgroup = []
    del tgroup
    
    for group in groups:
        # Create first set
        base_set = {c for c in group[0]}

        # Intersect all other sets
        for sgroup in group[1:]:
            base_set.intersection_update(sgroup)
            
        assert len(base_set) == 1
        total += PRIO_DICT[base_set.pop()]

    return total

if __name__ == "__main__":
    print("Solution 1:", solution1())
    print("Solution 2:", solution2())