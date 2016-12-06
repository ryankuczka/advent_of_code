import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from utils import AdventDay


class Day20(AdventDay):
    DAY = 20

    def get_divisors(self, num):
        divisors = set()
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                divisors.add(i)
                divisors.add(num // i)
        return divisors

    def test(self):
        houses = {n: 0 for n in range(1, 10)}
        for house in range(1, 10):
            for elf in self.get_divisors(house):
                houses[house] += 10 * elf
        return houses

    def part1(self):
        house = presents = 0
        while presents < int(self.get_input()[0]):
            house += 1
            presents = 0
            for elf in self.get_divisors(house):
                presents += 10 * elf

        return house

    def part2(self):
        house = presents = 0
        while presents < int(self.get_input()[0]):
            house += 1
            presents = 0
            for elf in self.get_divisors(house):
                if elf * 50 >= house:
                    presents += 11 * elf

        return house


if __name__ == '__main__':
    Day20().run()
