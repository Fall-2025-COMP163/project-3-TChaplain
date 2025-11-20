"""
COMP 163 - Project 3: Quest Chronicles
Character Manager Module - Starter Code

Name: [Your Name Here]

AI Usage: [Document any AI assistance used]

This module handles character creation, loading, and saving.
"""

import os
from custom_exceptions import (
    InvalidCharacterClassError,
    CharacterNotFoundError,
    SaveFileCorruptedError,
    InvalidSaveDataError,
    CharacterDeadError
)

# ============================================================================
# CHARACTER MANAGEMENT FUNCTIONS
# ============================================================================

def create_character(name, character_class):
    """
    Create a new character with stats based on class
    
    Valid classes: Warrior, Mage, Rogue, Cleric
    
    Returns: Dictionary with character data including:
            - name, class, level, health, max_health, strength, magic
            - experience, gold, inventory, active_quests, completed_quests
    
    Raises: InvalidCharacterClassError if class is not valid
    """
    # TODO: Implement character creation
    # Validate character_class first
    # Example base stats:
    # Warrior: health=120, strength=15, magic=5
    # Mage: health=80, strength=8, magic=20
    # Rogue: health=90, strength=12, magic=10
    # Cleric: health=100, strength=10, magic=15
    
    # All characters start with:
    # - level=1, experience=0, gold=100
    # - inventory=[], active_quests=[], completed_quests=[]
    
    # Raise InvalidCharacterClassError if class not in valid list
    

    valid = ("Warrior", "Mage", "Rogue", "Cleric")
    if character_class not in valid:
        raise InvalidCharacterClassError(f"Invalid class: {character_class}")

    # Base stats by class
    base_stats = {
        "Warrior": {"health": 120, "strength": 15, "magic": 5},
        "Mage": {"health": 80, "strength": 8, "magic": 20},
        "Rogue": {"health": 90, "strength": 12, "magic": 10},
        "Cleric": {"health": 100, "strength": 10, "magic": 15},
    }

    stats = base_stats[character_class]
    character = {
        "name": name,
        "class": character_class,
        "level": 1,
        "health": stats["health"],
        "max_health": stats["health"],
        "strength": stats["strength"],
        "magic": stats["magic"],
        "experience": 0,
        "gold": 100,
        "inventory": [],
        "active_quests": [],
        "completed_quests": []
    }

    return character

def save_character(character, save_directory="data/save_games"):
    """
    Save character to file
    
    Filename format: {character_name}_save.txt
    
    File format:
    NAME: character_name
    CLASS: class_name
    LEVEL: 1
    HEALTH: 120
    MAX_HEALTH: 120
    STRENGTH: 15
    MAGIC: 5
    EXPERIENCE: 0
    GOLD: 100
    INVENTORY: item1,item2,item3
    ACTIVE_QUESTS: quest1,quest2
    COMPLETED_QUESTS: quest1,quest2
    
    Returns: True if successful
    Raises: PermissionError, IOError (let them propagate or handle)
    """
    # TODO: Implement save functionality
    # Create save_directory if it doesn't exist
    # Handle any file I/O errors appropriately
    # Lists should be saved as comma-separated values
    

    if not os.path.exists(save_directory):
        try:
            os.makedirs(save_directory)
        except Exception as e:
            # Let permission errors or other I/O errors surface to caller
            raise

    filename = os.path.join(save_directory, f"{character['name']}_save.txt")

    # Prepare comma-separated strings for lists
    inv_str = ",".join(character.get("inventory", []))
    active_str = ",".join(character.get("active_quests", []))
    comp_str = ",".join(character.get("completed_quests", []))

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"NAME: {character['name']}\n")
            f.write(f"CLASS: {character['class']}\n")
            f.write(f"LEVEL: {int(character['level'])}\n")
            f.write(f"HEALTH: {int(character['health'])}\n")
            f.write(f"MAX_HEALTH: {int(character['max_health'])}\n")
            f.write(f"STRENGTH: {int(character['strength'])}\n")
            f.write(f"MAGIC: {int(character['magic'])}\n")
            f.write(f"EXPERIENCE: {int(character['experience'])}\n")
            f.write(f"GOLD: {int(character['gold'])}\n")
            f.write(f"INVENTORY: {inv_str}\n")
            f.write(f"ACTIVE_QUESTS: {active_str}\n")
            f.write(f"COMPLETED_QUESTS: {comp_str}\n")
    except Exception:
        # Let IO/Permission errors propagate as documented
        raise

    return True

