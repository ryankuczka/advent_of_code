import os
import re
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

from utils import AdventDay


class Day7(AdventDay):
    DAY = 7

    ABBA_REGEX = re.compile(r'([a-z])(?!\1)([a-z])\2\1')
    ABA_REGEX = re.compile(r'([a-z])(?!\1)([a-z])\1')
    IP_REGEX = re.compile(r'(?:^|\])(?P<nonhyper>[a-z]*)|(?<=\[)(?P<hyper>[a-z]*)(?=\])')

    def findall(self, regex, string):
        results = []
        pos = 0

        while True:
            result = regex.search(string, pos)
            if result is None:
                break
            results.append(result.groups())
            pos = result.start() + 1
        return results

    def part1(self):
        inp = self.get_input()
        tls = 0
        for ip in inp:
            nonhyper_abba = False
            hyper_abba = False
            for nonhyper, hyper in self.IP_REGEX.findall(ip):
                if nonhyper and self.ABBA_REGEX.search(nonhyper):
                    nonhyper_abba = True
                elif hyper and self.ABBA_REGEX.search(hyper):
                    hyper_abba = True

            if nonhyper_abba and not hyper_abba:
                tls += 1
        return tls

    def part2(self):
        inp = self.get_input()
        ssl = 0
        for ip in inp:
            abas = []

            nonhypers, hypers = zip(*self.IP_REGEX.findall(ip))
            # Go through the non-hypernet sequences and look for ABA sequences
            for nonhyper in nonhypers:
                if not nonhyper:
                    continue
                abas += self.findall(self.ABA_REGEX, nonhyper)

            if not abas:
                continue

            for hyper in hypers:
                if not hyper:
                    continue
                for a, b in abas:
                    bab = ''.join([b, a, b])
                    if bab in hyper:
                        break
                else:
                    continue
                ssl += 1
                break
        return ssl

if __name__ == '__main__':
    Day7().run()
