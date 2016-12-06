import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

import re

from utils import AdventDay


class Day5(AdventDay):
    DAY = 5

    DOUBLE_LETTER_REGEX = re.compile(r'(.)\1')
    FORBIDDEN_REGEX = re.compile(r'ab|cd|pq|xy')

    DOUBLE_PAIR_REGEX = re.compile(r'(..).*\1')
    LETTER_SANDWICH_REGEX = re.compile(r'(.).\1')

    def nice_vowels(self, string):
        return sum(map(string.count, 'aeiou')) >= 3

    def nice_double(self, string):
        return self.DOUBLE_LETTER_REGEX.search(string)

    def nice_forbidden(self, string):
        return not self.FORBIDDEN_REGEX.search(string)

    def nice_double_pair(self, string):
        return self.DOUBLE_PAIR_REGEX.search(string)

    def nice_letter_sandwich(self, string):
        return self.LETTER_SANDWICH_REGEX.search(string)

    def part1(self):
        nice_count = 0
        for string in self.get_input():
            if self.nice_vowels(string) and self.nice_double(string) and \
                    self.nice_forbidden(string):
                nice_count += 1

        return nice_count

    def part2(self):
        nice_count = 0
        for string in self.get_input():
            if self.nice_double_pair(string) and \
                    self.nice_letter_sandwich(string):
                nice_count += 1

        return nice_count


if __name__ == '__main__':
    Day5().run()
