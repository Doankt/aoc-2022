from aocparser import *

from math import sqrt

def point_dist(point_a, point_b):
    return sqrt((point_b[0] - point_a[0])**2 + (point_b[1] - point_a[1])**2)

class SnakeSolution:
    def __init__(self, tail_count: int = 1, test=False):
        self.start = [0, 0]
        self.snake = [[0,0] for _ in range(tail_count + 1)]
        
        self.tail_count = tail_count
        
        self.visited = set()
        self.visited.add((0, 0))

        self.test = test

    def do_step(self, direction):
        if direction == "R":
            self.snake[0][0] += 1
        elif direction == "L":
            self.snake[0][0] -= 1
        elif direction == "U":
            self.snake[0][1] += 1
        elif direction == "D":
            self.snake[0][1] -= 1
        else:
            raise ValueError

        for i in range(self.tail_count):
            if point_dist(self.snake[i], self.snake[i+1]) > sqrt(2):
                dx = self.snake[i][0] - self.snake[i+1][0]
                dy = self.snake[i][1] - self.snake[i+1][1]
                
                if dx:
                    self.snake[i+1][0] += 1 if dx > 0 else -1
                if dy:
                    self.snake[i+1][1] += 1 if dy > 0 else -1
                if i == self.tail_count - 1:
                    self.visited.add(tuple(self.snake[-1]))
            else:
                break
    
    def run(self):
        for line in read_input(9, self.test):
            direction, steps = line.strip("\n").split(" ")
            steps = int(steps)
            for _ in range(steps):
                self.do_step(direction)
        return len(self.visited)

def solution1():
    sol = SnakeSolution(tail_count= 1)
    return sol.run()

def solution2():
    sol = SnakeSolution(tail_count= 9)
    return sol.run()

if __name__ == "__main__":
    print("Solution 1:", solution1())
    print("Solution 2:", solution2())