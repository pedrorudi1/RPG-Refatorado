from Personagens import Personagens
import random

class Hero(Personagens):
    def __init__(self, classe, name, HP, MP, strenght, magic, vitality, spirit, agility, luck):
        self.classe = classe
        self.name = name
        self.HP = HP
        self.MP = MP
        self.strenght = strenght
        self.magic = magic
        self.vitality = vitality
        self.spirit = spirit
        self.agility = agility
        self.luck = luck
    
    def lvl_up(self):
        self.HP += round(random.randrange((5 + (0.02 * self.luck)), 15))
        self.MP += round(random.randrange((3 + (0.02 * self.luck)), 9))
        self.strenght += round(random.randrange((2 + (0.02 * self.luck)), 10))
        self.magic += round(random.randrange((2 + (0.02 * self.luck)), 9))
        self.vitality += round(random.randrange((2 + (0.02 * self.luck)), 10))
        self.spirit += round(random.randrange((2 + (0.02 * self.luck)), 9))
        self.agility += round(random.randrange((2 + (0.02 * self.luck)), 8))
        self.luck += round(random.randrange((1 + (0.01 * self.luck)), 5))