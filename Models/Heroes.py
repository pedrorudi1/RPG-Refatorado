import random
from Magics.MagicsList import *

class Heroes:
    MAX_HP = 9999
    MAX_MP = 999
    MAX_STATS = 255

    def __init__(self, level, name, HP, MP, strenght, magic, vitality, spirit, agility, luck, XP, XP_to_next_level):
        self.level = level
        self.name = name
        self.HP = HP
        self.MP = MP
        self.strenght = strenght
        self.magic = magic
        self.vitality = vitality
        self.spirit = spirit
        self.agility = agility
        self.luck = luck
        self.XP = XP
        self.XP_to_next_level = XP_to_next_level
    
    def equip_weapon(self, weapon):
        self.strenght += weapon.strenght
        self.magic += weapon.magic
        self.agility += weapon.agility
        self.luck += weapon.luck
    
    def equip_armor(self, armor):
        self.HP += armor.HP
        self.MP += armor.MP
        self.vitality += armor.vitality
        self.spirit += armor.spirit
        self.agility += armor.agility
        self.luck += armor.luck

    def equip_accessory(self, accessory):
        self.HP += accessory.HP
        self.MP += accessory.MP
        self.strenght += accessory.strenght
        self.magic += accessory.magic
        self.vitality += accessory.vitality
        self.spirit += accessory.spirit
        self.agility += accessory.agility
        self.luck += accessory.luck

    def use_skill(self, skill):
        self.MP -= skill.MP_cost

    def use_magic(self, magic):
        self.MP -= magic.MP_cost


class Hero(Heroes):
    
    def __init__(self, level, name, HP, MP, strenght, magic, vitality, spirit, agility, luck, XP, XP_to_next_level):
        self.level = level
        self.name = name
        self.HP = HP
        self.MP = MP
        self.strenght = strenght
        self.magic = magic
        self.vitality = vitality
        self.spirit = spirit
        self.agility = agility
        self.luck = luck
        self.XP = XP
        self.XP_to_next_level = XP_to_next_level
        self.magics = []
        self.skills = []
    
    def lvl_up(self):
        self.HP += random.randrange(round((20 + (0.02 * self.luck))), 150)
        if self.HP >= self.MAX_HP:
            self.HP = self.MAX_HP
        self.MP += random.randrange(round((4 + (0.02 * self.luck))), 14)
        if self.MP >= self.MAX_MP:
            self.MP = self.MAX_MP
        self.strenght += random.randrange(round((1 + (0.005 * self.luck))), 6)
        if self.strenght >= self.MAX_STATS:
            self.strenght = self.MAX_STATS
        self.magic += random.randrange(round((1 + (0.005 * self.luck))), 6)
        if self.magic >= self.MAX_STATS:
            self.magic = self.MAX_STATS
        self.vitality += random.randrange(round((1 + (0.005 * self.luck))), 6)
        if self.vitality >= self.MAX_STATS:
            self.vitality = self.MAX_STATS
        self.spirit += random.randrange(round((1 + (0.005 * self.luck))), 5)
        if self.spirit >= self.MAX_STATS:
            self.spirit = self.MAX_STATS
        self.agility += random.randrange(round((1 + (0.005 * self.luck))), 5)
        if self.agility >= self.MAX_STATS:
            self.agility = self.MAX_STATS
        self.luck += random.randrange(round((1 + (0.004 * self.luck))), 4)
        if self.luck >= self.MAX_STATS:
            self.luck = self.MAX_STATS
    
    def gain_xp(self, amount):
        self.XP += amount
        while self.XP >= self.XP_to_next_level and self.level < 99:
            self.XP -= self.XP_to_next_level
            self.level += 1
            self.lvl_up()
            self.XP_to_next_level = int(self.XP_to_next_level * 1.15)


