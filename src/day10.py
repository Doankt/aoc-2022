from aocparser import *

class CycleSolution1:
    def __init__(self, cycle_checks, test=False):
        self.test = test
        self.x_reg = 1
        self.cycle = 0
        self.cycle_checks = cycle_checks
        self.cycle_checkpoints = []

    def parse_line(self, line):
        if len(line.strip("\n").split(" ")) == 1:
            cmd = line.strip("\n")
            return (cmd, None)
        else:
            cmd, val = line.strip("\n").split(" ")
            return (cmd, int(val))
    
    def cycle_check(self):
        if self.cycle in self.cycle_checks:
            self.cycle_checkpoints.append(self.cycle * self.x_reg)

    def do_cmd(self, cmd, val):
        if cmd == "noop":
            self.cycle += 1
            self.cycle_check()
        elif cmd == "addx":
            for _ in range(2):
                self.cycle += 1
                self.cycle_check()
            self.x_reg += val
        else:
            raise ValueError

    def run(self):
        for line in read_input(10, self.test):
            cmd, val = self.parse_line(line)
            self.do_cmd(cmd, val)
        return sum(self.cycle_checkpoints)

class CycleSolution2:
    def __init__(self, cycle_checks, test=False):
        self.test = test

        self.x_reg = 1
        self.cycle = 0

        self.cycle_checks = cycle_checks
        self.crt = ["."]*cycle_checks[-1]

    def print_crt(self):
        print("".join(self.crt[:self.cycle_checks[0]]))
        for i in range(len(self.cycle_checks) - 1):
            print("".join(self.crt[self.cycle_checks[i]:self.cycle_checks[i+1]]))

    def parse_line(self, line):
        if len(line.strip("\n").split(" ")) == 1:
            cmd = line.strip("\n")
            return (cmd, None)
        else:
            cmd, val = line.strip("\n").split(" ")
            return (cmd, int(val))
    
    def cycle_check(self):
        if self.x_reg-1 <= ((self.cycle-1) % 40)  <= self.x_reg+1:
            self.crt[self.cycle-1] = "#"

    def do_cmd(self, cmd, val):
        if cmd == "noop":
            self.cycle += 1
            self.cycle_check()
        elif cmd == "addx":
            for _ in range(2):
                self.cycle += 1
                self.cycle_check()
            self.x_reg += val
        else:
            raise ValueError

    def run(self):
        for line in read_input(10, self.test):
            cmd, val = self.parse_line(line)
            self.do_cmd(cmd, val)

def solution1():
    sol = CycleSolution1([n for n in range(20, 220 + 1, 40)])
    return sol.run()

def solution2():
    sol = CycleSolution2([n for n in range(40, 240 + 1, 40)])
    sol.run()
    sol.print_crt()

if __name__ == "__main__":
    print("Solution 1:", solution1())
    print("Solution 2:")
    solution2()