from collections import defaultdict
import os
import re
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from utils import AdventDay


class Day10(AdventDay):
    DAY = 10

    TRANSFER_INSTRUCTION = re.compile('bot (?P<src_num>\d+) gives low to (?P<low_dest>bot|output) (?P<low_num>\d+) and high to (?P<high_dest>bot|output) (?P<high_num>\d+)')
    VALUE_INSTRUCTION = re.compile('value (?P<value>\d+) goes to bot (?P<bot_num>\d+)')

    def parse_instructions(self):
        inp = self.get_input()
        transfer_instructions = {}
        bot_values = defaultdict(list)

        for instr in inp:
            transfer = self.TRANSFER_INSTRUCTION.match(instr)
            if transfer:
                src, low_dest, low, high_dest, high = transfer.groups()
                transfer_instructions[int(src)] = {'low': {'dest': low_dest, 'num': int(low)}, 'high': {'dest': high_dest, 'num': int(high)}}

            value = self.VALUE_INSTRUCTION.match(instr)
            if value:
                val, bot = map(int, value.groups())
                bot_values[bot].append(val)
                bot_values[bot].sort()

        return transfer_instructions, bot_values

    def part1(self):
        transfers, bot_values = self.parse_instructions()
        outputs = defaultdict(list)

        while True:
            for bot_num, values in bot_values.items():
                if values == [17, 61]:
                    return bot_num

                if len(values) == 2:
                    low, high = values
                    instructions = transfers[bot_num]
                    for lohi, instr in instructions.items():
                        if instr['dest'] == 'bot':
                            bot_values[instr['num']].append(low if lohi == 'low' else high)
                            bot_values[instr['num']].sort()
                        elif instr['dest'] == 'output':
                            outputs[instr['num']].append(low if lohi == 'low' else high)
                    bot_values[bot_num] = []
                    break
            else:
                break

    def part2(self):
        transfers, bot_values = self.parse_instructions()
        outputs = defaultdict(list)

        while True:
            for bot_num, values in bot_values.items():
                if len(values) == 2:
                    low, high = values
                    instructions = transfers[bot_num]
                    for lohi, instr in instructions.items():
                        if instr['dest'] == 'bot':
                            bot_values[instr['num']].append(low if lohi == 'low' else high)
                            bot_values[instr['num']].sort()
                        elif instr['dest'] == 'output':
                            outputs[instr['num']].append(low if lohi == 'low' else high)
                    bot_values[bot_num] = []
                    break
            else:
                break

        return outputs[0][0] * outputs[1][0] * outputs[2][0]

if __name__ == '__main__':
    Day10().run()
