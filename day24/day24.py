import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

import itertools
import operator
from utils import AdventDay


class Day24(AdventDay):
    DAY = 24

    def part1(self):
        nums = map(int, self.get_input())
        group_sum = sum(nums) / 3

        for group_size in range(len(nums)):
            possible_qes = [reduce(operator.mul, group) for group in itertools.combinations(nums, group_size) if sum(group) == group_sum]
            if possible_qes:
                return min(possible_qes)

    def part2(self):
        nums = map(int, self.get_input())
        group_sum = sum(nums) / 4

        for group_size in range(len(nums)):
            possible_qes = [reduce(operator.mul, group) for group in itertools.combinations(nums, group_size) if sum(group) == group_sum]
            if possible_qes:
                return min(possible_qes)


if __name__ == '__main__':
    Day24().run()
