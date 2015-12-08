import os
import re


LINE_REGEX = re.compile(r'(toggle|turn (?:on|off)) (\d{,3}),(\d{,3}) through (\d{,3}),(\d{,3})')

def get_input():
    with open(os.path.abspath(os.path.join(__file__, os.pardir, 'input.txt'))) as input_file:
        return [line.strip() for line in input_file.readlines()]


def part1():
    lights = [[False for x in range(1000)] for y in range(1000)]

    for line in get_input():
        instr, xstart, ystart, xend, yend = LINE_REGEX.match(line).groups()
        for x in range(int(xstart), int(xend) + 1):
            for y in range(int(ystart), int(yend) + 1):
                if instr == 'toggle':
                    lights[x][y] = not lights[x][y]
                elif instr == 'turn on':
                    lights[x][y] = True
                elif instr == 'turn off':
                    lights[x][y] = False

    light_count = 0
    for row in lights:
        for light in row:
            light_count += 1 if light else 0

    print '# OF LIGHTS ON:', light_count


def part2():
    lights = [[0 for x in range(1000)] for y in range(1000)]

    for line in get_input():
        instr, xstart, ystart, xend, yend = LINE_REGEX.match(line).groups()
        for x in range(int(xstart), int(xend) + 1):
            for y in range(int(ystart), int(yend) + 1):
                if instr == 'toggle':
                    lights[x][y] += 2
                elif instr == 'turn on':
                    lights[x][y] += 1
                elif instr == 'turn off':
                    lights[x][y] = max(0, lights[x][y] - 1)

    brightness = 0
    for row in lights:
        for light in row:
            brightness += light

    print 'TOTAL BRIGHTNESS:', brightness


if __name__ == '__main__':
    part1()
    part2()
