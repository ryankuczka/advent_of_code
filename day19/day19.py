import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from collections import defaultdict

from utils import AdventDay


class Day19(AdventDay):
    DAY = 19

    def parse_input(self, inp):
        self.mapping = defaultdict(list)
        for line in inp:
            if '=>' in line:
                elem, repl = map(str.strip, line.split('=>'))
                self.mapping[elem].append(repl)
            elif line:
                self.starting_molecule = line

    def get_distinct_molecules(self):
        molecules = set()
        for index in range(len(self.starting_molecule)):
            elem = self.starting_molecule[index]

            if elem not in self.mapping:
                try:
                    elem += self.starting_molecule[index + 1]
                except IndexError:
                    continue

            if elem not in self.mapping:
                continue

            for repl in self.mapping[elem]:
                new_molecule = self.starting_molecule[:index] + repl + self.starting_molecule[index + len(elem):]
                molecules.add(new_molecule)

        return molecules

    def test(self):
        self.parse_input(self.get_test_input())
        return self.get_distinct_molecules()

    def part1(self):
        self.parse_input(self.get_input())
        return len(self.get_distinct_molecules())

    def part2(self):
        pass

if __name__ == '__main__':
    Day19().run()
