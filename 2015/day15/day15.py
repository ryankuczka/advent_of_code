import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

import pandas as pd
import re
from utils import AdventDay


class Day15(AdventDay):
    DAY = 15

    LINE_REGEX = re.compile(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)')

    def __init__(self):
        super(Day15, self).__init__()
        self.get_combinations()

    def get_combinations(self):
        self.combinations = set()
        for a in range(1, 98):
            for b in range(1, 98):
                for c in range(1, 98):
                    for d in range(1, 98):
                        if a + b + c + d == 100:
                            self.combinations.add((a, b, c, d))

    def test(self):
        data = {}
        calorie_data = {}
        index = ['capacity', 'durability', 'flavor', 'texture']
        for line in self.get_test_input():
            name, capacity, durability, flavor, texture, calories = \
                self.LINE_REGEX.match(line).groups()

            data[name] = map(int, [capacity, durability, flavor, texture])
            calorie_data[name] = int(calories)

        df = pd.DataFrame(data, index=index)
        max_score = 0
        max_calorie = 0
        for a in range(1, 100):
            calorie_count = a * calorie_data['Butterscotch'] + (100 - a) * calorie_data['Cinnamon']
            individual_scores = a * df['Butterscotch'] + (100 - a) * df['Cinnamon']
            individual_scores[individual_scores < 0] = 0
            score = individual_scores.product()
            if score > max_score:
                max_score = score
                if calorie_count == 500:
                    max_calorie = score

        return (max_score, max_calorie)

    def part1(self):
        data = {}
        index = ['capacity', 'durability', 'flavor', 'texture']
        names = []
        for line in self.get_input():
            name, capacity, durability, flavor, texture, calories = \
                self.LINE_REGEX.match(line).groups()

            data[name] = map(int, [capacity, durability, flavor, texture])
            names.append(name)

        df = pd.DataFrame(data, index=index)
        max_score = 0
        for combo in self.combinations:
            individual_scores = combo[0] * df[names[0]] + \
                combo[1] * df[names[1]] + combo[2] * df[names[2]] + \
                combo[3] * df[names[3]]
            individual_scores[individual_scores < 0] = 0
            score = individual_scores.product()
            if score > max_score:
                max_score = score

        return max_score

    def part2(self):
        data = {}
        calorie_data = {}
        index = ['capacity', 'durability', 'flavor', 'texture']
        names = []
        for line in self.get_input():
            name, capacity, durability, flavor, texture, calories = \
                self.LINE_REGEX.match(line).groups()

            data[name] = map(int, [capacity, durability, flavor, texture])
            calorie_data[name] = int(calories)
            names.append(name)

        df = pd.DataFrame(data, index=index)
        max_score = 0
        for combo in self.combinations:
            calorie_count = combo[0] * calorie_data[names[0]] + \
                combo[1] * calorie_data[names[1]] + combo[2] * calorie_data[names[2]] + \
                combo[3] * calorie_data[names[3]]
            if calorie_count != 500:
                continue
            individual_scores = combo[0] * df[names[0]] + \
                combo[1] * df[names[1]] + combo[2] * df[names[2]] + \
                combo[3] * df[names[3]]
            individual_scores[individual_scores < 0] = 0
            score = individual_scores.product()
            if score > max_score:
                max_score = score

        return max_score

if __name__ == '__main__':
    Day15().run()
