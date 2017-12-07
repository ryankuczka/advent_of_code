import os
import sys
import time
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from utils import AdventDay


class Day1(AdventDay):
    DAY = 1

    DIRECTIONS = ['N', 'E', 'S', 'W']

    def get_distance(self, directions):
        current_dir_idx = 0
        current_x = 0
        current_y = 0

        for direction in directions:
            turn, distance = direction[0], int(direction[1:])
            if turn == 'L':
                current_dir_idx = (current_dir_idx - 1) % 4
            else:
                current_dir_idx = (current_dir_idx + 1) % 4

            current_dir = self.DIRECTIONS[current_dir_idx]
            if current_dir == 'N':
                current_y += distance
            elif current_dir == 'E':
                current_x += distance
            elif current_dir == 'S':
                current_y -= distance
            elif current_dir == 'W':
                current_x -= distance

        return abs(current_x) + abs(current_y)

    def test(self):
        inp = self.get_test_input()[0]
        directions = [d.strip() for d in inp.split(',')]
        return self.get_distance(directions)

    def part1(self):
        inp = self.get_input()[0]
        directions = [d.strip() for d in inp.split(',')]
        return self.get_distance(directions)

    def part2(self):
        inp = self.get_input()[0]
        directions = [d.strip() for d in inp.split(',')]

        visited = set()

        current_dir_idx = 0
        current_loc = 0, 0

        visited.add(current_loc)

        for direction in directions:
            turn, distance = direction[0], int(direction[1:])
            if turn == 'L':
                current_dir_idx = (current_dir_idx - 1) % 4
            else:
                current_dir_idx = (current_dir_idx + 1) % 4

            current_dir = self.DIRECTIONS[current_dir_idx]
            for i in range(distance):
                if current_dir == 'N':
                    current_loc = current_loc[0], current_loc[1] + 1
                elif current_dir == 'E':
                    current_loc = current_loc[0] + 1, current_loc[1]
                elif current_dir == 'S':
                    current_loc = current_loc[0], current_loc[1] - 1
                elif current_dir == 'W':
                    current_loc = current_loc[0] - 1, current_loc[1]

                if current_loc in visited:
                    return sum(map(abs, current_loc))

                visited.add(current_loc)


if __name__ == '__main__':
    Day1().run()
