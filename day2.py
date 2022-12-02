from aocparser import *

MOVES_DICT = {
    'A': 0,
    'B': 1,
    'C': 2,
    'X': 0,
    'Y': 1,
    'Z': 2
}

RES_DICT = {
    'X': 0,
    'Y': 3,
    'Z': 6
}

def game_result(opponent: str, me: str):
    onum = MOVES_DICT[opponent]
    menum = MOVES_DICT[me]

    if onum == menum: return 3
    if (onum + 1) % 3 == menum: return 6
    return 0
    
def solution1():
    total = 0
    for line in read_input(2):
        moves = line.strip("\n").split()
        opponent = moves[0]
        me = moves[1]
        # Add 1 for my indexing
        total += MOVES_DICT[me] + game_result(opponent, me) + 1
    return total

def solution2():
    total = 0
    for line in read_input(2):
        moves = line.strip("\n").split()
        opponent = MOVES_DICT[moves[0]]
        res = moves[1]

        if res == 'X':
            me = (opponent + 2) % 3
        elif res == 'Y':
            me = opponent
        elif res == 'Z':
            me = (opponent + 4) % 3
        else:
            raise ValueError
        # Add 1 for my indexing
        total += me + RES_DICT[res] + 1
    return total

if __name__ == "__main__":
    print("Solution 1:", solution1())
    print("Solution 2:", solution2())