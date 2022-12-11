from aocparser import *
from itertools import accumulate
class Monkey:
    def __init__(self, sol_num, line_list) -> None:
        self.sol_num = sol_num
        self.id = int(line_list[0][:-1].split(" ")[-1])
        self.items = [int(i) for i in line_list[1].split(":")[1].split(", ")]
        self._operation = self._parse_op(line_list[2])

        test_val = int(line_list[3].split(" ")[-1])
        self._test = lambda x: True if x % test_val == 0 else False
        self._test_val = test_val

        self._to_path = (int(line_list[4].split(" ")[-1]), int(line_list[5].split(" ")[-1]))

        self.inspection_count = 0

    def _parse_op(self, op_line):
        op, op_val = op_line.split(" ")[-2:]
        if op == "+":
            if op_val == "old": return lambda x: x + x
            else:               return lambda x: x + int(op_val)
        elif op == "*":
            if op_val == "old": return lambda x: x * x
            else:               return lambda x: x * int(op_val)

    def inspect_front(self):
        item = self.items.pop(0)

        item = self._operation(item)
        
        if self.sol_num == 1:
            item = item // 3

        if self._test(item):
            dst = self._to_path[0]
        else:
            dst = self._to_path[1]
        self.inspection_count += 1
        return (dst, item)

    def inspect_all(self):
        send_to = []
        while self.items:
            send_to.append(self.inspect_front())
        return send_to

class MIMSolution:
    def __init__(self, sol_num, test=False) -> None:
        self.sol_num = sol_num
        self.mk_dict = dict()
        lines = get_input(11, test)
        
        # Make Monkeys
        i = 0
        while i < len(lines):
            m = Monkey(sol_num, [line.strip("\n") for line in lines[i:i+7] if line != "\n"])
            self.mk_dict[m.id] = m
            i += 7

        self._full_mul = list(accumulate([m._test_val for m in self.mk_dict.values()], lambda x, y: x* y))[-1]

    def _send_to_monkey(self, src, dst, item):
        if self.sol_num == 1:
            self.mk_dict[dst].items.append(item)
        else:
            self.mk_dict[dst].items.append(item % self._full_mul)

    def run(self, cycles):
        for _ in range(cycles):
            for id in sorted(list(self.mk_dict.keys())):
                res = self.mk_dict[id].inspect_all()
                for dst, item in res:
                    self._send_to_monkey(id, dst, item)

        inspection_count_list = sorted([monkey.inspection_count for monkey in self.mk_dict.values()])
        return inspection_count_list[-1] * inspection_count_list[-2]

def solution1():
    sol = MIMSolution(1)
    return sol.run(20)

def solution2():
    sol = MIMSolution(2)
    return sol.run(10000)

if __name__ == "__main__":
    print("Solution 1:", solution1())
    print("Solution 2:", solution2())