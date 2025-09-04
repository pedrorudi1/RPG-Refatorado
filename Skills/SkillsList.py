import random
from Skills.SkillsClass import Skill


#Hero Skills
slash = Skill("Slash", 1.15, "Single Enemy", "Physical Damage")
double_slash = Skill("Double Slash", 0.75, "Single Enemy", "Hits Twice")
power_slash = Skill("Power Slash", 1.5, "Single Enemy", "Physical Damage")
slash_all = Skill("Slash All", 0.9, "All Enemies", "Physical Damage")
critical_strike = Skill("Critical Strike", 2.0, "Single Enemy", "High Physical Damage")
heal = Skill("Heal", 1.2, "Single Ally", "Restores HP")
heal_all = Skill("Heal All", 0.8, "All Allies", "Restores HP")


#Warrior Skills
bash = Skill("Bash", 1.25, "Single Enemy", "Physical Damage")
war_cry = Skill("War Cry", 1.35, "Self", "Boosts Attack")
defensive_stance = Skill("Defensive Stance", 1.35, "Single Ally", "Boosts Defense")
cover = Skill("Cover", 0, "Single Ally", "Takes Damage for an Ally")
retaliate = Skill("Retaliate", 0, "Self", "Counterattacks when hit")
war_shout = Skill("War Shout", 1.35, "All Allies", "Boosts Attack")
maximum_impact = Skill("Maximum Impact", 2.5, "Single Enemy", "Massive Physical Damage")


#Mage Skills
mind_boost = Skill("Mind Boost", 1.25, "Self", "Boosts Magic Power")
spirit_boost = Skill("Spirit Boost", 1.25, "Self", "Boosts Magic Defense")
elemental_strike = Skill("Elemental Strike", 1.3, "Single Enemy", "Magic Damage")
firewall = Skill("Firewall", 1.35, "All", "Fire Damage")
kabum = Skill("Kabum", 1.35, "All", "Explodes a Group of Enemies")
blessing = Skill("Blessing", 1.25, "All Allies", "Boosts Group Spirit")
study = Skill("Study", random.randrange(15, 50), "Self", "Recovers MP")


#Fighter Skills
power_punch = Skill("Power Punch", 1.3, "Single Enemy", "Physical Damage")
fury_swipes = Skill("Fury Swipes", 0.5, "Single Enemy", "Hits Multiple Times")
iron_fist = Skill("Iron Fist", 1.4, "Single Enemy", "Physical Damage")
adrenaline_rush = Skill("Adrenaline Rush", 1.25, "Self", "Boosts Attack")
tough_skin = Skill("Tough Skin", 1.25, "Self", "Boosts Defense")
head_butt = Skill("Head Butt", 1.6, "Single Enemy", "High Physical Damage")
final_blow = Skill("Final Blow", 2.0, "Single Enemy", "Massive Physical Damage")


#Thief Skills
steal = Skill("Steal", 0, "Single Enemy", "Steals an Item")
backstab = Skill("Backstab", 1.5, "Single Enemy", "High Physical Damage")
poison_dart = Skill("Poison Dart", 1.2, "Single Enemy", "Poisons the Target")
mug = Skill("Mug", 1.3, "Single Enemy", "Steals an Item and Deals Damage")
evasion = Skill("Evasion", 1.25, "Self", "Boosts Evasion")
quick_strike = Skill("Quick Strike", 1.3, "Single Enemy", "Physical Damage")
shadow_step = Skill("Shadow Step", 1.4, "Single Enemy", "Physical Damage")
assassinate = Skill("Assassinate", 2.5, "Single Enemy", "Massive Physical Damage")


#Priest Skills
cure = Skill("Cure", 1.2, "Single Ally", "Restores HP")
cure_all = Skill("Cure All", 0.8, "All Allies", "Restores HP")
holy_light = Skill("Holy Light", 1.3, "Single Enemy", "Holy Damage")
divine_shield = Skill("Divine Shield", 1.25, "Self", "Boosts Magic Defense")
protect = Skill("Protect", 1.25, "Self", "Boosts Defense")
resurrect = Skill("Resurrect", 0, "Single Ally", "Revives a Fallen Ally")
sanctuary = Skill("Sanctuary", 1.7, "All Allies", "Restores HP")
judgment = Skill("Judgment", 2.5, "Single Enemy", "Massive Holy Damage")


#Ninja Skills
shuriken_throw = Skill("Shuriken Throw", 1.2, "Single Enemy", "Physical Damage")
shadow_clone = Skill("Shadow Clone", 1.25, "Self", "Boosts Evasion")
quick_slash = Skill("Quick Slash", 1.35, "Single Enemy", "Physical Damage")
silent_kill = Skill("Silent Kill", 1.75, "Single Enemy", "Heavy Physical Damage")
ultimate_technique = Skill("Ultimate Technique", 2.75, "Single Enemy", "Massive Physical Damage")

list_of_skills = [slash, double_slash, power_slash, slash_all, critical_strike, heal, heal_all,
                  bash, war_cry, defensive_stance, cover, retaliate, war_shout, maximum_impact,
                  mind_boost, spirit_boost, elemental_strike, firewall, kabum, blessing, study,
                  power_punch, fury_swipes, iron_fist, adrenaline_rush, tough_skin, head_butt, final_blow,
                  steal, backstab, poison_dart, mug, evasion, quick_strike, shadow_step, assassinate,
                  cure, cure_all, holy_light, divine_shield, protect, resurrect, sanctuary, judgment,
                  shuriken_throw, shadow_clone, quick_slash, silent_kill, ultimate_technique]