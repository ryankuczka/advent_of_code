import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from utils import AdventDay


class Day9(AdventDay):
    DAY = 9

    def part1(self):
        inp = self.get_input()
        compressed = ''.join(''.join(inp).split())
        uncompressed = ''

        in_marker = False
        in_substring = False
        marker = ''
        substring = ''
        substring_len = 0
        substring_cnt = 0

        for char in compressed:
            # If we're not in a marker or a substring...
            if not in_marker and not in_substring:
                # If we find the start of a marker...
                if char == '(':
                    in_marker = True
                # Otherwise, add the current character to uncompressed output
                else:
                    uncompressed += char

            # If we are parsing a marker...
            elif in_marker:
                # If this is the end of the marker, parse it, mark that we are
                # now in a substring, and reset the marker
                if char == ')':
                    substring_len, substring_cnt = map(int, marker.split('x'))
                    in_marker = False
                    in_substring = True
                    marker = ''
                # Otherwise, add this character to the marker
                else:
                    marker += char

            # If we are parsing a substring...
            elif in_substring:
                # Add the current character to a substring
                substring += char
                # Subtract 1 character from the remaining length
                substring_len -= 1
                # If this was the last character in a substring,
                # add the count to the uncompressed output and reset substring
                if substring_len == 0:
                    uncompressed += substring * substring_cnt
                    in_substring = False
                    substring = ''
                    substring_len = 0
                    substring_cnt = 0
        return len(uncompressed)

    def part2(self):
        pass

if __name__ == '__main__':
    Day9().run()