class Warrior(Heroes):
    def __init__(self, level, name, HP, MP, strenght, magic, vitality, spirit, agility, luck, XP, XP_to_next_level):
        self.level = level
        self.name = name
        self.HP = HP
        self.MP = MP
        self.strenght = strenght
        self.magic = magic
        self.vitality = vitality
        self.spirit = spirit
        self.agility = agility
        self.luck = luck
        self.XP = XP
        self.XP_to_next_level = XP_to_next_level
        self.magics = []
        self.skills = []

    def lvl_up(self):
        self.HP += random.randrange(round((20 + (0.02 * self.luck))), 150)
        if self.HP >= self.MAX_HP:
            self.HP = self.MAX_HP
        self.MP += random.randrange(round((2 + (0.02 * self.luck))), 10)
        if self.MP >= self.MAX_MP:
            self.MP = self.MAX_MP
        self.strenght += random.randrange(round((2 + (0.005 * self.luck))), 6)
        if self.strenght >= self.MAX_STATS:
            self.strenght = self.MAX_STATS
        self.magic += random.randrange(round(0.004 * self.luck), 4)
        if self.magic >= self.MAX_STATS:
            self.magic = self.MAX_STATS
        self.vitality += random.randrange(round((1 + (0.005 * self.luck))), 6)
        if self.vitality >= self.MAX_STATS:
            self.vitality = self.MAX_STATS
        self.spirit += random.randrange(round(0.004 * self.luck), 4)
        if self.spirit >= self.MAX_STATS:
            self.spirit = self.MAX_STATS
        self.agility += random.randrange(round((1 + (0.004 * self.luck))), 3)
        if self.agility >= self.MAX_STATS:
            self.agility = self.MAX_STATS
        self.luck += random.randrange(round((1 + (0.004 * self.luck))), 3)
        if self.luck >= self.MAX_STATS:
            self.luck = self.MAX_STATS

    def gain_xp(self, amount):
        self.XP += amount
        while self.XP >= self.XP_to_next_level and self.level < 99:
            self.XP -= self.XP_to_next_level
            self.level += 1
            self.lvl_up()
            self.XP_to_next_level = int(self.XP_to_next_level * 1.15)


class Mage(Heroes):
    def __init__(self, level, name, HP, MP, strenght, magic, vitality, spirit, agility, luck, XP, XP_to_next_level):
        self.level = level
        self.name = name
        self.HP = HP
        self.MP = MP
        self.strenght = strenght
        self.magic = magic
        self.vitality = vitality
        self.spirit = spirit
        self.agility = agility
        self.luck = luck
        self.XP = XP
        self.XP_to_next_level = XP_to_next_level
        self.magics = []
        self.skills = []

    def lvl_up(self):
        self.HP += random.randrange(round((50 + (0.02 * self.luck))), 90)
        if self.HP >= self.MAX_HP:
            self.HP = self.MAX_HP
        self.MP += random.randrange(round((5 + (0.02 * self.luck))), 18)
        if self.MP >= self.MAX_MP:
            self.MP = self.MAX_MP
        self.strenght += random.randrange(round((0.009 * self.luck)), 4)
        if self.strenght >= self.MAX_STATS:
            self.strenght = self.MAX_STATS
        self.magic += random.randrange(round((1 + (0.005 * self.luck))), 6)
        if self.magic >= self.MAX_STATS:
            self.magic = self.MAX_STATS
        self.vitality += random.randrange(round((0.006 * self.luck)), 4)
        if self.vitality >= self.MAX_STATS:
            self.vitality = self.MAX_STATS
        self.spirit += random.randrange(round((1 + (0.005 * self.luck))), 6)
        if self.spirit >= self.MAX_STATS:
            self.spirit = self.MAX_STATS
        self.agility += random.randrange(round((1 + (0.005 * self.luck))), 3)
        if self.agility >= self.MAX_STATS:
            self.agility = self.MAX_STATS
        self.luck += random.randrange(round((1 + (0.005 * self.luck))), 3)
        if self.luck >= self.MAX_STATS:
            self.luck = self.MAX_STATS

    def gain_xp(self, amount):
        self.XP += amount
        while self.XP >= self.XP_to_next_level and self.level < 99:
            self.XP -= self.XP_to_next_level
            self.level += 1
            self.lvl_up()
            self.XP_to_next_level = int(self.XP_to_next_level * 1.15)


