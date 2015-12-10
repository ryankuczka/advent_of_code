import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

import re
from utils import AdventDay


class Day7(AdventDay):
    DAY = 7

    LINE_REGEX = re.compile(r'(.*) -> (.*)')
    NOT_REGEX = re.compile('NOT ([a-z]{1,2})')
    SHIFT_REGEX = re.compile('([a-z]{1,2}) [LR]SHIFT ([0-9]+)')
    OR_REGEX = re.compile('([a-z]{1,2}) OR ([a-z]{1,2})')
    AND_REGEX = re.compile('([a-z0-9]+) AND ([a-z]{1,2})')
    NUM_REGEX = re.compile('\d+')
    WIRE_REGEX = re.compile('[a-z]{1,2}')

    def get_instructions(self):
        self.instructions = {}
        for line in self.get_input():
            instr, dest = self.LINE_REGEX.match(line).groups()
            self.instructions[dest] = instr

    def get_value(self, key):
        instr = self.instructions[key]

        # Short-circuit if we've already done this key
        if isinstance(instr, int):
            return instr

        if 'NOT' in instr:
            inner_key, = self.NOT_REGEX.match(instr).groups()
            self.instructions[key] = 65535 ^ self.get_value(inner_key)

        elif 'LSHIFT' in instr:
            inner_key, amnt = self.SHIFT_REGEX.match(instr).groups()
            self.instructions[key] = self.get_value(inner_key) << int(amnt)

        elif 'RSHIFT' in instr:
            inner_key, amnt = self.SHIFT_REGEX.match(instr).groups()
            self.instructions[key] = self.get_value(inner_key) >> int(amnt)

        elif 'OR' in instr:
            inner_key1, inner_key2 = self.OR_REGEX.match(instr).groups()
            self.instructions[key] = self.get_value(inner_key1) | self.get_value(inner_key2)

        elif 'AND' in instr:
            inner_key1, inner_key2 = self.AND_REGEX.match(instr).groups()
            if self.NUM_REGEX.match(inner_key1):
                self.instructions[key] = int(inner_key1) & self.get_value(inner_key2)
            else:
                self.instructions[key] = self.get_value(inner_key1) & self.get_value(inner_key2)

        elif self.NUM_REGEX.match(instr):
            self.instructions[key] = int(instr)

        elif self.WIRE_REGEX.match(instr):
            self.instructions[key] = self.get_value(instr)

        else:
            raise Exception('No matches found!')

        return self.instructions[key]

    def test(self):
        self.instructions = {}
        for line in self.get_test_input():
            instr, dest = self.LINE_REGEX.match(line).groups()
            self.instructions[dest] = instr

        return '\n'.join('{}: {}'.format(l, self.get_value(l)) for l in 'defghixy')

    def part1(self):
        self.get_instructions()
        self.part1_value = self.get_value('a')
        return self.part1_value

    def part2(self):
        self.get_instructions()
        # Override 'b' with value from part 1
        self.instructions['b'] = self.part1_value
        return self.get_value('a')


if __name__ == '__main__':
    Day7().run()
