import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

import re
from utils import AdventDay


class Day8(AdventDay):
    DAY = 8

    DELIM_REGEX = re.compile('^"|"$')
    ESCAPE_REGEX = re.compile(r'\\(\\|")')
    HEX_REGEX = re.compile(r'\\x.{2}')

    def part1(self):
        code_strings = self.get_input()
        actual_strings = []
        for code in code_strings:
            actual = self.DELIM_REGEX.sub('', code)
            actual = self.ESCAPE_REGEX.sub('X', actual)
            actual = self.HEX_REGEX.sub('X', actual)
            actual_strings.append(actual)

        code_len = sum(map(len, code_strings))
        actual_len = sum(map(len, actual_strings))
        return code_len - actual_len

    def part2(self):
        code_strings = self.get_input()
        encoded_strings = []
        for code in code_strings:
            encoded = self.DELIM_REGEX.sub('XXX', code)
            encoded = self.ESCAPE_REGEX.sub('XXXX', encoded)
            encoded = self.HEX_REGEX.sub('XXXXX', encoded)
            encoded_strings.append(encoded)

        code_len = sum(map(len, code_strings))
        encoded_len = sum(map(len, encoded_strings))
        return encoded_len - code_len


if __name__ == '__main__':
    Day8().run()
