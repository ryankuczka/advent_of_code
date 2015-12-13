import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

import re
import string
from utils import AdventDay


class Day11(AdventDay):
    DAY = 11

    # Match 2 or more groups of double letters
    DOUBLE_LETTER_REGEX = re.compile(r'(?:(.)\1.*){2,}')
    TRIPLE_RUNS = set([string.lowercase[i - 3:i] for i in range(3, 27)])
    ILLEGAL_LETTERS = {
        'i': 'j',
        'l': 'm',
        'o': 'p',
    }

    def increment(self, password):
        last_letter = password[-1]
        if last_letter == 'z':
            return self.increment(password[:-1]) + 'a'

        new_letter = chr(ord(last_letter) + 1)
        if new_letter in self.ILLEGAL_LETTERS:
            new_letter = self.ILLEGAL_LETTERS[new_letter]

        return password[:-1] + new_letter

    def valid_password(self, password):
        triple_sets = set([password[i - 3:i] for i in range(3, len(password) + 1)])
        return triple_sets & self.TRIPLE_RUNS and \
            self.DOUBLE_LETTER_REGEX.search(password) and \
            not set(self.ILLEGAL_LETTERS.keys()) & set(password)

    def get_next_valid_password(self, password):
        # Increment at least once
        new_password = self.increment(password)
        while not self.valid_password(new_password):
            new_password = self.increment(new_password)
        return new_password

    def test(self):
        results = ['abcdffaa', 'ghjaabcc']
        for i, password in enumerate(self.get_test_input()):
            new_password = self.get_next_valid_password(password)
            assert new_password == results[i], '{0} != {1}'.format(new_password, results[i])
        return 'Passed!'

    def part1(self):
        password = self.get_input()[0]
        self.part1 = self.get_next_valid_password(password)
        return self.part1

    def part2(self):
        return self.get_next_valid_password(self.part1)


if __name__ == '__main__':
    Day11().run()
