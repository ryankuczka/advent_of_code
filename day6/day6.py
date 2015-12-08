import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

import re
from utils import AdventDay


class Day6(AdventDay):
    DAY = 6

    LINE_REGEX = re.compile(r'(toggle|turn (?:on|off)) (\d{,3}),(\d{,3}) through (\d{,3}),(\d{,3})')

    def init_light_grid(self, init_value):
        self.lights = [[init_value for x in range(1000)] for y in range(1000)]

    def toggle_lights(self):
        for line in self.get_input():
            instr, xstart, ystart, xend, yend = self.LINE_REGEX.match(line).groups()
            for x in range(int(xstart), int(xend) + 1):
                for y in range(int(ystart), int(yend) + 1):
                    if instr == 'toggle':
                        self.lights[x][y] = self.toggle(x, y)
                    elif instr == 'turn on':
                        self.lights[x][y] = self.on(x, y)
                    elif instr == 'turn off':
                        self.lights[x][y] = self.off(x, y)

    def part1(self):
        self.init_light_grid(False)
        self.toggle = lambda x, y: not self.lights[x][y]
        self.on = lambda x, y: True
        self.off = lambda x, y: False

        self.toggle_lights()

        return sum(x for y in self.lights for x in y)

    def part2(self):
        self.init_light_grid(0)
        self.toggle = lambda x, y: self.lights[x][y] + 2
        self.on = lambda x, y: self.lights[x][y] + 1
        self.off = lambda x, y: max(0, self.lights[x][y] - 1)

        self.toggle_lights()

        return sum(x for y in self.lights for x in y)


if __name__ == '__main__':
    Day6().run()
