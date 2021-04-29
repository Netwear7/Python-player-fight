import unittest

from Player import Player


# Imports should be grouped in the following order (PEP8):
# Standard library imports.
# Related third party imports.
# Local application/library specific imports.


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.instance_player = Player("TestPlayer")

    def testAttackDamage_IfGreaterThan100_ExceptionThrown(self):
        for i in range(1, 100):
            attack_damage = self.instance_player.random_attack_damage()
            self.assertLessEqual(attack_damage, 100)

    def testAttackDamage_IfLessThan1_ExceptionThrown(self):
        # Test 100 times
        for i in range(1, 100):
            attack_damage = self.instance_player.random_attack_damage()
            self.assertGreaterEqual(attack_damage, 1)

    def testInstanceOfPlayer(self):
        pass

    if __name__ == '__main__':
        unittest.main()
