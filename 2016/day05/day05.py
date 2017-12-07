from hashlib import md5
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from utils import AdventDay


class Day5(AdventDay):
    DAY = 5

    def part1(self):
        inp = self.get_input()[0]
        index = 0
        password = ''
        while len(password) < 8:
            h = md5((inp + str(index)).encode()).hexdigest()
            if h[:5] == '00000':
                password += h[5]
            index += 1

        return password

    def part2(self):
        inp = self.get_input()[0]
        index = 0
        password = [None] * 8
        while not all(password):
            h = md5((inp + str(index)).encode()).hexdigest()
            if h[:5] == '00000':
                try:
                    pass_index = int(h[5])
                except ValueError:
                    pass
                else:
                    if pass_index <= 7 and password[pass_index] is None:
                        password[pass_index] = h[6]

            index += 1

        return ''.join(password)


if __name__ == '__main__':
    Day5().run()
