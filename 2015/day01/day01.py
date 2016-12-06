import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from utils import AdventDay


class Day1(AdventDay):
    DAY = 1

    def part1(self):
        inp = self.get_input()[0]
        return inp.count('(') - inp.count(')')

    def part2(self):
        inp = self.get_input()[0]
        cur_floor = 0
        for index, instr in enumerate(inp):
            cur_floor += 1 if instr == '(' else -1
            if cur_floor == -1:
                return index + 1


if __name__ == '__main__':
    Day1().run()
