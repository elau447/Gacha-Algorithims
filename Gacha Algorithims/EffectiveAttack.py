from sys import stdin
import csv


def find_best_match(input_name, available_names):
    """
    Finds the best matching name from available names using flexible matching.
    Returns the best match and its index, or (None, None) if no good match found.
    """
    input_name = input_name.strip().lower()
    
    # First try exact match
    for i, name in enumerate(available_names):
        if name.strip().lower() == input_name:
            return name, i
    
    # Then try partial match (input is contained in name)
    for i, name in enumerate(available_names):
        if input_name in name.strip().lower():
            return name, i
    
    # Then try reverse partial match (name is contained in input)
    for i, name in enumerate(available_names):
        if name.strip().lower() in input_name:
            return name, i
    
    # Finally try word-by-word matching
    input_words = input_name.split()
    best_match = None
    best_score = 0
    best_index = None
    
    for i, name in enumerate(available_names):
        name_words = name.strip().lower().split()
        score = 0
        
        # Count how many words match
        for input_word in input_words:
            for name_word in name_words:
                if input_word in name_word or name_word in input_word:
                    score += 1
                    break
        
        # Normalize score by length
        normalized_score = score / max(len(input_words), len(name_words))
        
        if normalized_score > best_score and normalized_score > 0.3:  # At least 30% match
            best_score = normalized_score
            best_match = name
            best_index = i
    
    return best_match, best_index