class Fighter(Heroes):
    def __init__(self, level, name, HP, MP, strenght, magic, vitality, spirit, agility, luck, XP, XP_to_next_level):
        self.level = level
        self.name = name
        self.HP = HP
        self.MP = MP
        self.strenght = strenght
        self.magic = magic
        self.vitality = vitality
        self.spirit = spirit
        self.agility = agility
        self.luck = luck
        self.XP = XP
        self.XP_to_next_level = XP_to_next_level
        self.magics = []
        self.skills = []

    def lvl_up(self):
        self.HP += random.randrange(round((20 + (0.02 * self.luck))), 140)
        if self.HP >= self.MAX_HP:
            self.HP = self.MAX_HP
        self.MP += random.randrange(round((3 + (0.01 * self.luck))), 15)
        if self.MP >= self.MAX_MP:
            self.MP = self.MAX_MP
        self.strenght += random.randrange(round((1 + (0.004 * self.luck))), 5)
        if self.strenght >= self.MAX_STATS:
            self.strenght = self.MAX_STATS
        self.magic += random.randrange(round((1 + (0.004 * self.luck))), 3)
        if self.magic >= self.MAX_STATS:
            self.magic = self.MAX_STATS
        self.vitality += random.randrange(round((1 + (0.004 * self.luck))), 5)
        if self.vitality >= self.MAX_STATS:
            self.vitality = self.MAX_STATS
        self.spirit += random.randrange(round((1 + (0.003 * self.luck))), 3)
        if self.spirit >= self.MAX_STATS:
            self.spirit = self.MAX_STATS
        self.agility += random.randrange(round((2 + (0.003 * self.luck))), 5)
        if self.agility >= self.MAX_STATS:
            self.agility = self.MAX_STATS
        self.luck += random.randrange(round((1 + (0.005 * self.luck))), 4)
        if self.luck >= self.MAX_STATS:
            self.luck = self.MAX_STATS

    def gain_xp(self, amount):
        self.XP += amount
        while self.XP >= self.XP_to_next_level and self.level < 99:
            self.XP -= self.XP_to_next_level
            self.level += 1
            self.lvl_up()
            self.XP_to_next_level = int(self.XP_to_next_level * 1.15)


class Thief(Heroes):
    def __init__(self, level, name, HP, MP, strenght, magic, vitality, spirit, agility, luck, XP, XP_to_next_level):
        self.level = level
        self.name = name
        self.HP = HP
        self.MP = MP
        self.strenght = strenght
        self.magic = magic
        self.vitality = vitality
        self.spirit = spirit
        self.agility = agility
        self.luck = luck
        self.XP = XP
        self.XP_to_next_level = XP_to_next_level
        self.magics = []
        self.skills = []

    def lvl_up(self):
        self.HP += random.randrange(round((30 + (0.02 * self.luck))), 130)
        if self.HP >= self.MAX_HP:
            self.HP = self.MAX_HP
        self.MP += random.randrange(round((3 + (0.02 * self.luck))), 14)
        if self.MP >= self.MAX_MP:
            self.MP = self.MAX_MP
        self.strenght += random.randrange(round((1 + (0.005 * self.luck))), 5)
        if self.strenght >= self.MAX_STATS:
            self.strenght = self.MAX_STATS
        self.magic += random.randrange(round((1 + (0.004 * self.luck))), 4)
        if self.magic >= self.MAX_STATS:
            self.magic = self.MAX_STATS
        self.vitality += random.randrange(round((1 + (0.005 * self.luck))), 4)
        if self.vitality >= self.MAX_STATS:
            self.vitality = self.MAX_STATS
        self.spirit += random.randrange(round((1 + (0.005 * self.luck))), 4)
        if self.spirit >= self.MAX_STATS:
            self.spirit = self.MAX_STATS
        self.agility += random.randrange(round((1 + (0.01 * self.luck))), 5)
        if self.agility >= self.MAX_STATS:
            self.agility = self.MAX_STATS
        self.luck += random.randrange(round((1 + (0.007 * self.luck))), 4)
        if self.luck >= self.MAX_STATS:
            self.luck = self.MAX_STATS

    def gain_xp(self, amount):
        self.XP += amount
        while self.XP >= self.XP_to_next_level and self.level < 99:
            self.XP -= self.XP_to_next_level
            self.level += 1
            self.lvl_up()
            self.XP_to_next_level = int(self.XP_to_next_level * 1.15)


