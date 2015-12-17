import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from utils import AdventDay


class Day16(AdventDay):
    DAY = 16

    FACTS = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1,
    }

    def part1(self):
        for line in self.get_input():
            sue, attributes = map(str.strip, line.split(':', 1))
            for sue_fact in map(str.strip, attributes.split(',')):
                fact, value = map(str.strip, sue_fact.split(':'))
                if self.FACTS[fact] != int(value):
                    break
            else:
                return sue

    def part2(self):
        for line in self.get_input():
            sue, attributes = map(str.strip, line.split(':', 1))
            for sue_fact in map(str.strip, attributes.split(',')):
                fact, value = map(str.strip, sue_fact.split(':'))
                if fact in ['cats', 'trees']:
                    if self.FACTS[fact] >= int(value):
                        break
                elif fact in ['pomeranians', 'goldfish']:
                    if self.FACTS[fact] <= int(value):
                        break
                elif self.FACTS[fact] != int(value):
                    break
            else:
                return sue

if __name__ == '__main__':
    Day16().run()
