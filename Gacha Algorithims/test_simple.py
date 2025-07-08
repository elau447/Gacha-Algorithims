# Simple test of the flexible matching function
from EffectiveAttack import find_best_match, read_character_data_from_csv

# Test the find_best_match function directly
print("Testing flexible name matching function:")
print("=" * 50)

# Test character names
character_names = ["Name", "Diluc", "Xiao", "Ganyu", "Hu Tao", "Childe", "Zhongli", "Albedo"]
weapon_names = ["Name", "Wolf's Gravestone", "Primordial Jade Winged-Spear", "Amos' Bow", "Staff of Homa", "Polar Star", "Vortex Vanquisher", "Cinnabar Spindle"]

test_inputs = [
    ("diluc", character_names),
    ("xiao", character_names),
    ("hu", character_names),
    ("hutao", character_names),
    ("tao", character_names),
    ("wolf", weapon_names),
    ("gravestone", weapon_names),
    ("jade", weapon_names),
    ("amos", weapon_names),
    ("homa", weapon_names),
    ("staff", weapon_names),
    ("polar", weapon_names),
]

for test_input, names_list in test_inputs:
    match, index = find_best_match(test_input, names_list)
    if match:
        print(f"✓ '{test_input}' -> '{match}' (index {index})")
    else:
        print(f"✗ '{test_input}' -> No match found")

print("\nTesting CSV reading with flexible matching:")
print("=" * 50)

# Test CSV reading
character_data = read_character_data_from_csv('character_stats.csv', 'diluc')
if character_data:
    print("✓ Successfully read Diluc data (partial match)")
else:
    print("✗ Failed to read Diluc data")

weapon_data = read_character_data_from_csv('weapon_stats.csv', 'wolf')
if weapon_data:
    print("✓ Successfully read Wolf's Gravestone data (partial match)")
else:
    print("✗ Failed to read Wolf's Gravestone data")
