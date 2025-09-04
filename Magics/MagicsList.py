import MagicsClass
from Models import Heroes, Enemies

# Attack Magics
fireball = MagicsClass.AttackMagic("Fireball", 1.1, "Single", "Fire")
fireblast = MagicsClass.AttackMagic("Fireblast", 1.25, "Single", "Fire")
explosion = MagicsClass.AttackMagic("Explosion", 1.75, "All", "Fire")
iceshard = MagicsClass.AttackMagic("Ice Shard", 1.0, "Single", "Ice")
frost = MagicsClass.AttackMagic("Frost", 1.25, "Single", "Ice")
blizzard = MagicsClass.AttackMagic("Blizzard", 1.75, "All", "Ice")
thunder = MagicsClass.AttackMagic("Thunder", 1.0, "Single", "Lightning")
thunderbolt = MagicsClass.AttackMagic("Thunder Bolt", 1.25, "Single", "Lightning")
thunderstorm = MagicsClass.AttackMagic("Thunder Storm", 1.75, "All", "Lightning")
quake = MagicsClass.AttackMagic("Quake", 1.0, "All", "Earth")
earthquake = MagicsClass.AttackMagic("Earthquake", 1.35, "All", "Earth")
wind = MagicsClass.AttackMagic("Wind", 1.2, "Single", "Wind")
tornado = MagicsClass.AttackMagic("Tornado", 1.45, "All", "Wind")
holy = MagicsClass.AttackMagic("Holy", 2.0, "Single", "Light")
dark = MagicsClass.AttackMagic("Dark", 2.0, "Single", "Dark")
comet = MagicsClass.AttackMagic("Comet", 1.75, "Single", "Non-Elemental")
meteor = MagicsClass.AttackMagic("Meteor", 2.5, "All", "Non-Elemental")
ultima = MagicsClass.AttackMagic("Ultima", 3.0, "All", "Non-Elemental")


# Heal Magics
cure = MagicsClass.HealMagic("Cure", 1.0, "Single")
cura = MagicsClass.HealMagic("Cura", 1.5, "Single")
curaga = MagicsClass.HealMagic("Curaga", 2.0, "All")
regen = MagicsClass.HealMagic("Regen", 0.5, "Single")
regen_all = MagicsClass.HealMagic("Regen All", 0.5, "All")
esuna = MagicsClass.HealMagic("Esuna", 0, "Single")
revive = MagicsClass.HealMagic("Revive", 0, "Single")
revive_all = MagicsClass.HealMagic("Revive All", 0, "All")


# Buff Magics
protect = MagicsClass.BuffMagic("Protect", Heroes.vitality, 1.35, 3)
shell = MagicsClass.BuffMagic("Shell", Heroes.spirit, 1.35, 3)
haste = MagicsClass.BuffMagic("Haste", Heroes.agility, 1.35, 3)
bravery = MagicsClass.BuffMagic("Bravery", Heroes.strenght, 1.25, 3)
faith = MagicsClass.BuffMagic("Faith", Heroes.magic, 1.25, 3)
reflect = MagicsClass.BuffMagic("Reflect", "Magic Reflect", 1.0, 3)

# Debuff Magics
slow = MagicsClass.DebuffMagic("Slow", Enemies.agility, 0.75, 3)
weak = MagicsClass.DebuffMagic("Weak", Enemies.strenght, 0.75, 3)
silence = MagicsClass.DebuffMagic("Silence", Enemies.magic, 0.0, 3)
poison = MagicsClass.DebuffMagic("Poison", Enemies.HP, 0.9, 3)
blind = MagicsClass.DebuffMagic("Blind", Enemies.luck, 0.5, 3)
sleep = MagicsClass.DebuffMagic("Sleep", Enemies.HP, 0.0, 2)
death = MagicsClass.DebuffMagic("Death", Enemies.HP, 0.0, 1)


# Summon Magics
ifrit = MagicsClass.SummonMagic("Ifrit", "Ifrit", 2.0, "All", "Fire")
shiva = MagicsClass.SummonMagic("Shiva", "Shiva", 2.0, "All", "Ice")
ramuh = MagicsClass.SummonMagic("Ramuh", "Ramuh", 2.0, "All", "Lightning")
gaia = MagicsClass.SummonMagic("Gaia", "Gaia", 2.0, "All", "Earth")
leviathan = MagicsClass.SummonMagic("Leviathan", "Leviathan", 2.0, "All", "Ice")
siren = MagicsClass.SummonMagic("Siren", "Siren", 2.0, "All", "Wind")
phoenix = MagicsClass.SummonMagic("Phoenix", "Phoenix", 2.0, "All", "Fire")
baldur = MagicsClass.SummonMagic("Baldur", "Baldur", 3.5, "All", "Light")
hades = MagicsClass.SummonMagic("Hades", "Hades", 3.5, "All", "Dark")
bahamut = MagicsClass.SummonMagic("Bahamut", "Bahamut", 3.5, "All", "Non-Elemental")
devil = MagicsClass.SummonMagic("Devil", "Devil", 3.0, "All", "Dark")
jupiter = MagicsClass.SummonMagic("Jupiter", "Jupiter", 4.0, "All", "Light")
