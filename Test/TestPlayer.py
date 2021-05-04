import unittest

from Player import Player


# Imports should be grouped in the following order (PEP8):
# Standard library imports.
# Related third party imports.
# Local application/library specific imports.


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.instance_player = Player("TestPlayer")

    def testAttackDamage_IfLessThan100(self):
        attack_damage = self.instance_player.random_attack_damage()
        self.assertLessEqual(attack_damage, 100)

    def testAttackDamage_IfGreaterThan1(self):
        attack_damage = self.instance_player.random_attack_damage()
        self.assertGreaterEqual(attack_damage, 1)

    def testInstanceOfPlayer(self):
        #wip
        pass

    if __name__ == '__main__':
        unittest.main()
