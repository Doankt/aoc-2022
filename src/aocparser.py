def read_input(day_num: int):
    with open(f"inputs/day{day_num}.txt", "r") as f:
        for line in f:
            yield line

def get_input(day_num: int):
    with open(f"inputs/day{day_num}.txt", "r") as f:
        return f.readlines()