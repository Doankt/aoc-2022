from aocparser import *
BOARD = []

def load_board():
    for line in read_input(8):
        BOARD.append([int(c) for c in line.strip("\n")])

def check_visible(arr:list):
    found_indexes = set()
    max = -1
    for i, num in enumerate(arr):
        if num > max:
            max = num
            found_indexes.add(i)

    max = -1
    for i, num in enumerate(arr[::-1]):
        if num > max:
            max = num
            found_indexes.add(len(arr)-i-1)
    return found_indexes

def direction_score(point_height, arr):
    score = 0
    for num in arr:
        score += 1
        if point_height <= num:
            break
    return score

def solution1():
    col_count = len(BOARD[0])
    found_indexes = set()
    
    # Iter over Rows
    for i, row in enumerate(BOARD):
        res = check_visible(row)
        for res_index in res:
            found_indexes.add((i, res_index))

    # Iter over Cols
    for j in range(col_count):
        res = check_visible([row[j] for row in BOARD])
        for res_index in res:
            found_indexes.add((res_index, j))
    return len(found_indexes)

def solution2():
    row_count = len(BOARD)
    col_count = len(BOARD[0])

    max_score = 0
    for row in range(1, row_count-1):
        for col in range(1, col_count-1):
            score = 1
            point_height = BOARD[row][col]
            
            # Check right
            score *= direction_score(point_height, BOARD[row][col+1:])
            # Check left
            score *= direction_score(point_height, BOARD[row][col-1::-1])
            # Check down
            score *= direction_score(point_height, [row[col] for row in BOARD[row+1:]])
            # Check up
            score *= direction_score(point_height, [row[col] for row in BOARD[row-1::-1]])
            if score >= max_score:
                max_score = score
    return max_score

if __name__ == "__main__":
    load_board()
    print("Solution 1:", solution1())
    print("Solution 2:", solution2())