from aocparser import *

import functools as ft

class PacketSolution:
    def __init__(self, sol_num, test=False) -> None:
        self.sol_num = sol_num
        self.test = test

        self.pairs = []
        pair_builder = []
        for line in read_input(13, test):
            if line.strip("\n"):
                pair_builder.append(eval(line.strip("\n")))
            else:
                self.pairs.append(tuple(pair_builder))
                pair_builder = []
        self.pairs.append(tuple(pair_builder))

    def list_compare(self, left, right):
        if not left and not right:  return True
        if not left:
            return -1 if right else 1
        if not right:
            return 1 if left else -1
        
        fl, fr = left[0], right[0]

        # Filter by comparison
        if isinstance(fl, int) and isinstance(fr, int):
            # int on both sides
            if fl == fr:
                res = True
            else:
                res = fl - fr
        elif isinstance(fl, int) and not isinstance(fr, int):
            # int on left, list on right
            res = self.list_compare([fl], fr)
        elif not isinstance(fl, int) and isinstance(fr, int):
            # list on right, int on left
            res = self.list_compare(fl, [fr])
        else:
            # list on both sides
            res = self.list_compare(fl, fr)

        # Check results
        if res:
            if type(res) == int:    return res
            return self.list_compare(left[1:], right[1:])
        else:   return False

    def run(self):
        if self.sol_num == 1:
            ret = 0
            
            for i in range(1, len(self.pairs) + 1):
                l, r = self.pairs[i-1]
                if self.list_compare(l, r) < 0:
                    ret += i
            return ret
        else:
            divider_packets = [[[2]], [[6]]]
            res = 1
            packets = divider_packets[:]
            for pair in self.pairs:
                packets.append(pair[0])
                packets.append(pair[1])

            packets.sort(key=ft.cmp_to_key(self.list_compare))
            for i, packet in enumerate(packets, 1):
                if packet in divider_packets:
                    res *= i
            return res
            
def solution1():
    sol = PacketSolution(1)
    return sol.run()

def solution2():
    sol = PacketSolution(2)
    return sol.run()

if __name__ == "__main__":
    print("Solution 1:", solution1())
    print("Solution 2:", solution2())