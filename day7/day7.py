import os
import re


LINE_REGEX = re.compile(r'(.*) -> (.*)')
NOT_REGEX = re.compile('NOT ([a-z]{1,2})')
SHIFT_REGEX = re.compile('([a-z]{1,2}) [LR]SHIFT ([0-9]+)')
OR_REGEX = re.compile('([a-z]{1,2}) OR ([a-z]{1,2})')
AND_REGEX = re.compile('([a-z0-9]+) AND ([a-z]{1,2})')
NUM_REGEX = re.compile('\d+')
WIRE_REGEX = re.compile('[a-z]{1,2}')


def get_test_input():
    with open(os.path.abspath(os.path.join(__file__, os.pardir, 'test_input.txt'))) as test_file:
        return [line.strip() for line in test_file.readlines()]


def get_input():
    with open(os.path.abspath(os.path.join(__file__, os.pardir, 'input.txt'))) as input_file:
        return [line.strip() for line in input_file.readlines()]


def get_value(key, instructions):
    instr = instructions[key]

    # Short-circuit if we've already done this key
    if isinstance(instr, int):
        return instr

    if 'NOT' in instr:
        inner_key, = NOT_REGEX.match(instr).groups()
        instructions[key] = 65535 ^ get_value(inner_key, instructions)

    elif 'LSHIFT' in instr:
        inner_key, amnt = SHIFT_REGEX.match(instr).groups()
        instructions[key] = get_value(inner_key, instructions) << int(amnt)

    elif 'RSHIFT' in instr:
        inner_key, amnt = SHIFT_REGEX.match(instr).groups()
        instructions[key] = get_value(inner_key, instructions) >> int(amnt)

    elif 'OR' in instr:
        inner_key1, inner_key2 = OR_REGEX.match(instr).groups()
        instructions[key] = get_value(inner_key1, instructions) | get_value(inner_key2, instructions)

    elif 'AND' in instr:
        inner_key1, inner_key2 = AND_REGEX.match(instr).groups()
        if NUM_REGEX.match(inner_key1):
            instructions[key] = int(inner_key1) & get_value(inner_key2, instructions)
        else:
            instructions[key] = get_value(inner_key1, instructions) & get_value(inner_key2, instructions)

    elif NUM_REGEX.match(instr):
        instructions[key] = int(instr)

    elif WIRE_REGEX.match(instr):
        instructions[key] = get_value(instr, instructions)

    else:
        raise Exception('No matches found!')

    return instructions[key]


def test():
    instructions = {}
    for line in get_test_input():
        instr, dest = LINE_REGEX.match(line).groups()
        instructions[dest] = instr

    print 'd:', get_value('d', instructions)
    print 'e:', get_value('e', instructions)
    print 'f:', get_value('f', instructions)
    print 'g:', get_value('g', instructions)
    print 'h:', get_value('h', instructions)
    print 'i:', get_value('i', instructions)

def part1():
    instructions = {}
    for line in get_input():
        instr, dest = LINE_REGEX.match(line).groups()
        instructions[dest] = instr

    avalue = get_value('a', instructions)
    print 'a:', avalue
    return avalue


def part2(avalue):
    instructions = {}
    for line in get_input():
        instr, dest = LINE_REGEX.match(line).groups()
        instructions[dest] = instr

    # Override 'b' with value from part 1
    instructions['b'] = avalue

    print 'a:', get_value('a', instructions)


if __name__ == '__main__':
    avalue = part1()
    part2(avalue)
