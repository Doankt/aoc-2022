from aocparser import *
import re

def load_stacks():
    with open("inputs/day5.txt", "r") as file:
        lines = []
        line = file.readline().strip("\n")
        while line:
            lines.append(line)
            line = file.readline().strip("\n")

    # Reverse lines for parsing
    lines.reverse()
    
    # Find number of stacks
    num_stacks = [int(n) for n in lines[0].split(" ") if n][-1]
    stacks = []
    for _ in range(num_stacks): stacks.append([])

    # Loop for chars
    for line in lines[1:]:
        for i in range(num_stacks):
            # Each char group is len 3
            char = line[(4*i)+1]
            if char != " ":
                stacks[i].append(char)
    return stacks

def load_moves():
    lines = []
    with open("inputs/day5.txt", "r") as file:
        # Skip through stacks
        while (file.readline().strip("\n")):    pass

        # Start reading moves
        line = file.readline().strip("\n")
        while line:
            lines.append(line)
            line = file.readline().strip("\n")
    return lines

MOVE_REGEX = "move (?P<num_moved>[0-9]{0,}) from (?P<start_stack>[0-9]{0,}) to (?P<end_stack>[0-9]{0,})"
def read_move(line: str) -> (int):
    res = re.search(MOVE_REGEX, line)
    return(
        (
            int(res.group("num_moved")),
            int(res.group("start_stack")) - 1,
            int(res.group("end_stack")) - 1
        )
    )

def do_move(stacks, move, multi=False):
    num_moved, start_stack, end_stack = read_move(move)
    start_stack = stacks[start_stack]
    end_stack = stacks[end_stack]

    if not multi:
        for _ in range(num_moved):
            n = start_stack.pop()
            end_stack.append(n)
    else:
        temp_move = start_stack[-num_moved:]
        for _ in range(num_moved):
            start_stack.pop()
        end_stack.extend(temp_move)

def solution1():
    stacks = load_stacks()
    moves = load_moves()
    for move in moves:
        do_move(stacks, move, False)
    return "".join(s[-1] for s in stacks)

def solution2():
    stacks = load_stacks()
    moves = load_moves()
    for move in moves:
        do_move(stacks, move, True)

    return "".join(s[-1] for s in stacks)

if __name__ == "__main__":
    print("Solution 1:", solution1())
    print("Solution 2:", solution2())