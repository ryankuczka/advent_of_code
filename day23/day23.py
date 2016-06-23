import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from utils import AdventDay


class Day23(AdventDay):
    DAY = 23

    def perform_instruction(self):
        instr, info = self.instructions[self.current].split(' ', 1)

        if instr == 'jie':
            register, jump = map(str.strip, info.split(','))
            if getattr(self, register) % 2 == 0:
                self.current += int(jump)
            else:
                self.current += 1
        elif instr == 'jio':
            register, jump = map(str.strip, info.split(','))
            if getattr(self, register) == 1:
                self.current += int(jump)
            else:
                self.current += 1
        elif instr == 'jmp':
            self.current += int(info)
        elif instr == 'inc':
            setattr(self, info, getattr(self, info) + 1)
            self.current += 1
        elif instr == 'hlf':
            setattr(self, info, getattr(self, info) / 2)
            self.current += 1
        elif instr == 'tpl':
            setattr(self, info, getattr(self, info) * 3)
            self.current += 1

    def part1(self):
        self.current = self.a = self.b = 0
        self.instructions = self.get_input()

        while True:
            try:
                self.perform_instruction()
            except IndexError:
                break

        return self.b

    def part2(self):
        self.current = self.b = 0
        self.a = 1
        self.instructions = self.get_input()

        while True:
            try:
                self.perform_instruction()
            except IndexError:
                break

        return self.b


if __name__ == '__main__':
    Day23().run()
