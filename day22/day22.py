import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(__file__, os.pardir, os.pardir)))

import itertools

from utils import AdventDay


class Day22(AdventDay):
    DAY = 22

    # Taken from input.txt
    boss_hp = 71
    boss_dmg = 10

    player_hp = 50
    player_mana = 500

    spells = ('magic_missile', 'drain', 'shield', 'poison', 'recharge')

    def fight(self):
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
