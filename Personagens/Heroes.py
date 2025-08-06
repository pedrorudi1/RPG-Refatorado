from Personagens import Personagens
import random

class Hero(Personagens):
    
    def __init__(self, name, HP, MP, strenght, magic, vitality, spirit, agility, luck):
        self.name = name
        self.HP = HP
        self.MP = MP
        self.strenght = strenght
        self.magic = magic
        self.vitality = vitality
        self.spirit = spirit
        self.agility = agility
        self.luck = luck
        self.magics = []
        self.skills = []
    
    def lvl_up(self):
        self.HP = min(random.randrange(round((5 + (0.02 * self.luck))), 16), self.MAX_HP)
        self.MP = min(random.randrange(round((3 + (0.02 * self.luck))), 10), self.MAX_MP)
        self.strenght = min(random.randrange(round((2 + (0.02 * self.luck))), 10), self.MAX_STATS)
        self.magic = min(random.randrange(round((2 + (0.02 * self.luck))), 10), self.MAX_STATS)
        self.vitality = min(random.randrange(round((2 + (0.02 * self.luck))), 11), self.MAX_STATS)
        self.spirit = min(random.randrange(round((2 + (0.02 * self.luck))), 10), self.MAX_STATS)
        self.agility = min(random.randrange(round((2 + (0.02 * self.luck))), 9), self.MAX_STATS)
        self.luck = min(random.randrange(round((1 + (0.01 * self.luck))), 6), self.MAX_STATS)


class Warrior(Personagens):
    def __init__(self, name, HP, MP, strenght, magic, vitality, spirit, agility, luck):
        self.name = name
        self.HP = HP
        self.MP = MP
        self.strenght = strenght
        self.magic = magic
        self.vitality = vitality
        self.spirit = spirit
        self.agility = agility
        self.luck = luck
        self.magics = []
        self.skills = []

    def lvl_up(self):
        self.HP = min(random.randrange(round((5 + (0.02 * self.luck))), 17), self.MAX_HP)
        self.MP = min(random.randrange(round((1 + (0.02 * self.luck))), 8), self.MAX_MP)
        self.strenght = min(random.randrange(round((2 + (0.02 * self.luck))), 17), self.MAX_STATS)
        self.magic = min(random.randrange(round((1 + (0.005 * self.luck))), 6), self.MAX_STATS)
        self.vitality = min(random.randrange(round((2 + (0.02 * self.luck))), 13), self.MAX_STATS)
        self.spirit = min(random.randrange(round((2 + (0.01 * self.luck))), 8), self.MAX_STATS)
        self.agility = min(random.randrange(round((2 + (0.02 * self.luck))), 9), self.MAX_STATS)
        self.luck = min(random.randrange(round((1 + (0.01 * self.luck))), 6), self.MAX_STATS)


class Mage(Personagens):
    def __init__(self, name, HP, MP, strenght, magic, vitality, spirit, agility, luck):
        self.name = name
        self.HP = HP
        self.MP = MP
        self.strenght = strenght
        self.magic = magic
        self.vitality = vitality
        self.spirit = spirit
        self.agility = agility
        self.luck = luck
        self.magics = []
        self.skills = []

    def lvl_up(self):
        self.HP = min(random.randrange(round((3 + (0.02 * self.luck))), 12), self.MAX_HP)
        self.MP = min(random.randrange(round((5 + (0.02 * self.luck))), 18), self.MAX_MP)
        self.strenght = min(random.randrange(round((1 + (0.01 * self.luck))), 6), self.MAX_STATS) 
        self.magic = min(random.randrange(round((5 + (0.02 * self.luck))), 18), self.MAX_STATS)
        self.vitality = min(random.randrange(round((2 + (0.02 * self.luck))), 10), self.MAX_STATS)
        self.spirit = min(random.randrange(round((3 + (0.02 * self.luck))), 12), self.MAX_STATS)
        self.agility = min(random.randrange(round((2 + (0.02 * self.luck))), 8), self.MAX_STATS)
        self.luck = min(random.randrange(round((1 + (0.01 * self.luck))), 6), self.MAX_STATS)


