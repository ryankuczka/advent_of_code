from collections import Counter
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from utils import AdventDay


class Day6(AdventDay):
    DAY = 6

    def part1(self):
        inp = self.get_input()
        cols = zip(*inp)
        result = ''
        for col in cols:
            result += Counter(col).most_common(1)[0][0]
        return result

    def part2(self):
        inp = self.get_input()
        cols = zip(*inp)
        result = ''
        for col in cols:
            result += Counter(col).most_common()[-1][0]
        return result


if __name__ == '__main__':
    Day6().run()
