from aocparser import *

def solution1():
    max_cal = 0

    curr = []
    for line in read_input(1):
        if line == "\n":
            max_cal = max(max_cal, sum(curr))
            curr = []
        else:
            curr.append(int(line.strip("\n")))
    max_cal = max(max_cal, sum(curr))
    return max_cal

def solution2():
    full_list = []

    curr = []
    for line in read_input(1):
        if line == "\n":
            # Compare to max here
            full_list.append(sum(curr))
            curr = []
        else:
            curr.append(int(line.strip("\n")))
    full_list.append(sum(curr))


    full_list.sort(reverse=True)
    return sum(full_list[:3])

if __name__ == "__main__":
    print("Solution 1:", solution1())
    print("Solution 2:", solution2())