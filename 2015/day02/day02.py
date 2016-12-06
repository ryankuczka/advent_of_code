import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from utils import AdventDay


class Day2(AdventDay):
    DAY = 2

    def part1(self):
        area = 0
        for present in self.get_input():
            x, y, z = map(int, present.split('x'))
            sides = [x * y, x * z, y * z]
            area += sum(2 * s for s in sides)
            area += min(sides)
        return area

    def part2(self):
        ribbon = 0
        for present in self.get_input():
            sides = map(int, present.split('x'))
            short_sides = sorted(sides)[:2]
            ribbon += sum(2 * s for s in short_sides)
            ribbon += sides[0] * sides[1] * sides[2]
        return ribbon


if __name__ == '__main__':
    Day2().run()
