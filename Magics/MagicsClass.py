
class AttackMagic:
    def __init__(self, name: str, strength: float, target: enumerate, element: str):
        self.name = name
        self.strength = strength
        self.target = target
        self.element = element


class HealMagic:
    def __init__(self, name: str, strength: float, target: enumerate):
        self.name = name
        self.strength = strength
        self.target = target


class BuffMagic:
    def __init__(self, name: str, attribute: int, increase: float, duration: int):
        self.name = name
        self.attribute = attribute
        self.increase = increase
        self.duration = duration


class DebuffMagic:
    def __init__(self, name: str, attribute: int, decrease: float, duration: int):
        self.name = name
        self.attribute = attribute
        self.decrease = decrease
        self.duration = duration


class SummonMagic:
    def __init__(self, name: str, creature: str, strength: float, target: str, element: str):
        self.name = name
        self.creature = creature
        self.strenght = strength
        self.target = target
        self.element = element
