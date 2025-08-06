from abc import ABC, abstractmethod

class Personagens:
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

