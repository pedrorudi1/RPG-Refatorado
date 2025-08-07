import unittest
from Models.Heroes import Hero, Warrior, Mage, Fighter, Thief, Priest, Ninja

class TestHeroes(unittest.TestCase):
    def setUp(self):
        # Cria instâncias das classes com valores altos para testar limites
        self.hero = Hero(1, "TestHero", 9000, 900, 200, 200, 200, 200, 200, 200, 0, 10)
        self.warrior = Warrior(1, "TestWarrior", 9000, 900, 200, 200, 200, 200, 200, 200, 0, 10)
        self.mage = Mage(1, "TestMage", 9000, 900, 200, 200, 200, 200, 200, 200, 0, 10)
        self.fighter = Fighter(1, "TestFighter", 9000, 900, 200, 200, 200, 200, 200, 200,0, 10)
        self.thief = Thief(1, "TestThief", 9000, 900, 200, 200, 200, 200, 200, 200, 0, 10)
        self.priest = Priest(1, "TestPriest", 9000, 900, 200, 200, 200, 200, 200, 200, 0, 10)
        self.ninja = Ninja(1, "TestNinja", 9000, 900, 200, 200, 200, 200, 200, 200, 0, 10)

    def test_max_stats(self):
        # Testa cada personagem após subir vários níveis
        characters = [self.hero, self.warrior, self.mage, self.fighter, 
                     self.thief, self.priest, self.ninja]
        
        # Sobe 100 níveis para garantir que alcance os limites
        for char in characters:
            for _ in range(100):
                char.lvl_up()
            
            # Verifica se os limites máximos são respeitados
            self.assertLessEqual(char.HP, char.MAX_HP)
            self.assertLessEqual(char.MP, char.MAX_MP)
            self.assertLessEqual(char.strenght, char.MAX_STATS)
            self.assertLessEqual(char.magic, char.MAX_STATS)
            self.assertLessEqual(char.vitality, char.MAX_STATS)
            self.assertLessEqual(char.spirit, char.MAX_STATS)
            self.assertLessEqual(char.agility, char.MAX_STATS)
            self.assertLessEqual(char.luck, char.MAX_STATS)

    def test_initial_stats(self):
        # Testa se os status iniciais são atribuídos corretamente
        self.assertEqual(self.hero.name, "TestHero")
        self.assertEqual(self.hero.HP, 9000)
        self.assertEqual(self.hero.MP, 900)
        self.assertEqual(self.hero.strenght, 200)
        
    def test_lists_independence(self):
        # Testa se as listas de magias e habilidades são independentes
        self.hero.magics.append("Magic1")
        self.warrior.magics.append("Magic2")
        
        self.assertNotEqual(self.hero.magics, self.warrior.magics)
        self.assertEqual(len(self.mage.magics), 0)

if __name__ == '__main__':
    unittest.main()