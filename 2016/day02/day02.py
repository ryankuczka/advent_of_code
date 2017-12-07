import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from utils import AdventDay


class Day2(AdventDay):
    DAY = 2

    KEYPAD = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
    ]

    KEYPAD2 = [
        [None, None, '1', None, None],
        [None, '2', '3', '4', None],
        ['5', '6', '7', '8', '9'],
        [None, 'A', 'B', 'C', None],
        [None, None, 'D', None, None],
    ]

    INSTRUCTIONS = {
        'U': lambda loc: (loc[0], max(loc[1] - 1, 0)),
        'R': lambda loc: (min(loc[0] + 1, 2), loc[1]),
        'D': lambda loc: (loc[0], min(loc[1] + 1, 2)),
        'L': lambda loc: (max(loc[0] - 1, 0), loc[1]),
    }

    def process_instruction(self, loc, instruction, keypad):
        for c in instruction:
            if c == 'U':
                new_loc = loc[0], max(loc[1] - 1, 0)
            elif c == 'R':
                new_loc = min(loc[0] + 1, len(keypad[0]) - 1), loc[1]
            elif c == 'D':
                new_loc = loc[0], min(loc[1] + 1, len(keypad) - 1)
            elif c == 'L':
                new_loc = max(loc[0] - 1, 0), loc[1]

            if keypad[new_loc[1]][new_loc[0]] is not None:
                loc = new_loc
        return loc

    def get_code(self, loc, inp, keypad):
        code = ''
        for instruction in inp:
            loc = self.process_instruction(loc, instruction, keypad)
            code += keypad[loc[1]][loc[0]]
        return code

    def test(self):
        inp = self.get_test_input()
        return self.get_code((1, 1), inp, self.KEYPAD), self.get_code((0, 2), inp, self.KEYPAD2)

    def part1(self):
        inp = self.get_input()
        return self.get_code((1, 1), inp, self.KEYPAD)

    def part2(self):
        inp = self.get_input()
        return self.get_code((0, 2), inp, self.KEYPAD2)


if __name__ == '__main__':
    Day2().run()