class Fighter(Personagens):
    def __init__(self, name, HP, MP, strenght, magic, vitality, spirit, agility, luck):
        self.name = name
        self.HP = HP
        self.MP = MP
        self.strenght = strenght
        self.magic = magic
        self.vitality = vitality
        self.spirit = spirit
        self.agility = agility
        self.luck = luck
        self.magics = []
        self.skills = []

    def lvl_up(self):
        self.HP = min(random.randrange(round((4 + (0.02 * self.luck))), 15), self.MAX_HP)
        self.MP = min(random.randrange(round((2 + (0.02 * self.luck))), 9), self.MAX_MP)
        self.strenght = min(random.randrange(round((3 + (0.02 * self.luck))), 17), self.MAX_STATS)
        self.magic = min(random.randrange(round((1 + (0.01 * self.luck))), 6), self.MAX_STATS)
        self.vitality = min(random.randrange(round((3 + (0.02 * self.luck))), 12), self.MAX_STATS)
        self.spirit = min(random.randrange(round((2 + (0.02 * self.luck))), 9), self.MAX_STATS)
        self.agility = min(random.randrange(round((2 + (0.02 * self.luck))), 13), self.MAX_STATS)
        self.luck = min(random.randrange(round((1 + (0.01 * self.luck))), 6), self.MAX_STATS)


class Thief(Personagens):
    def __init__(self, name, HP, MP, strenght, magic, vitality, spirit, agility, luck):
        self.name = name
        self.HP = HP
        self.MP = MP
        self.strenght = strenght
        self.magic = magic
        self.vitality = vitality
        self.spirit = spirit
        self.agility = agility
        self.luck = luck
        self.magics = []
        self.skills = []

    def lvl_up(self):
        self.HP = min(random.randrange(round((4 + (0.02 * self.luck))), 14), self.MAX_HP)
        self.MP = min(random.randrange(round((3 + (0.02 * self.luck))), 10), self.MAX_MP)
        self.strenght = min(random.randrange(round((2 + (0.02 * self.luck))), 10), self.MAX_STATS)
        self.magic = min(random.randrange(round((2 + (0.02 * self.luck))), 9), self.MAX_STATS)
        self.vitality = min(random.randrange(round((2 + (0.02 * self.luck))), 10), self.MAX_STATS)
        self.spirit = min(random.randrange(round((2 + (0.02 * self.luck))), 9), self.MAX_STATS)
        self.agility = min(random.randrange(round((3 + (0.02 * self.luck))), 15), self.MAX_STATS)
        self.luck = min(random.randrange(round((1 + (0.01 * self.luck))), 8), self.MAX_STATS)


class Priest(Personagens):
    def __init__(self, name, HP, MP, strenght, magic, vitality, spirit, agility, luck):
        self.name = name
        self.HP = HP
        self.MP = MP
        self.strenght = strenght
        self.magic = magic
        self.vitality = vitality
        self.spirit = spirit
        self.agility = agility
        self.luck = luck
        self.magics = []
        self.skills = []

    def lvl_up(self):
        self.HP = min(random.randrange(round((3 + (0.02 * self.luck))), 13), self.MAX_HP)
        self.MP = min(random.randrange(round((5 + (0.02 * self.luck))), 17), self.MAX_MP)
        self.strenght = min(random.randrange(round((1 + (0.01 * self.luck))), 7), self.MAX_STATS)
        self.magic = min(random.randrange(round((4 + (0.02 * self.luck))), 15), self.MAX_STATS)
        self.vitality = min(random.randrange(round((2 + (0.02 * self.luck))), 10), self.MAX_STATS)
        self.spirit = min(random.randrange(round((4 + (0.02 * self.luck))), 14), self.MAX_STATS)
        self.agility = min(random.randrange(round((2 + (0.02 * self.luck))), 9), self.MAX_STATS)
        self.luck = min(random.randrange(round((1 + (0.01 * self.luck))), 6), self.MAX_STATS)


class Ninja(Personagens):
    def __init__(self, name, HP, MP, strenght, magic, vitality, spirit, agility, luck):
        self.name = name
        self.HP = HP
        self.MP = MP
        self.strenght = strenght
        self.magic = magic
        self.vitality = vitality
        self.spirit = spirit
        self.agility = agility
        self.luck = luck
        self.magics = []
        self.skills = []

    def lvl_up(self):
        self.HP = min(random.randrange(round((4 + (0.02 * self.luck))), 15), self.MAX_HP)
        self.MP = min(random.randrange(round((2 + (0.02 * self.luck))), 9), self.MAX_MP)
        self.strenght = min(random.randrange(round((3 + (0.02 * self.luck))), 15), self.MAX_STATS)
        self.magic = min(random.randrange(round((1 + (0.01 * self.luck))), 6), self.MAX_STATS)
        self.vitality = min(random.randrange(round((3 + (0.02 * self.luck))), 11), self.MAX_STATS)
        self.spirit = min(random.randrange(round((2 + (0.02 * self.luck))), 9), self.MAX_STATS)
        self.agility = min(random.randrange(round((2 + (0.02 * self.luck))), 13), self.MAX_STATS)
        self.luck = min(random.randrange(round((1 + (0.01 * self.luck))), 6), self.MAX_STATS)