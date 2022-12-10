from aocparser import *
FILE_SYS = dict()

def recur_file_sum(dir, size=0, dir_sum=0):
    curr_sum = 0
    dir_fn = 0
    for val in dir.values():
        if type(val) == dict:
            sz, df = recur_file_sum(val)
            curr_sum += sz
            dir_fn += df
        else:
            curr_sum += val
    if curr_sum <= 100000:
        return (size + curr_sum, dir_sum + curr_sum + dir_fn)
    return (size + curr_sum, dir_sum + dir_fn)

def get_dir_size(dir, size=0):
    curr_sum = 0
    for val in dir.values():
        if type(val) == dict:
            curr_sum += get_dir_size(val)
        else:
            curr_sum += val
    return size + curr_sum

def get_bigger_dirs(dir, min_size, size=0, dir_list=[]):
    curr_list = dir_list
    curr_sum = 0
    for val in dir.values():
        if type(val) == dict:
            sz, _ = get_bigger_dirs(val, min_size)
            curr_sum += sz
        else:
            curr_sum += val
    if curr_sum >= min_size:
        curr_list.append(curr_sum)
        return (size + curr_sum, curr_list)
    return (size + curr_sum, curr_list)

def load_system():
    with aoc_open(7) as file:
        working_dir = []
        line = file.readline()
        while line:
            if line.startswith("$"):
                cmd_line = line.strip("$").strip(" ").split()
                cmd = cmd_line[0]

                if cmd == "ls":
                    line = file.readline()
                    while line and not line.startswith("$"):
                        identifier, name = line.strip("\n").split()
                        if identifier == "dir":
                            working_dir[-1][name] = dict()
                        else:
                            working_dir[-1][name] = int(identifier)
                        line = file.readline()
                elif cmd == "cd":
                    next_dir = cmd_line[1]
                    if next_dir == "..":
                        working_dir.pop()
                    elif next_dir == "/":
                        working_dir = [FILE_SYS]
                    else:
                        working_dir.append(working_dir[-1][next_dir])
                    line = file.readline()
                else:
                    raise ValueError()

def solution1():
    return recur_file_sum(FILE_SYS)[1]

def solution2():
    total_size = get_dir_size(FILE_SYS)
    free = 70000000 - total_size
    needed = 30000000 - free
    _, res = get_bigger_dirs(FILE_SYS, needed)
    res.sort()
    return res[0]

if __name__ == "__main__":
    load_system()
    print("Solution 1:", solution1())
    print("Solution 2:", solution2())