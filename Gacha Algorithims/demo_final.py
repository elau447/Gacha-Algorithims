# Final demonstration of flexible name matching capabilities
print("=== Flexible Name Matching Examples ===")
print()

# Import the functions we need
from EffectiveAttack import find_best_match

# Sample data from our CSV files
characters = ["Name", "Diluc", "Xiao", "Ganyu", "Hu Tao", "Childe", "Zhongli", "Albedo"]
weapons = ["Name", "Wolf's Gravestone", "Primordial Jade Winged-Spear", "Amos' Bow", "Staff of Homa", "Polar Star", "Vortex Vanquisher", "Cinnabar Spindle"]

print("CHARACTER MATCHING EXAMPLES:")
print("-" * 40)
character_tests = ["diluc", "xiao", "ganyu", "hu", "hutao", "tao", "childe", "zhongli", "albedo", "geo", "dil"]

for test in character_tests:
    match, index = find_best_match(test, characters)
    if match:
        print(f"'{test}' → '{match}' ✓")
    else:
        print(f"'{test}' → No match found ✗")

print("\nWEAPON MATCHING EXAMPLES:")
print("-" * 40)
weapon_tests = ["wolf", "gravestone", "jade", "spear", "amos", "bow", "homa", "staff", "polar", "star", "vortex", "cinnabar", "spindle", "wgs"]

for test in weapon_tests:
    match, index = find_best_match(test, weapons)
    if match:
        print(f"'{test}' → '{match}' ✓")
    else:
        print(f"'{test}' → No match found ✗")

print("\nKEY FEATURES:")
print("-" * 40)
print("✓ Case-insensitive matching")
print("✓ Partial name matching (both directions)")
print("✓ Word-by-word matching")
print("✓ Fuzzy matching with scoring")
print("✓ User-friendly error messages")
print("✓ 'list' command to see all options")
print()
print("Examples of what works:")
print("- 'diluc' matches 'Diluc'")
print("- 'hu' matches 'Hu Tao'")
print("- 'wolf' matches 'Wolf's Gravestone'")
print("- 'jade' matches 'Primordial Jade Winged-Spear'")
print("- 'homa' matches 'Staff of Homa'")
print()
print("You can now run EffectiveAttack.py and use any of these partial names!")
