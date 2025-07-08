

# this function calculates the effective attack of a character
def effective_attack(base_attack, crit, atk, damage_bonus):
    totalatk = base_attack * (1+atk) + 311
    return totalatk * (1 + crit) * (1+damage_bonus)

#change inputs in here
def main():
    weapon_atk = 640
    character_atk = 330
    atksubstat = 0.2  # Example substat bonus (20% increase)
    atkArtifact = 0.466 + 0.466  # Example artifact bonus (46.6% increase)
    atkWeapon = 0.8  # Example weapon bonus (80% increase)
    base_attack = weapon_atk + character_atk
    crit_dmg = 1.8
    crit_rate = 0.9
    crit = crit_dmg * crit_rate
    atk = atkArtifact + atkWeapon + atksubstat

    elemental_bonus = 0.75
    normal_damage_bonus = 0.75  # Example normal damage bonus (75% increase)
    damage_bonus = elemental_bonus + normal_damage_bonus
    name = "Skirk"  # Example character name
    print("Effective Attack for", name + ":", effective_attack(base_attack, crit, atk, damage_bonus))


if __name__ == "__main__":
    main()