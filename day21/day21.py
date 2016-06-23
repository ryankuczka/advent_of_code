import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

import itertools

from utils import AdventDay


class Day21(AdventDay):
    DAY = 21

    # Taken from input.txt
    boss_hp = 100
    boss_dmg = 8
    boss_def = 2

    player_hp = 100

    weapons = (
        (8, 4, 0),
        (10, 5, 0),
        (25, 6, 0),
        (40, 7, 0),
        (74, 8, 0),
    )

    armor = (
        (0, 0, 0),
        (13, 0, 1),
        (31, 0, 2),
        (53, 0, 3),
        (75, 0, 4),
        (102, 0, 5),
    )

    rings = (
        (0, 0, 0),
        (0, 0, 0),
        (25, 1, 0),
        (50, 2, 0),
        (100, 3, 0),
        (20, 0, 1),
        (40, 0, 2),
        (80, 0, 3),
    )

    def fight(self, dmg, armor):
        boss_hp = self.boss_hp
        player_hp = self.player_hp

        while True:
            boss_hp -= max(dmg - self.boss_def, 1)
            if boss_hp <= 0:
                return 'PLAYER'
            player_hp -= max(self.boss_dmg - armor, 1)
            if player_hp <= 0:
                return 'BOSS'

    def get_item_combos(self):
        item_combos = set()
        for weapon in self.weapons:
            for armor in self.armor:
                for ring1, ring2 in itertools.combinations(self.rings, 2):
                    item_combos.add((weapon, armor, ring1, ring2))
        return item_combos

    def part1(self):
        min_gold = None
        for item_combo in self.get_item_combos():
            gold, dmg, armor = map(sum, zip(*item_combo))
            if self.fight(dmg, armor) == 'PLAYER' and (min_gold is None or gold < min_gold):
                min_gold = gold

        return min_gold

    def part2(self):
        max_gold = None
        for item_combo in self.get_item_combos():
            gold, dmg, armor = map(sum, zip(*item_combo))
            if self.fight(dmg, armor) == 'BOSS' and (max_gold is None or gold > max_gold):
                max_gold = gold

        return max_gold


if __name__ == '__main__':
    Day21().run()
