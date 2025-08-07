class Enemy:
    def __init__(self, name, HP, MP, strenght, magic, vitality, spirit, agility, luck, given_xp, given_gold, vulnerability):
        self.name = name
        self.HP = HP
        self.MP = MP
        self.strenght = strenght
        self.magic = magic
        self.vitality = vitality
        self.spirit = spirit
        self.agility = agility
        self.luck = luck
        self.given_xp = given_xp
        self.given_gold = given_gold
        self.vulnerability = vulnerability
        self.magics = []
        self.skills = []