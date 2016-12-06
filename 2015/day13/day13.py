import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from collections import defaultdict
import itertools
import re
from utils import AdventDay


class Day13(AdventDay):
    DAY = 13

    LINE_REGEX = re.compile(r'^([A-GM]\w+) would (gain|lose) (\d+) happiness units by sitting next to ([A-GM]\w+)\.')
    TEST_NAMES = ['Alice', 'Bob', 'Carol', 'David']
    NAMES = ['Alice', 'Bob', 'Carol', 'David', 'Eric', 'Frank', 'George', 'Mallory']

    def parse_input(self, test=False):
        self.happiness = defaultdict(dict)
        inp = self.get_test_input() if test else self.get_input()
        for line in inp:
            name1, direction, diff, name2 = self.LINE_REGEX.match(line).groups()
            if direction == 'gain':
                diff = int(diff)
            else:
                diff = -1 * int(diff)
            self.happiness[name1][name2] = diff

    def get_happiness(self, names):
        happiness = 0
        for i in range(len(names)):
            name1 = names[i]
            name2 = names[(i + 1) % len(names)]
            happiness += self.happiness[name1][name2]
            happiness += self.happiness[name2][name1]
        return happiness

    def test(self):
        self.parse_input(test=True)
        return max(self.get_happiness(perm) for perm in itertools.permutations(self.TEST_NAMES))

    def part1(self):
        self.parse_input()
        return max(self.get_happiness(perm) for perm in itertools.permutations(self.NAMES))

    def part2(self):
        self.parse_input()
        for name in self.NAMES:
            self.happiness['Me'][name] = 0
            self.happiness[name]['Me'] = 0
        return max(self.get_happiness(perm) for perm in itertools.permutations(self.NAMES + ['Me']))


if __name__ == '__main__':
    Day13().run()
