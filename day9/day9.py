import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from collections import defaultdict
from itertools import permutations
import re
from utils import AdventDay


class Day9(AdventDay):
    DAY = 9

    LINE_REGEX = re.compile(r'(\w+) to (\w+) = (\d+)')

    def build_graph(self):
        """
        Not the best, but it's functional for small data sets...
        """
        self.graph = defaultdict(dict)
        for line in self.get_input():
            city1, city2, distance = self.LINE_REGEX.match(line).groups()
            self.graph[city1][city2] = int(distance)
            self.graph[city2][city1] = int(distance)

        self.graph = dict(self.graph)

    def get_path_len(self, path):
        length = 0
        # Get distance between each node
        for index in range(len(path) - 1):
            length += self.graph[path[index]][path[index + 1]]
        return length

    def part1(self):
        self.build_graph()
        # Let's brute force this!
        path_lens = []
        for path in permutations(self.graph.keys()):
            path_lens.append(self.get_path_len(path))
        return min(path_lens)

    def part2(self):
        self.build_graph()
        # Let's brute force this!
        path_lens = []
        for path in permutations(self.graph.keys()):
            path_lens.append(self.get_path_len(path))
        return max(path_lens)


if __name__ == '__main__':
    Day9().run()
