"""
COMP 163 - Project 3: Quest Chronicles
Game Data Module - Starter Code

Name: [Your Name Here]

AI Usage: [Document any AI assistance used]

This module handles loading and validating game data from text files.
"""

import os
from custom_exceptions import (
    InvalidDataFormatError,
    MissingDataFileError,
    CorruptedDataError
)

# ============================================================================
# DATA LOADING FUNCTIONS
# ============================================================================

def load_quests(filename="data/quests.txt"):
    """
    Load quest data from file
    
    Expected format per quest (separated by blank lines):
    QUEST_ID: unique_quest_name
    TITLE: Quest Display Title
    DESCRIPTION: Quest description text
    REWARD_XP: 100
    REWARD_GOLD: 50
    REQUIRED_LEVEL: 1
    PREREQUISITE: previous_quest_id (or NONE)
    
    Returns: Dictionary of quests {quest_id: quest_data_dict}
    Raises: MissingDataFileError, InvalidDataFormatError, CorruptedDataError
    """
    # TODO: Implement this function
    # Must handle:
    # - FileNotFoundError → raise MissingDataFileError
    # - Invalid format → raise InvalidDataFormatError
    # - Corrupted/unreadable data → raise CorruptedDataError
    

    if not os.path.exists(filename):
        raise MissingDataFileError(f"Missing quest file: {filename}")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read().strip()
    except Exception:
        raise CorruptedDataError("Could not read quests file")

    if not content:
        raise InvalidDataFormatError("Quest file is empty")

    quests = {}
    blocks = content.split("\n\n")  # Split quests by blank lines

    for block in blocks:
        lines = [line.strip() for line in block.split("\n") if line.strip()]
        quest = parse_quest_block(lines)
        validate_quest_data(quest)
        quests[quest["quest_id"]] = quest

    return quests

def load_items(filename="data/items.txt"):
    """
    Load item data from file
    
    Expected format per item (separated by blank lines):
    ITEM_ID: unique_item_name
    NAME: Item Display Name
    TYPE: weapon|armor|consumable
    EFFECT: stat_name:value (e.g., strength:5 or health:20)
    COST: 100
    DESCRIPTION: Item description
    
    Returns: Dictionary of items {item_id: item_data_dict}
    Raises: MissingDataFileError, InvalidDataFormatError, CorruptedDataError
    """
    # TODO: Implement this function
    # Must handle same exceptions as load_quests
    

    if not os.path.exists(filename):
        raise MissingDataFileError(f"Missing item file: {filename}")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read().strip()
    except Exception:
        raise CorruptedDataError("Could not read items file")

    if not content:
        raise InvalidDataFormatError("Item file is empty")

    items = {}
    blocks = content.split("\n\n")  # Split items by blank lines

    for block in blocks:
        lines = [line.strip() for line in block.split("\n") if line.strip()]
        item = parse_item_block(lines)
        validate_item_data(item)
        items[item["item_id"]] = item

    return items

def validate_quest_data(quest_dict):
    """
    Validate that quest dictionary has all required fields
    
    Required fields: quest_id, title, description, reward_xp, 
                    reward_gold, required_level, prerequisite
    
    Returns: True if valid
    Raises: InvalidDataFormatError if missing required fields
    """
    # TODO: Implement validation
    # Check that all required keys exist
    # Check that numeric values are actually numbers
    

    required = [
        "quest_id",
        "title",
        "description",
        "reward_xp",
        "reward_gold",
        "required_level",
        "prerequisite"
    ]

    for field in required:
        if field not in quest_dict:
            raise InvalidDataFormatError(f"Missing quest field: {field}")

    # Check number fields
    for num_field in ["reward_xp", "reward_gold", "required_level"]:
        if not isinstance(quest_dict[num_field], int):
            raise InvalidDataFormatError(f"Invalid number for {num_field}")

    return True

def validate_item_data(item_dict):
    """
    Validate that item dictionary has all required fields
    
    Required fields: item_id, name, type, effect, cost, description
    Valid types: weapon, armor, consumable
    
    Returns: True if valid
    Raises: InvalidDataFormatError if missing required fields or invalid type
    """
    # TODO: Implement validation
    

    required = [
        "item_id",
        "name",
        "type",
        "effect",
        "cost",
        "description"
    ]

    for field in required:
        if field not in item_dict:
            raise InvalidDataFormatError(f"Missing item field: {field}")

    # Valid types
    if item_dict["type"] not in ("weapon", "armor", "consumable"):
        raise InvalidDataFormatError("Invalid item type")

    # Cost must be integer
    if not isinstance(item_dict["cost"], int):
        raise InvalidDataFormatError("Invalid item cost")

    return True

