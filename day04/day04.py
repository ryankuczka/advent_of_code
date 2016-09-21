import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from hashlib import md5

from utils import AdventDay


class Day4(AdventDay):
    DAY = 4

    def find_hash(self, leading_zeroes=5):
        zeroes = '0' * leading_zeroes
        base_key = self.get_input()[0]
        i = 1

        key = '{0}{1}'.format(base_key, i)

        while not md5(key).hexdigest().startswith(zeroes):
            i += 1
            key = '{0}{1}'.format(base_key, i)

        return i

    def part1(self):
        return self.find_hash()

    def part2(self):
        return self.find_hash(6)


if __name__ == '__main__':
    Day4().run()
