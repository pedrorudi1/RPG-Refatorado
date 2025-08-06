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

    @abstractmethod
    def equip_weapon(self, weapon):
        pass

    @abstractmethod
    def equip_armor(self, armor):
        pass

    @abstractmethod
    def equip_accessory(self, accessory):
        pass

    @abstractmethod
    def use_skill(self, skill):
        pass

    @abstractmethod
    def use_magic(self, spell):
        pass
    
    @abstractmethod
    def level_up(self):
        pass
