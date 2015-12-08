import os


class AdventDay(object):
    DAY = None

    def run(self):
        if hasattr(self, 'test'):
            print '# TEST #'
            print self.test()
            print

        print '# PART 1 #'
        print self.part1()
        print

        print '# PART 2 #'
        print self.part2()

    def part1(self):
        pass

    def part2(self):
        pass

    def _get_input(self, filename):
        dir_name = 'day{}'.format(self.DAY)
        inp_path = os.path.abspath(os.path.join(__file__, os.pardir, dir_name, filename))
        with open(inp_path) as inp_file:
            return [line.strip() for line in inp_file.readlines()]

    def get_input(self):
        return self._get_input('input.txt')

    def get_test_input(self):
        return self._get_input('test_input.txt')
