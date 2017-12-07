from collections import deque
import os
import re
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from utils import AdventDay


class Day8(AdventDay):
    DAY = 8

    RECT_REGEX = re.compile(r'rect (?P<x>\d+)x(?P<y>\d+)')
    ROW_REGEX = re.compile(r'rotate row y=(?P<x>\d+) by (?P<count>\d+)')
    COL_REGEX = re.compile(r'rotate column x=(?P<y>\d+) by (?P<count>\d+)')

    def build_grid(self):
        grid = deque()
        for row in range(6):
            grid.append(deque())
            for col in range(50):
                grid[row].append(0)
        return grid

    def transpose_grid(self, grid):
        gridT = deque()
        for col in range(len(grid[0])):
            gridT.append(deque())
            for row in range(len(grid)):
                gridT[col].append(grid[row][col])
        return gridT

    def parse_instructions(self):
        grid = self.build_grid()
        inp = self.get_input()
        for instr in inp:
            rect_match = self.RECT_REGEX.match(instr)
            if rect_match:
                for row in range(int(rect_match.group('y'))):
                    for col in range(int(rect_match.group('x'))):
                        grid[row][col] = 1
                continue

            row_match = self.ROW_REGEX.match(instr)
            if row_match:
                grid[int(row_match.group('x'))].rotate(int(row_match.group('count')))
                continue

            col_match = self.COL_REGEX.match(instr)
            if col_match:
                gridT = self.transpose_grid(grid)
                gridT[int(col_match.group('y'))].rotate(int(col_match.group('count')))
                grid = self.transpose_grid(gridT)
        return grid

    def part1(self):
        grid = self.parse_instructions()
        return sum(map(sum, grid))

    def part2(self):
        grid = self.parse_instructions()
        s = ''
        for row in grid:
            for col in row:
                if col:
                    s += '#'
                else:
                    s += '.'
            s += '\n'
        return s

if __name__ == '__main__':
    Day8().run()
