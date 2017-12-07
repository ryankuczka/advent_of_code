from itertools import chain, islice
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from utils import AdventDay


class Day3(AdventDay):
    DAY = 3

    def part1(self):
        inp = self.get_input()
        possible = 0
        for shape in inp:
            x, y, z = map(int, shape.split())

            if x + y <= z or x + z <= y or y + z <= x:
                continue

            possible += 1

        return possible

    def part2(self):
        inp = self.get_input()
        possible = 0
        rows = [map(int, row.split()) for row in inp]
        cols = list(chain.from_iterable(zip(*rows)))
        shapes = [cols[i:i + 3] for i in range(0, len(cols), 3)]
        for x, y, z in shapes:
            if x + y <= z or x + z <= y or y + z <= x:
                continue
            possible += 1

        return possible


if __name__ == '__main__':
    Day3().run()
