import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from collections import defaultdict
import re
from utils import AdventDay


class Day14(AdventDay):
    DAY = 14

    LINE_REGEX = re.compile(r'(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds\.')

    def get_distances(self, speed, fly_time, rest_time, total_time):
        last_change = 0
        distance = 0
        flying = True
        distances = []
        for second in range(1, total_time + 1):
            if flying:
                distance += speed

            distances.append(distance)

            if (flying and last_change + fly_time == second) or \
                    (not flying and last_change + rest_time == second):
                flying = not flying
                last_change = second
        return distances

    def test(self):
        distances = {}
        for line in self.get_test_input():
            name, speed, fly_time, rest_time = self.LINE_REGEX.match(line).groups()
            distances[name] = self.get_distances(int(speed), int(fly_time), int(rest_time), 1000)

        assert distances['Comet'][-1] == 1120, '{} != 1120'.format(distances['Comet'][-1])
        assert distances['Dancer'][-1] == 1056, '{} != 1056'.format(distances['Dancer'][-1])

    def part1(self):
        distances = []
        for line in self.get_input():
            name, speed, fly_time, rest_time = self.LINE_REGEX.match(line).groups()
            distances.append(self.get_distances(int(speed), int(fly_time), int(rest_time), 2503))
        return max(d[-1] for d in distances)

    def part2(self):
        distances = {}
        scores = defaultdict(int)
        for line in self.get_input():
            name, speed, fly_time, rest_time = self.LINE_REGEX.match(line).groups()
            distances[name] = self.get_distances(int(speed), int(fly_time), int(rest_time), 2503)

        max_distances = [max(i) for i in zip(*distances.values())]

        for name, d in distances.items():
            for i, distance in enumerate(d):
                if distance == max_distances[i]:
                    scores[name] += 1

        return max(scores.values())

if __name__ == '__main__':
    Day14().run()