class Priest(Heroes):
    def __init__(self, level, name, HP, MP, strenght, magic, vitality, spirit, agility, luck, XP, XP_to_next_level):
        self.level = level
        self.name = name
        self.HP = HP
        self.MP = MP
        self.strenght = strenght
        self.magic = magic
        self.vitality = vitality
        self.spirit = spirit
        self.agility = agility
        self.luck = luck
        self.XP = XP
        self.XP_to_next_level = XP_to_next_level
        self.magics = []
        self.skills = []

    def lvl_up(self):
        self.HP += random.randrange(round((40 + (0.02 * self.luck))), 110)
        if self.HP >= self.MAX_HP:
            self.HP = self.MAX_HP
        self.MP += random.randrange(round((5 + (0.02 * self.luck))), 16)
        if self.MP >= self.MAX_MP:
            self.MP = self.MAX_MP
        self.strenght += random.randrange(round((1 + (0.005 * self.luck))), 4)
        if self.strenght >= self.MAX_STATS:
            self.strenght = self.MAX_STATS
        self.magic += random.randrange(round((1 + (0.01 * self.luck))), 5)
        if self.magic >= self.MAX_STATS:
            self.magic = self.MAX_STATS
        self.vitality += random.randrange(round((1 + (0.004 * self.luck))), 5)
        if self.vitality >= self.MAX_STATS:
            self.vitality = self.MAX_STATS
        self.spirit += random.randrange(round((1 + (0.007 * self.luck))), 5)
        if self.spirit >= self.MAX_STATS:
            self.spirit = self.MAX_STATS
        self.agility += random.randrange(round(0.005 * self.luck), 4)
        if self.agility >= self.MAX_STATS:
            self.agility = self.MAX_STATS
        self.luck += random.randrange(round((1 + (0.004 * self.luck))), 3)
        if self.luck >= self.MAX_STATS:
            self.luck = self.MAX_STATS

    def gain_xp(self, amount):
        self.XP += amount
        while self.XP >= self.XP_to_next_level and self.level < 99:
            self.XP -= self.XP_to_next_level
            self.level += 1
            self.lvl_up()
            self.XP_to_next_level = int(self.XP_to_next_level * 1.15)


class Ninja(Heroes):
    def __init__(self, level, name, HP, MP, strenght, magic, vitality, spirit, agility, luck, XP, XP_to_next_level):
        self.level = level
        self.name = name
        self.HP = HP
        self.MP = MP
        self.strenght = strenght
        self.magic = magic
        self.vitality = vitality
        self.spirit = spirit
        self.agility = agility
        self.luck = luck
        self.XP = XP
        self.XP_to_next_level = XP_to_next_level
        self.magics = []
        self.skills = []

    def lvl_up(self):
        self.HP += random.randrange(round((35 + (0.02 * self.luck))), 115)
        if self.HP >= self.MAX_HP:
            self.HP = self.MAX_HP
        self.MP += random.randrange(round((1 + (0.02 * self.luck))), 12)
        if self.MP >= self.MAX_MP:
            self.MP = self.MAX_MP
        self.strenght += random.randrange(round((1 + (0.007 * self.luck))), 5)
        if self.strenght >= self.MAX_STATS:
            self.strenght = self.MAX_STATS
        self.magic += random.randrange(round((1 + (0.004 * self.luck))), 4)
        if self.magic >= self.MAX_STATS:
            self.magic = self.MAX_STATS
        self.vitality += random.randrange(round((1 + (0.005 * self.luck))), 5)
        if self.vitality >= self.MAX_STATS:
            self.vitality = self.MAX_STATS
        self.spirit += random.randrange(round((1 + (0.005 * self.luck))), 4)
        if self.spirit >= self.MAX_STATS:
            self.spirit = self.MAX_STATS
        self.agility += random.randrange(round((1 + (0.007 * self.luck))), 6)
        if self.agility >= self.MAX_STATS:
            self.agility = self.MAX_STATS
        self.luck += random.randrange(round((1 + (0.005 * self.luck))), 4)
        if self.luck >= self.MAX_STATS:
            self.luck = self.MAX_STATS

    def gain_xp(self, amount):
        self.XP += amount
        while self.XP >= self.XP_to_next_level and self.level < 99:
            self.XP -= self.XP_to_next_level
            self.level += 1
            self.lvl_up()
            self.XP_to_next_level = int(self.XP_to_next_level * 1.15)