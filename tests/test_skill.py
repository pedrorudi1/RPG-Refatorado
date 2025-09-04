import unittest
from Models.Heroes import HeroesClass, Hero, Warrior, Mage, Fighter, Thief, Priest, Ninja

class DummySkill:
    def __init__(self, name):
        self.name = name

class TestHeroSkills(unittest.TestCase):
    def setUp(self):
        self.hero = Hero(1, "TestHero", 100, 10, 10, 10, 10, 10, 10, 10, 0, 10)
        self.warrior = Warrior(1, "TestWarrior", 100, 10, 10, 10, 10, 10, 10, 10, 0, 10)
        self.mage = Mage(1, "TestMage", 100, 10, 10, 10, 10, 10, 10, 10, 0, 10)
        self.fighter = Fighter(1, "TestFighter", 100, 10, 10, 10, 10, 10, 10, 10, 0, 10)
        self.thief = Thief(1, "TestThief", 100, 10, 10, 10, 10, 10, 10, 10, 0, 10)
        self.priest = Priest(1, "TestPriest", 100, 10, 10, 10, 10, 10, 10, 10, 0, 10)
        self.ninja = Ninja(1, "TestNinja", 100, 10, 10, 10, 10, 10, 10, 10, 0, 10)

    def test_hero_learns_skills(self):
        skill8 = DummySkill("Skill8")
        skill10 = DummySkill("Skill10")
        self.hero.level = 8
        self.hero.learn_skill(skill8)
        self.assertIn(skill8, self.hero.skills)
        self.hero.level = 10
        self.hero.learn_skill(skill10)
        self.assertIn(skill10, self.hero.skills)

    def test_warrior_learns_skills(self):
        skill5 = DummySkill("Skill5")
        skill8 = DummySkill("Skill8")
        self.warrior.level = 5
        self.warrior.learn_skill(skill5)
        self.assertIn(skill5, self.warrior.skills)
        self.warrior.level = 8
        self.warrior.learn_skill(skill8)
        self.assertIn(skill8, self.warrior.skills)

    def test_mage_learns_skills(self):
        skill8 = DummySkill("Skill8")
        skill9 = DummySkill("Skill9")
        self.mage.level = 8
        self.mage.learn_skill(skill8)
        self.assertIn(skill8, self.mage.skills)
        self.mage.level = 9
        self.mage.learn_skill(skill9)
        self.assertIn(skill9, self.mage.skills)

    def test_fighter_learns_skills(self):
        skill8 = DummySkill("Skill8")
        skill9 = DummySkill("Skill9")
        self.fighter.level = 8
        self.fighter.learn_skill(skill8)
        self.assertIn(skill8, self.fighter.skills)
        self.fighter.level = 9
        self.fighter.learn_skill(skill9)
        self.assertIn(skill9, self.fighter.skills)

    def test_thief_learns_skills(self):
        skill3 = DummySkill("Skill3")
        skill9 = DummySkill("Skill9")
        self.thief.level = 3
        self.thief.learn_skill(skill3)
        self.assertIn(skill3, self.thief.skills)
        self.thief.level = 9
        self.thief.learn_skill(skill9)
        self.assertIn(skill9, self.thief.skills)

    def test_priest_learns_skills(self):
        skill5 = DummySkill("Skill5")
        skill9 = DummySkill("Skill9")
        self.priest.level = 5
        self.priest.learn_skill(skill5)
        self.assertIn(skill5, self.priest.skills)
        self.priest.level = 9
        self.priest.learn_skill(skill9)
        self.assertIn(skill9, self.priest.skills)

    def test_ninja_learns_skills(self):
        # Adapte conforme a implementação do Ninja.learn_skill
        skill8 = DummySkill("Skill8")
        self.ninja.level = 8
        self.ninja.learn_skill(skill8)
        self.assertIn(skill8, getattr(self.ninja, "skills", []))

if __name__ == "__main__":
    unittest.main()