def load_character(character_name, save_directory="data/save_games"):
    """
    Load character from save file
    
    Args:
        character_name: Name of character to load
        save_directory: Directory containing save files
    
    Returns: Character dictionary
    Raises: 
        CharacterNotFoundError if save file doesn't exist
        SaveFileCorruptedError if file exists but can't be read
        InvalidSaveDataError if data format is wrong
    """
    # TODO: Implement load functionality
    # Check if file exists → CharacterNotFoundError
    # Try to read file → SaveFileCorruptedError
    # Validate data format → InvalidSaveDataError
    # Parse comma-separated lists back into Python lists
    

    filename = os.path.join(save_directory, f"{character_name}_save.txt")

    if not os.path.exists(filename):
        raise CharacterNotFoundError(f"No save for: {character_name}")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
    except Exception:
        raise SaveFileCorruptedError(f"Could not read save file for: {character_name}")

    data = {}
    for line in lines:
        if ": " not in line:
        # For empty lists, allow lines like "INVENTORY:"
            if any(line.startswith(k) for k in ("INVENTORY", "ACTIVE_QUESTS", "COMPLETED_QUESTS")):
                key = line.strip(":")
                data[key.lower()] = []
                continue
            raise InvalidSaveDataError(f"Malformed line in save file: '{line}'")
        key, value = line.split(": ", 1)

        # Map keys to internal data types
        if key == "NAME":
            data["name"] = value
        elif key == "CLASS":
            data["class"] = value
        elif key == "LEVEL":
            try:
                data["level"] = int(value)
            except ValueError:
                raise InvalidSaveDataError("Invalid LEVEL value")
        elif key == "HEALTH":
            try:
                data["health"] = int(value)
            except ValueError:
                raise InvalidSaveDataError("Invalid HEALTH value")
        elif key == "MAX_HEALTH":
            try:
                data["max_health"] = int(value)
            except ValueError:
                raise InvalidSaveDataError("Invalid MAX_HEALTH value")
        elif key == "STRENGTH":
            try:
                data["strength"] = int(value)
            except ValueError:
                raise InvalidSaveDataError("Invalid STRENGTH value")
        elif key == "MAGIC":
            try:
                data["magic"] = int(value)
            except ValueError:
                raise InvalidSaveDataError("Invalid MAGIC value")
        elif key == "EXPERIENCE":
            try:
                data["experience"] = int(value)
            except ValueError:
                raise InvalidSaveDataError("Invalid EXPERIENCE value")
        elif key == "GOLD":
            try:
                data["gold"] = int(value)
            except ValueError:
                raise InvalidSaveDataError("Invalid GOLD value")
        elif key == "INVENTORY":
            # Empty -> empty list
            data["inventory"] = [x for x in value.split(",") if x] if value else []
        elif key == "ACTIVE_QUESTS":
            data["active_quests"] = [x for x in value.split(",") if x] if value else []
        elif key == "COMPLETED_QUESTS":
            data["completed_quests"] = [x for x in value.split(",") if x] if value else []
        else:
            # Unknown keys are treated as format errors to be strict for tests
            raise InvalidSaveDataError(f"Unknown save key: {key}")

    # Validate that required keys are present and types are correct
    try:
        validate_character_data(data)
    except InvalidSaveDataError:
        raise

    return data

def list_saved_characters(save_directory="data/save_games"):
    """
    Get list of all saved character names
    
    Returns: List of character names (without _save.txt extension)
    """
    # TODO: Implement this function
    # Return empty list if directory doesn't exist
    # Extract character names from filenames
    

    if not os.path.exists(save_directory):
        return []

    files = []
    try:
        for fname in os.listdir(save_directory):
            if fname.endswith("_save.txt"):
                # strip the suffix
                name = fname[:-9]  # remove "_save.txt" (9 chars)
                files.append(name)
    except Exception:
        # On unexpected errors, return empty list (safe fallback)
        return []

    return files

def delete_character(character_name, save_directory="data/save_games"):
    """
    Delete a character's save file
    
    Returns: True if deleted successfully
    Raises: CharacterNotFoundError if character doesn't exist
    """
    # TODO: Implement character deletion
    # Verify file exists before attempting deletion
    

    filename = os.path.join(save_directory, f"{character_name}_save.txt")
    if not os.path.exists(filename):
        raise CharacterNotFoundError(f"No save found for: {character_name}")

    try:
        os.remove(filename)
    except Exception:
        # Propagate unexpected OS errors
        raise

    return True

# ============================================================================
# CHARACTER OPERATIONS
# ============================================================================

def gain_experience(character, xp_amount):
    """
    Add experience to character and handle level ups
    
    Level up formula: level_up_xp = current_level * 100
    Example when leveling up:
    - Increase level by 1
    - Increase max_health by 10
    - Increase strength by 2
    - Increase magic by 2
    - Restore health to max_health
    
    Raises: CharacterDeadError if character health is 0
    """
    # TODO: Implement experience gain and leveling
    # Check if character is dead first
    # Add experience
    # Check for level up (can level up multiple times)
    # Update stats on level up
    

    if is_character_dead(character):
        raise CharacterDeadError("Cannot gain experience: character is dead")

    try:
        xp_amount = int(xp_amount)
    except Exception:
        raise ValueError("xp_amount must be an integer")

    character["experience"] = character.get("experience", 0) + xp_amount

    # Handle multiple level-ups if enough XP
    while character["experience"] >= character["level"] * 100:
        required = character["level"] * 100
        character["experience"] -= required
        character["level"] += 1
        # Stat increases on level up
        character["max_health"] = int(character.get("max_health", 0) + 10)
        character["strength"] = int(character.get("strength", 0) + 2)
        character["magic"] = int(character.get("magic", 0) + 2)
        # Restore health to the new max
        character["health"] = int(character["max_health"])

    return character


