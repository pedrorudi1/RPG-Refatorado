import unittest
from Models.Heroes import Hero, Warrior, Mage, Fighter, Thief, Priest, Ninja

class TestLevelUp(unittest.TestCase):
    def setUp(self):
        self.hero = Hero(1, "TestHero", 100, 50, 10, 10, 10, 10, 10, 10, 0, 10)
        self.warrior = Warrior(1, "TestWarrior", 100, 50, 10, 10, 10, 10, 10, 10, 0 ,10)
        self.mage = Mage(1, "TestMage", 100, 50, 10, 10, 10, 10, 10, 10, 0, 10)
        self.fighter = Fighter(1, "TestFighter", 100, 50, 10, 10, 10, 10, 10, 10, 0, 10)
        self.thief = Thief(1, "TestThief", 100, 50, 10, 10, 10, 10, 10, 10, 0, 10)
        self.priest = Priest(1, "TestPriest", 100, 50, 10, 10, 10, 10, 10, 10, 0, 10)
        self.ninja = Ninja(1, "TestNinja", 100, 50, 10, 10, 10, 10, 10, 10, 0, 10)

    def test_level_up_limit(self):
        characters = [
            self.hero, self.warrior, self.mage, self.fighter,
            self.thief, self.priest, self.ninja
        ]
        # Dá experiência suficiente para tentar passar do nível 99
        for char in characters:
            char.gain_xp(100000000)
            self.assertLessEqual(char.level, 99)
            print(f"\n{char.__class__.__name__} ({char.name}) - Nível: {char.level}")
            print(f"HP: {char.HP}, MP: {char.MP}, STR: {char.strenght}, MAG: {char.magic}, VIT: {char.vitality}, SPR: {char.spirit}, AGI: {char.agility}, LUCK: {char.luck}")

if __name__ == "__main__":
    unittest.main()