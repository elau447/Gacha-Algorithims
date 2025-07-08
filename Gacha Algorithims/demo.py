# Interactive demo of flexible matching
import sys
import os

# Add current directory to path so we can import our module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from EffectiveAttack import read_character_data_from_csv, combine_character_and_weapon_stats, effective_attack

def demo_flexible_matching():
    print("=== Flexible Name Matching Demo ===")
    print("You can now use partial names! Examples:")
    print("Characters: 'diluc', 'hu', 'xiao', 'ganyu', etc.")
    print("Weapons: 'wolf', 'jade', 'amos', 'homa', 'staff', etc.")
    print()
    
    # Test with some examples
    test_cases = [
        ("diluc", "wolf"),
        ("hu", "homa"),
        ("xiao", "jade"),
        ("ganyu", "amos")
    ]
    
    for char_input, weapon_input in test_cases:
        print(f"Testing: '{char_input}' + '{weapon_input}'")
        
        # Read data
        character_data = read_character_data_from_csv('character_stats.csv', char_input)
        weapon_data = read_character_data_from_csv('weapon_stats.csv', weapon_input)
        
        if character_data and weapon_data:
            # Combine stats
            combined_stats = combine_character_and_weapon_stats(character_data, weapon_data)
            
            if combined_stats:
                base_attack = combined_stats['base_attack']
                crit_rate = combined_stats['crit_rate']
                crit_dmg = combined_stats['crit_dmg']
                atk_percent = combined_stats['atk_percent']
                elemental_dmg = combined_stats['elemental_dmg']
                
                crit = crit_dmg * crit_rate
                damage_bonus = elemental_dmg
                
                result = effective_attack(base_attack, crit, atk_percent, damage_bonus)
                print(f"  Result: {result} effective attack")
            else:
                print("  Error combining stats")
        else:
            print("  Failed to read data")
        print()

if __name__ == "__main__":
    demo_flexible_matching()