def read_character_data_from_csv(csv_file_path, character_name):
    """
    Reads character data from a CSV file where the first row contains character names.
    Returns a dictionary with the character's stats if found, None otherwise.
    Uses flexible name matching for better user experience.
    """
    try:
        with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            
            # Read the header row (character names)
            header = next(reader)
            
            # Find the best matching column for the character
            matched_name, character_column = find_best_match(character_name, header)
            
            if character_column is None:
                print(f"No good match found for '{character_name}' in CSV file.")
                print(f"Available options: {', '.join(header[1:])}")  # Skip 'Name' column
                return None
            else:
                if matched_name.strip().lower() != character_name.strip().lower():
                    print(f"Found closest match: '{matched_name}' for input '{character_name}'")
            
            character_column = character_column
            
            # Read the data rows and create a dictionary
            character_data = {}
            for row in reader:
                if len(row) > character_column and len(row) > 0:
                    stat_name = row[0].strip()
                    try:
                        # Handle string values for stat types
                        if stat_name in ['ascension_stat_type', 'weapon_substat_type', 'passive_type']:
                            character_data[stat_name] = row[character_column].strip()
                        else:
                            stat_value = float(row[character_column])
                            character_data[stat_name] = stat_value
                    except (ValueError, IndexError):
                        print(f"Warning: Could not parse value for {stat_name}")
                        continue
            
            return character_data
            
    except FileNotFoundError:
        print(f"CSV file '{csv_file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return None


def combine_character_and_weapon_stats(character_data, weapon_data):
    """
    Combines character and weapon stats into a single dictionary with total values.
    """
    if not character_data or not weapon_data:
        return None
    
    combined_stats = {}
    
    # Base attack = character base attack + weapon base attack
    combined_stats['base_attack'] = character_data.get('character_base_atk', 0) + weapon_data.get('weapon_base_atk', 0)
    
    # Combine percentage bonuses
    combined_stats['atk_percent'] = (
        character_data.get('atk_percent', 0) + 
        weapon_data.get('atk_percent_bonus', 0) +
        weapon_data.get('passive_atk_bonus', 0)
    )
    
    # Handle ascension stat bonus
    ascension_type = character_data.get('ascension_stat_type', '')
    ascension_value = character_data.get('ascension_stat_value', 0)
    if ascension_type == 'atk_percent':
        combined_stats['atk_percent'] += ascension_value
    
    # Handle weapon substat bonus
    weapon_substat_type = weapon_data.get('weapon_substat_type', '')
    weapon_substat_value = weapon_data.get('weapon_substat_value', 0)
    if weapon_substat_type == 'atk_percent':
        combined_stats['atk_percent'] += weapon_substat_value
    
    # Crit rate = base + character + weapon + ascension + weapon substat
    combined_stats['crit_rate'] = (
        character_data.get('crit_rate_bonus', 0.05) +  # Base 5%
        weapon_data.get('crit_rate_bonus', 0) +
        (ascension_value if ascension_type == 'crit_rate' else 0) +
        (weapon_substat_value if weapon_substat_type == 'crit_rate' else 0)
    )
    
    # Crit damage = base + character + weapon + ascension + weapon substat
    combined_stats['crit_dmg'] = (
        character_data.get('crit_dmg_bonus', 0.5) +  # Base 50%
        weapon_data.get('crit_dmg_bonus', 0) +
        (ascension_value if ascension_type == 'crit_dmg' else 0) +
        (weapon_substat_value if weapon_substat_type == 'crit_dmg' else 0)
    )
    
    # Elemental Mastery
    combined_stats['em'] = character_data.get('em', 0) + weapon_data.get('em', 0)
    
    # Damage bonuses
    combined_stats['elemental_dmg'] = (
        (ascension_value if 'dmg' in ascension_type else 0) +
        weapon_data.get('passive_dmg_bonus', 0)
    )
    
    # Other stats
    combined_stats['def_percent'] = (
        character_data.get('def_percent', 0) + 
        weapon_data.get('def_percent_bonus', 0) +
        (ascension_value if ascension_type == 'def_percent' else 0) +
        (weapon_substat_value if weapon_substat_type == 'def_percent' else 0)
    )
    
    combined_stats['hp_percent'] = (
        character_data.get('hp_percent', 0) + 
        weapon_data.get('hp_percent_bonus', 0) +
        (ascension_value if ascension_type == 'hp_percent' else 0) +
        (weapon_substat_value if weapon_substat_type == 'hp_percent' else 0)
    )
    
    combined_stats['energy_recharge'] = (
        character_data.get('energy_recharge', 1.0) + 
        weapon_data.get('energy_recharge_bonus', 0) +
        (ascension_value if ascension_type == 'energy_recharge' else 0) +
        (weapon_substat_value if weapon_substat_type == 'energy_recharge' else 0)
    )
    
    return combined_stats


# this function calculates the effective attack of a character
def effective_attack(base_attack, crit, atk, damage_bonus):
    totalatk = base_attack * (1 + atk) + 311
    return round(totalatk * (1 + crit) * (1 + damage_bonus))


# change inputs in here
def main():
    print("=== Genshin Impact Effective Attack Calculator ===")
    print("Note: You can use partial names (e.g., 'diluc', 'wolf', 'jade', 'homa')")
    print()
    
    # Get character and weapon names from user input
    print("Enter character name (or 'list' to see options): ", end="")
    character_input = input().strip()
    
    if character_input.lower() == 'list':
        show_available_options('character_stats.csv', "characters")
        print("Enter character name: ", end="")
        character_input = input().strip()
    
    print("Enter weapon name (or 'list' to see options): ", end="")
    weapon_input = input().strip()
    
    if weapon_input.lower() == 'list':
        show_available_options('weapon_stats.csv', "weapons")
        print("Enter weapon name: ", end="")
        weapon_input = input().strip()
    
    # Paths to your CSV files
    character_csv_path = 'character_stats.csv'
    weapon_csv_path = 'weapon_stats.csv'
    
    # Read character and weapon data from CSV files
    character_data = read_character_data_from_csv(character_csv_path, character_input)
    weapon_data = read_character_data_from_csv(weapon_csv_path, weapon_input)
    
    if character_data is None or weapon_data is None:
        print("Character or weapon data not found. Using default values...")
        # Fallback to default values
        base_attack = 970  # Default total base attack
        crit_rate = 0.5
        crit_dmg = 1.5
        atk_percent = 0.5
        elemental_dmg = 0.466
        normal_damage_bonus = 0.0
    else:
        # Combine character and weapon stats
        combined_stats = combine_character_and_weapon_stats(character_data, weapon_data)
        
        if combined_stats is None:
            print("Error combining stats. Using default values...")
            base_attack = 970
            crit_rate = 0.5
            crit_dmg = 1.5
            atk_percent = 0.5
            elemental_dmg = 0.466
            normal_damage_bonus = 0.0
        else:
            base_attack = combined_stats['base_attack']
            crit_rate = combined_stats['crit_rate']
            crit_dmg = combined_stats['crit_dmg']
            atk_percent = combined_stats['atk_percent']
            elemental_dmg = combined_stats['elemental_dmg']
            normal_damage_bonus = 0.0  # This would come from artifacts/talents
            
            # Print the combined stats for debugging
            print(f"\nCombined Stats for {character_input} with {weapon_input}:")
            print(f"Base Attack: {base_attack}")
            print(f"ATK%: {atk_percent:.1%}")
            print(f"Crit Rate: {crit_rate:.1%}")
            print(f"Crit DMG: {crit_dmg:.1%}")
            print(f"Elemental DMG: {elemental_dmg:.1%}")
            print(f"EM: {combined_stats['em']}")
            print(f"DEF%: {combined_stats['def_percent']:.1%}")
            print(f"HP%: {combined_stats['hp_percent']:.1%}")
            print(f"Energy Recharge: {combined_stats['energy_recharge']:.1%}")
    
    # Calculate effective attack using the combined stats
    crit = crit_dmg * crit_rate
    damage_bonus = elemental_dmg + normal_damage_bonus
    
    print(f"\nEffective Attack for {character_input} with {weapon_input}: {effective_attack(base_attack, crit, atk_percent, damage_bonus)}")


def show_available_options(csv_file_path, option_type="items"):
    """
    Shows available options from a CSV file.
    """
    try:
        with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            available = [name.strip() for name in header[1:] if name.strip()]  # Skip 'Name' column
            print(f"Available {option_type}: {', '.join(available)}")
    except Exception:
        print(f"Could not read {option_type} from {csv_file_path}")


if __name__ == "__main__":
    main()