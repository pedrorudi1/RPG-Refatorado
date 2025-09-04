import random


class HeroesClass:
    
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

    def list_skills(self):
        return [skill.name for skill in self.skills]


class Hero(HeroesClass):
    
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
        from Skills.SkillsList import slash, double_slash, power_slash, slash_all, critical_strike, heal, heal_all as skills
        self.learn_skill(skills)
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
        self.list_skills()

    def gain_xp(self, amount):
        self.XP += amount
        while self.XP >= self.XP_to_next_level and self.level < 99:
            self.XP -= self.XP_to_next_level
            self.level += 1
            self.lvl_up()
            self.XP_to_next_level = int(self.XP_to_next_level * 1.15)

    def learn_skill(self):
        from Skills.SkillsList import slash, double_slash, power_slash, slash_all, critical_strike, heal, heal_all

        if self.level >= 8 and slash not in self.skills:
            self.skills.append(slash)
        if self.level >= 10 and heal not in self.skills:
            self.skills.append(heal)
        if self.level >= 12 and double_slash not in self.skills:
            self.skills.append(double_slash)
        if self.level >= 18 and power_slash not in self.skills:
            self.skills.append(power_slash)
        if self.level >= 25 and slash_all not in self.skills:
            self.skills.append(slash_all)
        if self.level >= 30 and heal_all not in self.skills:
            self.skills.append(heal_all)
        if self.level >= 35 and critical_strike not in self.skills:
            self.skills.append(critical_strike)


class Warrior(HeroesClass):

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

    def learn_skill(self, skill):
        from Skills.SkillsList import cover, bash, war_cry, defensive_stance, retaliate, war_shout, maximum_impact

        if self.level >= 5 and skill not in self.skills:
            self.skills.append(cover)
        if self.level >= 8 and skill not in self.skills:
            self.skills.append(bash)
        if self.level >= 10 and skill not in self.skills:
            self.skills.append(war_cry)
        if self.level >= 18 and skill not in self.skills:
            self.skills.append(defensive_stance)
        if self.level >= 25 and skill not in self.skills:
            self.skills.append(retaliate)
        if self.level >= 31 and skill not in self.skills:
            self.skills.append(war_shout)
        if self.level >= 39 and skill not in self.skills:
            self.skills.append(maximum_impact)


class Mage(HeroesClass):
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

    def learn_skill(self, skill):
        from Skills.SkillsList import mind_boost, spirit_boost, elemental_strike, firewall, kabum, blessing, study

        if self.level >= 8 and skill not in self.skills:
            self.skills.append(mind_boost)
        if self.level >= 9 and skill not in self.skills:
            self.skills.append(spirit_boost)
        if self.level >= 12 and skill not in self.skills:
            self.skills.append(elemental_strike)
        if self.level >= 18 and skill not in self.skills:
            self.skills.append(firewall)
        if self.level >= 25 and skill not in self.skills:
            self.skills.append(study)
        if self.level >= 28 and skill not in self.skills:
            self.skills.append(blessing)
        if self.level >= 39 and skill not in self.skills:
            self.skills.append(kabum)


class Fighter(HeroesClass):
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

    def learn_skill(self, skill):
        from Skills.SkillsList import power_punch, fury_swipes, iron_fist, adrenaline_rush, tough_skin, head_butt, final_blow

        if self.level >= 8 and skill not in self.skills:
            self.skills.append(power_punch)
        if self.level >= 9 and skill not in self.skills:
            self.skills.append(fury_swipes)
        if self.level >= 12 and skill not in self.skills:
            self.skills.append(iron_fist)
        if self.level >= 18 and skill not in self.skills:
            self.skills.append(adrenaline_rush)
        if self.level >= 25 and skill not in self.skills:
            self.skills.append(tough_skin)
        if self.level >= 28 and skill not in self.skills:
            self.skills.append(head_butt)
        if self.level >= 39 and skill not in self.skills:
            self.skills.append(final_blow)


class Thief(HeroesClass):
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

    def learn_skill(self, skill):
        from Skills.SkillsList import steal, backstab, poison_dart, mug, evasion, quick_strike, shadow_step, assassinate

        if self.level >= 3 and skill not in self.skills:
            self.skills.append(steal)
        if self.level >= 9 and skill not in self.skills:
            self.skills.append(backstab)
        if self.level >= 12 and skill not in self.skills:
            self.skills.append(poison_dart)
        if self.level >= 20 and skill not in self.skills:
            self.skills.append(mug)
        if self.level >= 25 and skill not in self.skills:
            self.skills.append(evasion)
        if self.level >= 28 and skill not in self.skills:
            self.skills.append(quick_strike)
        if self.level >= 39 and skill not in self.skills:
            self.skills.append(shadow_step)
        if self.level >= 45 and skill not in self.skills:
            self.skills.append(assassinate)

class Priest(HeroesClass):
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

    def learn_skill(self, skill):
        from Skills.SkillsList import cure, cure_all, holy_light, divine_shield, protect, resurrect, sanctuary, judgment

        if self.level >= 5 and skill not in self.skills:
            self.skills.append(cure)
        if self.level >= 9 and skill not in self.skills:
            self.skills.append(divine_shield)
        if self.level >= 12 and skill not in self.skills:
            self.skills.append(protect)
        if self.level >= 18 and skill not in self.skills:
            self.skills.append(resurrect)
        if self.level >= 25 and skill not in self.skills:
            self.skills.append(cure_all)
        if self.level >= 28 and skill not in self.skills:
            self.skills.append(holy_light)
        if self.level >= 39 and skill not in self.skills:
            self.skills.append(sanctuary)
        if self.level >= 45 and skill not in self.skills:
            self.skills.append(judgment)

class Ninja(HeroesClass):
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

    def learn_skill(self, skill):
        from Skills.SkillsList import shuriken_throw, shadow_clone, quick_slash, silent_kill, ultimate_technique

        if self.level >= 5 and skill not in self.skills:
            self.skills.append(shuriken_throw)
        if self.level >= 9 and skill not in self.skills:
            self.skills.append(shadow_clone)
        if self.level >= 18 and skill not in self.skills:
            self.skills.append(quick_slash)
        if self.level >= 28 and skill not in self.skills:
            self.skills.append(silent_kill)
        if self.level >= 41 and skill not in self.skills:
            self.skills.append(ultimate_technique)