def add_gold(character, amount):
    """
    Add gold to character's inventory
    
    Args:
        character: Character dictionary
        amount: Amount of gold to add (can be negative for spending)
    
    Returns: New gold total
    Raises: ValueError if result would be negative
    """
    # TODO: Implement gold management
    # Check that result won't be negative
    # Update character's gold
    

    try:
        amount = int(amount)
    except Exception:
        raise ValueError("amount must be an integer")

    current = int(character.get("gold", 0))
    new_total = current + amount
    if new_total < 0:
        raise ValueError("Insufficient gold")

    character["gold"] = new_total
    return new_total

def heal_character(character, amount):
    """
    Heal character by specified amount
    
    Health cannot exceed max_health
    
    Returns: Actual amount healed
    """
    # TODO: Implement healing
    # Calculate actual healing (don't exceed max_health)
    # Update character health
    

    if is_character_dead(character):
        raise CharacterDeadError("Cannot heal: character is dead")

    try:
        amount = int(amount)
    except Exception:
        raise ValueError("amount must be an integer")

    max_h = int(character.get("max_health", 0))
    current = int(character.get("health", 0))
    if current >= max_h:
        return 0

    heal_amount = min(amount, max_h - current)
    character["health"] = current + heal_amount
    return heal_amount

def is_character_dead(character):
    """
    Check if character's health is 0 or below
    
    Returns: True if dead, False if alive
    """
    # TODO: Implement death check
    

    try:
        return int(character.get("health", 0)) <= 0
    except Exception:
        # If health isn't parseable, treat as dead for safety
        return True

def revive_character(character):
    """
    Revive a dead character with 50% health
    
    Returns: True if revived
    """
    # TODO: Implement revival
    # Restore health to half of max_health
    

    if not is_character_dead(character):
        return False

    max_h = int(character.get("max_health", 0))
    revived_hp = max(1, int(max_h * 0.5))
    character["health"] = revived_hp
    return True

# ============================================================================
# VALIDATION
# ============================================================================

def validate_character_data(character):
    """
    Validate that character dictionary has all required fields
    
    Required fields: name, class, level, health, max_health, 
                    strength, magic, experience, gold, inventory,
                    active_quests, completed_quests
    
    Returns: True if valid
    Raises: InvalidSaveDataError if missing fields or invalid types
    """
    # TODO: Implement validation
    # Check all required keys exist
    # Check that numeric values are numbers
    # Check that lists are actually lists
    

    required = [
        "name", "class", "level", "health", "max_health",
        "strength", "magic", "experience", "gold",
        "inventory", "active_quests", "completed_quests"
    ]

    for key in required:
        if key not in character:
            raise InvalidSaveDataError(f"Missing character field: {key}")

    # Numeric checks
    for num_key in ("level", "health", "max_health", "strength", "magic", "experience", "gold"):
        try:
            _ = int(character[num_key])
        except Exception:
            raise InvalidSaveDataError(f"Invalid numeric field: {num_key}")

    # List checks
    for list_key in ("inventory", "active_quests", "completed_quests"):
        if not isinstance(character[list_key], list):
            raise InvalidSaveDataError(f"Invalid list field: {list_key}")

    # Class validation
    if character["class"] not in ("Warrior", "Mage", "Rogue", "Cleric"):
        raise InvalidSaveDataError(f"Invalid character class: {character['class']}")

    return True

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== CHARACTER MANAGER TEST ===")

    try:
        char = create_character("TestHero", "Warrior")
        print("Created:", char)
        save_character(char)
        loaded = load_character("TestHero")
        print("Loaded:", loaded)
        print("Saved characters:", list_saved_characters())
        print("Delete:", delete_character("TestHero"))
    except Exception as e:
        print("Error during test:", e)
    
    # Test character creation
    # try:
    #     char = create_character("TestHero", "Warrior")
    #     print(f"Created: {char['name']} the {char['class']}")
    #     print(f"Stats: HP={char['health']}, STR={char['strength']}, MAG={char['magic']}")
    # except InvalidCharacterClassError as e:
    #     print(f"Invalid class: {e}")
    
    # Test saving
    # try:
    #     save_character(char)
    #     print("Character saved successfully")
    # except Exception as e:
    #     print(f"Save error: {e}")
    
    # Test loading
    # try:
    #     loaded = load_character("TestHero")
    #     print(f"Loaded: {loaded['name']}")
    # except CharacterNotFoundError:
    #     print("Character not found")
    # except SaveFileCorruptedError:
    #     print("Save file corrupted")

