from aocparser import *
from collections import deque

class ElevationSolution:
    def __init__(self, sol_num, test=False) -> None:
        self.sol_num = sol_num
        self.test = test

        self.board = []
        self.start = (-1, -1)
        
        for i, line in enumerate(read_input(12, test)):
            board_builder = []
            for j, char in enumerate(line.strip("\n")):
                if char == "S":
                    self.start = (i, j)
                    board_builder.append(ord("a")-97)
                elif char == "E":
                    self.dest = (i, j)
                    board_builder.append(ord("z")-97)
                else:   board_builder.append(ord(char)-97)
            self.board.append(board_builder)

    def get_point_height(self, point):
        return self.board[point[0]][point[1]]

    def height_check_valid(self, start_point, new_point):
        if self.sol_num == 1:
            return self.get_point_height(new_point) <= self.get_point_height(start_point) + 1 
        else:
            return self.get_point_height(new_point) + 1 >= self.get_point_height(start_point)

    def find_valid_neighbors(self, point):
        nlist = []
        x, y, = point
        
        # Check up
        if x - 1 >= 0 and self.height_check_valid(point, (x-1, y)):
            nlist.append((x-1, y))
        # Check down
        if x + 1 < len(self.board) and self.height_check_valid(point, (x+1, y)):
            nlist.append((x+1, y))
        # Check left
        if y - 1 >= 0 and self.height_check_valid(point, (x, y-1)):
            nlist.append((x, y-1))
        # Check right
        if y + 1 < len(self.board[0]) and self.height_check_valid(point, (x, y+1)):
            nlist.append((x, y+1))
        
        return nlist

    def path_reached_dst(self, path):
        return path and path[-1] == self.dest

    def shortest_dist_to_goal(self) -> int:
        if self.start == self.dest: return 0

        q = deque()
        q.append((0,self.start[0], self.start[1]))
        visited = set(self.start)

        while q:
            distance, row, col = q.popleft()
            neighbors = self.find_valid_neighbors((row, col))
            for neighbor in neighbors:
                if neighbor == self.dest:
                    return distance + 1
                if neighbor not in visited:
                    q.append((distance+1, neighbor[0], neighbor[1]))

                visited.add(neighbor)
        # No path to goal
        return -1

    def find_best_start(self):
        q = deque()
        # Start at end
        q.append((0,self.dest[0], self.dest[1]))
        visited = set(self.dest)

        while q:
            distance, row, col = q.popleft()
            neighbors = self.find_valid_neighbors((row, col))
            for neighbor in neighbors:
                if self.get_point_height(neighbor) == 0:
                    return distance + 1
                if neighbor not in visited:
                    q.append((distance+1, neighbor[0], neighbor[1]))
                visited.add(neighbor)
        # No path to goal
        return -1

    def run(self):
        if self.sol_num == 1:
            return self.shortest_dist_to_goal()
        else:
            return self.find_best_start()

def solution1():
    sol = ElevationSolution(1)
    return sol.run()

def solution2():
    sol = ElevationSolution(2)
    return sol.run()

if __name__ == "__main__":
    print("Solution 1:", solution1())
    print("Solution 2:", solution2())
    