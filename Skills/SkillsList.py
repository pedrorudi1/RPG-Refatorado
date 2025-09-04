import random
from Skills import SkillsClass
from Models.Heroes import HeroesClass, Warrior, Mage, Fighter, Thief, Priest, Ninja

#Hero Skills
slash = SkillsClass.Skill("Slash", 1.15, "Single Enemy", "Physical Damage")
double_slash = SkillsClass.Skill("Double Slash", 0.75, "Single Enemy", "Hits Twice")
power_slash = SkillsClass.Skill("Power Slash", 1.5, "Single Enemy", "Physical Damage")
slash_all = SkillsClass.Skill("Slash All", 0.9, "All Enemies", "Physical Damage")
critical_strike = SkillsClass.Skill("Critical Strike", 2.0, "Single Enemy", "High Physical Damage")
heal = SkillsClass.Skill("Heal", 1.2, "Single Ally", "Restores HP")
heal_all = SkillsClass.Skill("Heal All", 0.8, HeroesClass.HP, "Restores HP")


#Warrior Skills
bash = SkillsClass.Skill("Bash", 1.25, "Single Enemy", "Physical Damage")
war_cry = SkillsClass.Skill("War Cry", 1.35, Warrior.strenght, "Boosts Attack")
defensive_stance = SkillsClass.Skill("Defensive Stance", 1.35, Warrior.defense, "Boosts Defense")
cover = SkillsClass.Skill("Cover", 0, "Single Ally", "Takes Damage for an Ally")
retaliate = SkillsClass.Skill("Retaliate", 0, Warrior, "Counterattacks when hit")
war_shout = SkillsClass.Skill("War Shout", 1.35, HeroesClass.strenght, "Boosts Attack")
maximum_impact = SkillsClass.Skill("Maximum Impact", 2.5, "Single Enemy", "Massive Physical Damage")


#Mage Skills
mind_boost = SkillsClass.Skill("Mind Boost", 1.25, Mage.magic, "Boosts Magic Power")
spirit_boost = SkillsClass.Skill("Spirit Boost", 1.25, Mage.spirit, "Boosts Magic Defense")
elemental_strike = SkillsClass.Skill("Elemental Strike", 1.3, "Single Enemy", "Magic Damage")
firewall = SkillsClass.Skill("Firewall", 1.35, "All", "Fire Damage")
kabum = SkillsClass.Skill("Kabum", 1.35, "All", "Explodes a Group of Enemies")
blessing = SkillsClass.Skill("Blessing", 1.25, HeroesClass.spirit, "Boosts Group Spirit")
study = SkillsClass.Skill("Study", random.randrange(15, 50), Mage.MP, "Recovers MP")


#Fighter Skills
power_punch = SkillsClass.Skill("Power Punch", 1.3, "Single Enemy", "Physical Damage")
fury_swipes = SkillsClass.Skill("Fury Swipes", 0.5, "Single Enemy", "Hits Multiple Times")
iron_fist = SkillsClass.Skill("Iron Fist", 1.4, "Single Enemy", "Physical Damage")
adrenaline_rush = SkillsClass.Skill("Adrenaline Rush", 1.25, Fighter.strenght, "Boosts Attack")
tough_skin = SkillsClass.Skill("Tough Skin", 1.25, Fighter.defense, "Boosts Defense")
head_butt = SkillsClass.Skill("Head Butt", 1.6, "Single Enemy", "High Physical Damage")
final_blow = SkillsClass.Skill("Final Blow", 2.0, "Single Enemy", "Massive Physical Damage")


#Thief Skills
steal = SkillsClass.Skill("Steal", 0, "Single Enemy", "Steals an Item")
backstab = SkillsClass.Skill("Backstab", 1.5, "Single Enemy", "High Physical Damage")
poison_dart = SkillsClass.Skill("Poison Dart", 1.2, "Single Enemy", "Poisons the Target")
mug = SkillsClass.Skill("Mug", 1.3, "Single Enemy", "Steals an Item and Deals Damage")
evasion = SkillsClass.Skill("Evasion", 1.25, Thief.agility, "Boosts Evasion")
quick_strike = SkillsClass.Skill("Quick Strike", 1.3, "Single Enemy", "Physical Damage")
shadow_step = SkillsClass.Skill("Shadow Step", 1.4, "Single Enemy", "Physical Damage")
assassinate = SkillsClass.Skill("Assassinate", 2.5, "Single Enemy", "Massive Physical Damage")


#Priest Skills
cure = SkillsClass.Skill("Cure", 1.2, "Single Ally", "Restores HP")
cure_all = SkillsClass.Skill("Cure All", 0.8, "All Allies", "Restores HP")
holy_light = SkillsClass.Skill("Holy Light", 1.3, "Single Enemy", "Holy Damage")
divine_shield = SkillsClass.Skill("Divine Shield", 1.25, Priest.spirit, "Boosts Magic Defense")
protect = SkillsClass.Skill("Protect", 1.25, Priest.defense, "Boosts Defense")
resurrect = SkillsClass.Skill("Resurrect", 0, "Single Ally", "Revives a Fallen Ally")
sanctuary = SkillsClass.Skill("Sanctuary", 1.7, "All Allies", "Restores HP")
judgment = SkillsClass.Skill("Judgment", 2.5, "Single Enemy", "Massive Holy Damage")


#Ninja Skills
shuriken_throw = SkillsClass.Skill("Shuriken Throw", 1.2, "Single Enemy", "Physical Damage")
shadow_clone = SkillsClass.Skill("Shadow Clone", 1.25, Ninja.agility, "Boosts Evasion")
quick_slash = SkillsClass.Skill("Quick Slash", 1.35, "Single Enemy", "Physical Damage")
silent_kill = SkillsClass.Skill("Silent Kill", 1.75, "Single Enemy", "Heavy Physical Damage")
ultimate_technique = SkillsClass.Skill("Ultimate Technique", 2.75, "Single Enemy", "Massive Physical Damage")

