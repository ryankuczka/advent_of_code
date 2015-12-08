import os
import re


DELIM_REGEX = re.compile('^"|"$')
ESCAPE_REGEX = re.compile(r'\\(\\|")')
HEX_REGEX = re.compile(r'\\x.{2}')


def get_input():
    with open(os.path.abspath(os.path.join(__file__, os.pardir, 'input.txt'))) as input_file:
        return [line.strip() for line in input_file.readlines()]


def part1():
    code_strings = get_input()
    actual_strings = []
    for code in code_strings:
        actual = DELIM_REGEX.sub('', code)
        actual = ESCAPE_REGEX.sub('X', actual)
        actual = HEX_REGEX.sub('X', actual)
        actual_strings.append(actual)

    code_len = sum(map(len, code_strings))
    actual_len = sum(map(len, actual_strings))
    print 'CODE:', code_len
    print 'ACTUAL:', actual_len
    print 'DIFF:', code_len - actual_len


def part2():
    code_strings = get_input()
    encoded_strings = []
    for code in code_strings:
        encoded = DELIM_REGEX.sub('XXX', code)
        encoded = ESCAPE_REGEX.sub('XXXX', encoded)
        encoded = HEX_REGEX.sub('XXXXX', encoded)
        encoded_strings.append(encoded)

    code_len = sum(map(len, code_strings))
    encoded_len = sum(map(len, encoded_strings))
    print 'CODE:', code_len
    print 'ENCODED:', encoded_len
    print 'DIFF:', encoded_len - code_len


if __name__ == '__main__':
    print 'PART 1'
    part1()
    print
    print 'PART 2'
    part2()
