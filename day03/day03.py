import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from utils import AdventDay


class Day3(AdventDay):
    DAY = 3

    MOVEMENTS = {
        '^': lambda pos: (pos[0], pos[1] + 1),
        '>': lambda pos: (pos[0] + 1, pos[1]),
        'v': lambda pos: (pos[0], pos[1] - 1),
        '<': lambda pos: (pos[0] - 1, pos[1]),
    }

    def part1(self):
        houses = set()
        position = (0, 0)
        houses.add(position)

        for direction in self.get_input()[0]:
            position = self.MOVEMENTS[direction](position)
            houses.add(position)
        return len(houses)

    def part2(self):
        houses = set()
        santa_position = (0, 0)
        robo_position = (0, 0)

        houses.add(santa_position)

        for i, direction in enumerate(self.get_input()[0]):
            if i % 2 == 0:
                santa_position = self.MOVEMENTS[direction](santa_position)
                houses.add(santa_position)
            else:
                robo_position = self.MOVEMENTS[direction](robo_position)
                houses.add(robo_position)

        return len(houses)


if __name__ == '__main__':
    Day3().run()
