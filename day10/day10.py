import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from collections import defaultdict
from itertools import permutations
import re
from utils import AdventDay


class Day10(AdventDay):
    DAY = 10

    GROUP_REGEX = re.compile(r'(.)\1*')

    def look_and_say(self, inp):
        out = ''
        groups = [m.group(0) for m in self.GROUP_REGEX.finditer(inp)]
        for group in groups:
            out += str(len(group)) + group[0]
        return out

    def test(self):
        results = ['1', '11', '21', '1211', '111221', '312211']
        cur_val = self.get_test_input()[0]
        for i in range(6):
            assert cur_val == results[i], '{0} != {1}'.format(cur_val, results[i])
            cur_val = self.look_and_say(cur_val)
        return 'Passed!'

    def part1(self):
        cur_val = self.get_input()[0]
        for _ in range(40):
            cur_val = self.look_and_say(cur_val)
        self.part1_result = cur_val
        return len(cur_val)

    def part2(self):
        cur_val = self.part1_result
        for _ in range(10):
            cur_val = self.look_and_say(cur_val)
        return len(cur_val)


if __name__ == '__main__':
    Day10().run()
