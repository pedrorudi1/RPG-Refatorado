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
        self.HP += random.randrange(round((5 + (0.02 * self.luck))), 16)
        self.MP += random.randrange(round((3 + (0.02 * self.luck))), 10)
        self.strenght += random.randrange(round((2 + (0.02 * self.luck))), 9)
        self.magic += random.randrange(round((2 + (0.02 * self.luck))), 10)
        self.vitality += random.randrange(round((2 + (0.02 * self.luck))), 11)
        self.spirit += random.randrange(round((2 + (0.02 * self.luck))), 10)
        self.agility += random.randrange(round((2 + (0.02 * self.luck))), 9)
        self.luck += random.randrange(round((1 + (0.01 * self.luck))), 6)

