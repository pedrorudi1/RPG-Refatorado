class AttackMagic:
    def __init__(self, name, strength, target, element):
        self.name = name
        self.strength = strength
        self.target = target
        self.element = element


class HealMagic:
    def __init__(self, name, strength, target):
        self.name = name
        self.strength = strength
        self.target = target


class SupportMagic:
    def __init__(self, name, effect, target):
        self.name = name
        self.effect = effect
        self.target = target


class BuffMagic:
    def __init__(self, name, attribute, increase, duration):
        self.name = name
        self.attribute = attribute
        self.increase = increase
        self.duration = duration


class DebuffMagic:
    def __init__(self, name, attribute, decrease, duration):
        self.name = name
        self.attribute = attribute
        self.decrease = decrease
        self.duration = duration


class SummonMagic:
    def __init__(self, name, creature, strength, element):
        self.name = name
        self.creature = creature
        self.strenght = strength
        self.element = element


