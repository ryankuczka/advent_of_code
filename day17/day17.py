import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

import itertools
from utils import AdventDay


class Day17(AdventDay):
    DAY = 17

    def part1(self):
        containers = map(int, self.get_input())
        self.valid = []
        for num in range(1, len(containers) + 1):
            for combo in itertools.combinations(containers, num):
                if sum(combo) == 150:
                    self.valid.append(combo)

        return len(self.valid)

    def part2(self):
        min_length = min(map(len, self.valid))
        return len(filter(lambda c: len(c) == min_length, self.valid))

if __name__ == '__main__':
    Day17().run()
