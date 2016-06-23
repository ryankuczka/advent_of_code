import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from pprint import pprint
from utils import AdventDay


class Day25(AdventDay):
    DAY = 25

    def build_grid(self):
        current = 20151125
        self.grid = [[]]
        row = 0
        while True:
            self.grid[row].append(current)
            row -= 1
            current = (current * 252533) % 33554393
            if row == -1:
                self.grid.append([])
                row = len(self.grid) - 1

            try:
                return self.grid[2980][3074]
            except IndexError:
                pass

    def part1(self):
        return self.build_grid()

    def part2(self):
        pass


if __name__ == '__main__':
    Day25().run()
