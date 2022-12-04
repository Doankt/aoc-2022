from aocparser import *

def solution1():
    total = 0
    for line in read_input(4):
        left, right = [l.split("-") for l in line.strip("\n").split(",")]
        left = {i for i in range(int(left[0]), int(left[1]) + 1)}
        right = {i for i in range(int(right[0]), int(right[1]) + 1)}

        if left.issubset(right) or right.issubset(left):
            total += 1
    return total

def solution2():
    total = 0
    for line in read_input(4):
        left, right = [l.split("-") for l in line.strip("\n").split(",")]
        left = {i for i in range(int(left[0]), int(left[1]) + 1)}
        right = {i for i in range(int(right[0]), int(right[1]) + 1)}

        if len(left.intersection(right)) >= 1:
            total += 1
    return total

if __name__ == "__main__":
    print("Solution 1:", solution1())
    print("Solution 2:", solution2())