def create_default_data_files():
    """
    Create default data files if they don't exist
    This helps with initial setup and testing
    """
    # TODO: Implement this function
    # Create data/ directory if it doesn't exist
    # Create default quests.txt and items.txt files
    # Handle any file permission errors appropriately
    

    if not os.path.exists("data"):
        os.makedirs("data")

    # Default quests
    if not os.path.exists("data/quests.txt"):
        try:
            with open("data/quests.txt", "w", encoding="utf-8") as f:
                f.write(
                    "QUEST_ID: intro\n"
                    "TITLE: Welcome Adventurer\n"
                    "DESCRIPTION: Your journey begins.\n"
                    "REWARD_XP: 50\n"
                    "REWARD_GOLD: 20\n"
                    "REQUIRED_LEVEL: 1\n"
                    "PREREQUISITE: NONE\n\n"
                )
        except Exception:
            raise CorruptedDataError("Could not create quests file")
    
    if not os.path.exists("data/items.txt"):
        try:
            with open("data/items.txt", "w", encoding="utf-8") as f:
                f.write(
                    "ITEM_ID: basic_sword\n"
                    "NAME: Basic Sword\n"
                    "TYPE: weapon\n"
                    "EFFECT: strength:5\n"
                    "COST: 25\n"
                    "DESCRIPTION: A simple starter weapon.\n\n"
                )
        except Exception:
            raise CorruptedDataError("Could not create items file")


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def parse_quest_block(lines):
    """
    Parse a block of lines into a quest dictionary
    
    Args:
        lines: List of strings representing one quest
    
    Returns: Dictionary with quest data
    Raises: InvalidDataFormatError if parsing fails
    """
    # TODO: Implement parsing logic
    # Split each line on ": " to get key-value pairs
    # Convert numeric strings to integers
    # Handle parsing errors gracefully
    

    quest = {}

    try:
        for line in lines:
            if ": " not in line:
                raise InvalidDataFormatError("Quest line missing ':' separator")

            key, value = line.split(": ", 1)
            key = key.strip()
            value = value.strip()

            if key == "QUEST_ID":
                quest["quest_id"] = value
            elif key == "TITLE":
                quest["title"] = value
            elif key == "DESCRIPTION":
                quest["description"] = value
            elif key == "REWARD_XP":
                quest["reward_xp"] = int(value)
            elif key == "REWARD_GOLD":
                quest["reward_gold"] = int(value)
            elif key == "REQUIRED_LEVEL":
                quest["required_level"] = int(value)
            elif key == "PREREQUISITE":
                quest["prerequisite"] = value
            else:
                raise InvalidDataFormatError(f"Unknown quest field: {key}")

    except ValueError:
        raise InvalidDataFormatError("Invalid number in quest block")

    return quest

def parse_item_block(lines):
    """
    Parse a block of lines into an item dictionary
    
    Args:
        lines: List of strings representing one item
    
    Returns: Dictionary with item data
    Raises: InvalidDataFormatError if parsing fails
    """
    # TODO: Implement parsing logic
    

    item = {}

    try:
        for line in lines:
            if ": " not in line:
                raise InvalidDataFormatError("Item line missing ':' separator")

            key, value = line.split(": ", 1)
            key = key.strip()
            value = value.strip()

            if key == "ITEM_ID":
                item["item_id"] = value
            elif key == "NAME":
                item["name"] = value
            elif key == "TYPE":
                item["type"] = value
            elif key == "EFFECT":
                # Format: stat:value
                if ":" not in value:
                    raise InvalidDataFormatError("Invalid item effect format")
                stat, amount = value.split(":", 1)
                item["effect"] = {stat: int(amount)}
            elif key == "COST":
                item["cost"] = int(value)
            elif key == "DESCRIPTION":
                item["description"] = value
            else:
                raise InvalidDataFormatError(f"Unknown item field: {key}")

    except ValueError:
        raise InvalidDataFormatError("Invalid number in item block")

    return item

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== GAME DATA MODULE TEST ===")

    create_default_data_files()

    try:
        print(load_quests())
    except Exception as e:
        print("Quest Load Error:", e)

    try:
        print(load_items())
    except Exception as e:
        print("Item Load Error:", e)
    

    # Test creating default files
    # create_default_data_files()
    
    # Test loading quests
    # try:
    #     quests = load_quests()
    #     print(f"Loaded {len(quests)} quests")
    # except MissingDataFileError:
    #     print("Quest file not found")
    # except InvalidDataFormatError as e:
    #     print(f"Invalid quest format: {e}")
    
    # Test loading items
    # try:
    #     items = load_items()
    #     print(f"Loaded {len(items)} items")
    # except MissingDataFileError:
    #     print("Item file not found")
    # except InvalidDataFormatError as e:
    #     print(f"Invalid item format: {e}")

