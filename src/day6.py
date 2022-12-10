from aocparser import *

def find_window(window_size: int):
    with aoc_open(6) as file:
        data = file.read()
    shift = 0
    while shift <= len(data) - window_size:
        window = data[shift:shift+window_size]

        if len(set(window)) == window_size:
            return shift + window_size
        shift += 1

def solution1():
    return find_window(4)

def solution2():
    return find_window(14)

if __name__ == "__main__":
    print("Solution 1:", solution1())
    print("Solution 2:", solution2())