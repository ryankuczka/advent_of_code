import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from utils import AdventDay


class Day18(AdventDay):
    DAY = 18

    def print_lights(self):
        print '\n'.join(''.join('#' if self.lights[y][x] else '.' for x in range(len(self.lights[0]))) for y in range(len(self.lights)))
        print

    def toggle_lights(self):
        max_x = len(self.lights[0])
        max_y = len(self.lights)
        new_lights = [[False for x in range(max_x)] for y in range(max_y)]
        for x in range(max_x):
            for y in range(max_y):
                neighbors = [(a, b) for a in range(max(x - 1, 0), min(x + 2, max_x)) for b in range(max(y - 1, 0), min(y + 2, max_y))]
                neighbors.remove((x, y))
                on_neighbors = [n for n in neighbors if self.lights[n[1]][n[0]]]

                if self.lights[y][x] and len(on_neighbors) not in [2, 3]:
                    new_lights[y][x] = False
                elif not self.lights[y][x] and len(on_neighbors) == 3:
                    new_lights[y][x] = True
                else:
                    new_lights[y][x] = self.lights[y][x]
        self.lights = new_lights

    def test(self):
        self.lights = [[light == '#' for light in row] for row in self.get_test_input()]
        self.lights[0][0] = self.lights[0][5] = self.lights[5][0] = self.lights[5][5] = True
        for step in range(5):
            # self.print_lights()
            self.toggle_lights()
            self.lights[0][0] = self.lights[0][5] = self.lights[5][0] = self.lights[5][5] = True
        # self.print_lights()
        return sum(x for y in self.lights for x in y)

    def part1(self):
        self.lights = [[light == '#' for light in row] for row in self.get_input()]
        for step in range(100):
            self.toggle_lights()

        return sum(x for y in self.lights for x in y)

    def part2(self):
        self.lights = [[light == '#' for light in row] for row in self.get_input()]
        self.lights[0][0] = self.lights[0][99] = self.lights[99][0] = self.lights[99][99] = True
        for step in range(100):
            self.toggle_lights()
            self.lights[0][0] = self.lights[0][99] = self.lights[99][0] = self.lights[99][99] = True

        return sum(x for y in self.lights for x in y)

if __name__ == '__main__':
    Day18().run()
