from collections import Counter
import os
import re
from string import ascii_lowercase
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from utils import AdventDay


class Day4(AdventDay):
    DAY = 4

    ROOM_REGEX = re.compile(r'(?P<name>[a-z-]+)-(?P<sector>\d+)\[(?P<checksum>[a-z]+)\]')

    def is_real(self, name, checksum):
        name = name.replace('-', '')
        counts = Counter(name)
        for i, (letter, count) in enumerate(sorted(counts.most_common(), key=lambda x: (-x[1], x[0]))):
            if i > 4:
                break
            if letter != checksum[i]:
                return False
        return True

    def decrypt_room(self, name, sector):
        decrypted_name = ''
        for letter in name:
            if letter == '-':
                decrypted_name += ' '
            else:
                decrypted_name += ascii_lowercase[(ascii_lowercase.index(letter) + sector) % 26]
        return decrypted_name

    def test(self):
        inp = self.get_test_input()
        sector_sum = 0
        for room in inp:
            match = self.ROOM_REGEX.match(room)
            if self.is_real(match.group('name'), match.group('checksum')):
                print('    REAL: {}'.format(room))
                sector_sum += int(match.group('sector'))
            else:
                print('NOT REAL: {}'.format(room))

        return sector_sum, self.decrypt_room('qzmt-zixmtkozy-ivhz', 343)

    def part1(self):
        inp = self.get_input()
        sector_sum = 0
        for room in inp:
            match = self.ROOM_REGEX.match(room)
            if self.is_real(match.group('name'), match.group('checksum')):
                sector_sum += int(match.group('sector'))

        return sector_sum

    def part2(self):
        inp = self.get_input()
        for room in inp:
            match = self.ROOM_REGEX.match(room)
            if self.is_real(match.group('name'), match.group('checksum')):
                if self.decrypt_room(match.group('name'), int(match.group('sector'))) == 'northpole object storage':
                    return match.group('sector')


if __name__ == '__main__':
    Day4().run()
