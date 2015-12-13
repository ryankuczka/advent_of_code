import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

import json
import re
from utils import AdventDay


class Day12(AdventDay):
    DAY = 12

    # Match 2 or more groups of double letters
    NUM_REGEX = re.compile(r'-?\d+')

    def add_values(self, obj):
        if isinstance(obj, dict):
            if self.ignore_red and 'red' in obj.values():
                return 0
            dict_sum = 0
            for i in obj.values():
                dict_sum += self.add_values(i)
            return dict_sum
        elif isinstance(obj, list):
            list_sum = 0
            for i in obj:
                list_sum += self.add_values(i)
            return list_sum
        elif isinstance(obj, int):
            return obj
        return 0

    def part1(self):
        self.ignore_red = False
        inp = json.loads(self.get_input()[0])
        return self.add_values(inp)

    def part2(self):
        self.ignore_red = True
        inp = json.loads(self.get_input()[0])
        return self.add_values(inp)


if __name__ == '__main__':
    Day12().run()
