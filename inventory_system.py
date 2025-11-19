"""
COMP 163 - Project 3: Quest Chronicles
Inventory System Module - Starter Code

Name: [Your Name Here]

AI Usage: [Document any AI assistance used]

This module handles inventory management, item usage, and equipment.
"""

from custom_exceptions import (
    InventoryFullError,
    ItemNotFoundError,
    InsufficientResourcesError,
    InvalidItemTypeError
)

# Maximum inventory size
MAX_INVENTORY_SIZE = 20

# ============================================================================
# INVENTORY MANAGEMENT
# ============================================================================

def add_item_to_inventory(character, item_id):
    """
    Add an item to character's inventory
    
    Args:
        character: Character dictionary
        item_id: Unique item identifier
    
    Returns: True if added successfully
    Raises: InventoryFullError if inventory is at max capacity
    """
    # TODO: Implement adding items
    # Check if inventory is full (>= MAX_INVENTORY_SIZE)
    # Add item_id to character['inventory'] list
    pass

    inventory = character.get("inventory", [])

    if len(inventory) >= MAX_INVENTORY_SIZE:
        raise InventoryFullError("Inventory is full.")

    inventory.append(item_id)
    return True

def remove_item_from_inventory(character, item_id):
    """
    Remove an item from character's inventory
    
    Args:
        character: Character dictionary
        item_id: Item to remove
    
    Returns: True if removed successfully
    Raises: ItemNotFoundError if item not in inventory
    """
    # TODO: Implement item removal
    # Check if item exists in inventory
    # Remove item from list
    pass

    inventory = character.get("inventory", [])

    if item_id not in inventory:
        raise ItemNotFoundError(f"Item '{item_id}' not in inventory.")

    inventory.remove(item_id)
    return True

def has_item(character, item_id):
    """
    Check if character has a specific item
    
    Returns: True if item in inventory, False otherwise
    """
    # TODO: Implement item check
    pass

    return item_id in character.get("inventory", [])

def count_item(character, item_id):
    """
    Count how many of a specific item the character has
    
    Returns: Integer count of item
    """
    # TODO: Implement item counting
    # Use list.count() method
    pass

    return character.get("inventory", []).count(item_id)

def get_inventory_space_remaining(character):
    """
    Calculate how many more items can fit in inventory
    
    Returns: Integer representing available slots
    """
    # TODO: Implement space calculation
    pass

    return MAX_INVENTORY_SIZE - len(character.get("inventory", []))

def clear_inventory(character):
    """
    Remove all items from inventory
    
    Returns: List of removed items
    """
    # TODO: Implement inventory clearing
    # Save current inventory before clearing
    # Clear character's inventory list
    pass

    removed_items = character.get("inventory", []).copy()
    character["inventory"] = []
    return removed_items

# ============================================================================
# ITEM USAGE
# ============================================================================

def use_item(character, item_id, item_data):
    """
    Use a consumable item from inventory
    
    Args:
        character: Character dictionary
        item_id: Item to use
        item_data: Item information dictionary from game_data
    
    Item types and effects:
    - consumable: Apply effect and remove from inventory
    - weapon/armor: Cannot be "used", only equipped
    
    Returns: String describing what happened
    Raises: 
        ItemNotFoundError if item not in inventory
        InvalidItemTypeError if item type is not 'consumable'
    """
    # TODO: Implement item usage
    # Check if character has the item
    # Check if item type is 'consumable'
    # Parse effect (format: "stat_name:value" e.g., "health:20")
    # Apply effect to character
    # Remove item from inventory
    pass

    if not has_item(character, item_id):
        raise ItemNotFoundError(f"{item_id} not found in inventory.")

    if item_data["type"] != "consumable":
        raise InvalidItemTypeError(f"{item_id} is not a consumable.")

    # Parse effect (e.g., "health:20")
    stat, value = parse_item_effect(item_data["effect"])

    # Apply change
    apply_stat_effect(character, stat, value)

    # Remove from inventory
    remove_item_from_inventory(character, item_id)

    return f"Used {item_data['name']} and gained {value} {stat}."

def equip_weapon(character, item_id, item_data):
    """
    Equip a weapon
    
    Args:
        character: Character dictionary
        item_id: Weapon to equip
        item_data: Item information dictionary
    
    Weapon effect format: "strength:5" (adds 5 to strength)
    
    If character already has weapon equipped:
    - Unequip current weapon (remove bonus)
    - Add old weapon back to inventory
    
    Returns: String describing equipment change
    Raises:
        ItemNotFoundError if item not in inventory
        InvalidItemTypeError if item type is not 'weapon'
    """
    # TODO: Implement weapon equipping
    # Check item exists and is type 'weapon'
    # Handle unequipping current weapon if exists
    # Parse effect and apply to character stats
    # Store equipped_weapon in character dictionary
    # Remove item from inventory
    pass

    if not has_item(character, item_id):
        raise ItemNotFoundError(f"{item_id} not found.")

    if item_data["type"] != "weapon":
        raise InvalidItemTypeError(f"{item_id} is not a weapon.")

    # Unequip old weapon
    if character.get("equipped_weapon"):
        old_weapon_id = character["equipped_weapon"]
        old_weapon_data = character["item_data"][old_weapon_id]

        # Remove old weapon bonus
        stat, value = parse_item_effect(old_weapon_data["effect"])
        apply_stat_effect(character, stat, -value)

        # Add old weapon back
        add_item_to_inventory(character, old_weapon_id)

    # Equip new weapon
    stat, value = parse_item_effect(item_data["effect"])
    apply_stat_effect(character, stat, value)

    character["equipped_weapon"] = item_id
    remove_item_from_inventory(character, item_id)

    return f"Equipped weapon: {item_data['name']}"

def equip_armor(character, item_id, item_data):
    """
    Equip armor
    
    Args:
        character: Character dictionary
        item_id: Armor to equip
        item_data: Item information dictionary
    
    Armor effect format: "max_health:10" (adds 10 to max_health)
    
    If character already has armor equipped:
    - Unequip current armor (remove bonus)
    - Add old armor back to inventory
    
    Returns: String describing equipment change
    Raises:
        ItemNotFoundError if item not in inventory
        InvalidItemTypeError if item type is not 'armor'
    """
    # TODO: Implement armor equipping
    # Similar to equip_weapon but for armor
    pass

    if not has_item(character, item_id):
        raise ItemNotFoundError(f"{item_id} not found.")

    if item_data["type"] != "armor":
        raise InvalidItemTypeError(f"{item_id} is not armor.")

    # Unequip current armor
    if character.get("equipped_armor"):
        old_armor_id = character["equipped_armor"]
        old_armor_data = character["item_data"][old_armor_id]

        stat, value = parse_item_effect(old_armor_data["effect"])
        apply_stat_effect(character, stat, -value)

        add_item_to_inventory(character, old_armor_id)

        # Equip new armor
    stat, value = parse_item_effect(item_data["effect"])
    apply_stat_effect(character, stat, value)

    character["equipped_armor"] = item_id
    remove_item_from_inventory(character, item_id)

    return f"Equipped armor: {item_data['name']}"

def unequip_weapon(character):
    """
    Remove equipped weapon and return it to inventory
    
    Returns: Item ID that was unequipped, or None if no weapon equipped
    Raises: InventoryFullError if inventory is full
    """
    # TODO: Implement weapon unequipping
    # Check if weapon is equipped
    # Remove stat bonuses
    # Add weapon back to inventory
    # Clear equipped_weapon from character
    pass

    if not character.get("equipped_weapon"):
        return None

    weapon_id = character["equipped_weapon"]
    weapon_data = character["item_data"][weapon_id]

    stat, value = parse_item_effect(weapon_data["effect"])
    apply_stat_effect(character, stat, -value)

    if get_inventory_space_remaining(character) == 0:
        raise InventoryFullError("No space to unequip weapon.")

    add_item_to_inventory(character, weapon_id)
    character["equipped_weapon"] = None

    return weapon_id

def unequip_armor(character):
    """
    Remove equipped armor and return it to inventory
    
    Returns: Item ID that was unequipped, or None if no armor equipped
    Raises: InventoryFullError if inventory is full
    """
    # TODO: Implement armor unequipping
    pass

    if not character.get("equipped_armor"):
        return None

    armor_id = character["equipped_armor"]
    armor_data = character["item_data"][armor_id]

    stat, value = parse_item_effect(armor_data["effect"])
    apply_stat_effect(character, stat, -value)

    if get_inventory_space_remaining(character) == 0:
        raise InventoryFullError("No space to unequip armor.")

    add_item_to_inventory(character, armor_id)
    character["equipped_armor"] = None

    return armor_id

# ============================================================================
# SHOP SYSTEM
# ============================================================================

def purchase_item(character, item_id, item_data):
    """
    Purchase an item from a shop
    
    Args:
        character: Character dictionary
        item_id: Item to purchase
        item_data: Item information with 'cost' field
    
    Returns: True if purchased successfully
    Raises:
        InsufficientResourcesError if not enough gold
        InventoryFullError if inventory is full
    """
    # TODO: Implement purchasing
    # Check if character has enough gold
    # Check if inventory has space
    # Subtract gold from character
    # Add item to inventory
    pass

    cost = item_data["cost"]

    if character["gold"] < cost:
        raise InsufficientResourcesError("Not enough gold.")

    if get_inventory_space_remaining(character) == 0:
        raise InventoryFullError("Inventory full.")

    character["gold"] -= cost
    add_item_to_inventory(character, item_id)

    return True

def sell_item(character, item_id, item_data):
    """
    Sell an item for half its purchase cost
    
    Args:
        character: Character dictionary
        item_id: Item to sell
        item_data: Item information with 'cost' field
    
    Returns: Amount of gold received
    Raises: ItemNotFoundError if item not in inventory
    """
    # TODO: Implement selling
    # Check if character has item
    # Calculate sell price (cost // 2)
    # Remove item from inventory
    # Add gold to character
    pass

    """Sell item for half value."""
    if not has_item(character, item_id):
        raise ItemNotFoundError(f"{item_id} not found.")

    price = item_data["cost"] // 2

    remove_item_from_inventory(character, item_id)
    character["gold"] += price

    return price


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def parse_item_effect(effect_string):
    """
    Parse item effect string into stat name and value
    
    Args:
        effect_string: String in format "stat_name:value"
    
    Returns: Tuple of (stat_name, value)
    Example: "health:20" → ("health", 20)
    """
    # TODO: Implement effect parsing
    # Split on ":"
    # Convert value to integer
    pass

    """Convert 'stat:value' → ('stat', int(value))"""
    try:
        stat, value = effect_string.split(":")
        return stat, int(value)
    except:
        raise InvalidItemTypeError("Invalid effect format.")

def apply_stat_effect(character, stat_name, value):
    """
    Apply a stat modification to character
    
    Valid stats: health, max_health, strength, magic
    
    Note: health cannot exceed max_health
    """
    # TODO: Implement stat application
    # Add value to character[stat_name]
    # If stat is health, ensure it doesn't exceed max_health
    pass

    """Apply stat modification with safety checks."""
    if stat_name not in character:
        character[stat_name] = 0

    character[stat_name] += value

    # Cap health at max_health
    if stat_name == "health":
        character["health"] = min(character["health"], character.get("max_health", 9999))

def display_inventory(character, item_data_dict):
    """
    Display character's inventory in formatted way
    
    Args:
        character: Character dictionary
        item_data_dict: Dictionary of all item data
    
    Shows item names, types, and quantities
    """
    # TODO: Implement inventory display
    # Count items (some may appear multiple times)
    # Display with item names from item_data_dict
    pass

    """Print formatted item list."""
    inventory = character.get("inventory", [])
    
    print("\n=== INVENTORY ===")
    if not inventory:
        print("Inventory is empty.")
        return
    
    counted = {}
    for item in inventory:
        counted[item] = counted.get(item, 0) + 1

    for item_id, qty in counted.items():
        item_name = item_data_dict[item_id]["name"]
        item_type = item_data_dict[item_id]["type"]
        print(f"{item_name} ({item_type}) x{qty}")

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== INVENTORY SYSTEM TEST ===")
    
    item_data = {
        "health_potion": {
            "item_id": "health_potion",
            "name": "Health Potion",
            "type": "consumable",
            "effect": "health:25",
            "cost": 30
        },
        "iron_sword": {
            "item_id": "iron_sword",
            "name": "Iron Sword",
            "type": "weapon",
            "effect": "strength:5",
            "cost": 100
        },
        "leather_armor": {
            "item_id": "leather_armor",
            "name": "Leather Armor",
            "type": "armor",
            "effect": "max_health:10",
            "cost": 80
        }
    }

    # Dummy character
    test_char = {
        "inventory": [],
        "gold": 150,
        "health": 50,
        "max_health": 50,
        "strength": 10,
        "magic": 5,
        "item_data": item_data,   # used for equip/unequip
        "equipped_weapon": None,
        "equipped_armor": None
    }

    print("=== TEST 1: Add Items ===")
    try:
        add_item_to_inventory(test_char, "health_potion")
        add_item_to_inventory(test_char, "iron_sword")
        add_item_to_inventory(test_char, "leather_armor")
        print("Inventory:", test_char["inventory"])
    except Exception as e:
        print("Error:", e)

    print("\n=== TEST 2: Use Health Potion ===")
    try:
        result = use_item(test_char, "health_potion", item_data["health_potion"])
        print(result)
        print("Health:", test_char["health"])
        print("Inventory:", test_char["inventory"])
    except Exception as e:
        print("Error:", e)

    print("\n=== TEST 3: Equip Weapon ===")
    try:
        result = equip_weapon(test_char, "iron_sword", item_data["iron_sword"])
        print(result)
        print("Strength:", test_char["strength"])
        print("Equipped:", test_char["equipped_weapon"])
    except Exception as e:
        print("Error:", e)

    print("\n=== TEST 4: Equip Armor ===")
    try:
        result = equip_armor(test_char, "leather_armor", item_data["leather_armor"])
        print(result)
        print("Max Health:", test_char["max_health"])
        print("Equipped:", test_char["equipped_armor"])
    except Exception as e:
        print("Error:", e)

    print("\n=== TEST 5: Unequip Weapon ===")
    try:
        unequipped = unequip_weapon(test_char)
        print(f"Unequipped: {unequipped}")
        print("Strength:", test_char["strength"])
        print("Inventory:", test_char["inventory"])
    except Exception as e:
        print("Error:", e)

    print("\n=== TEST 6: Sell Armor ===")
    try:
        gold_received = sell_item(test_char, "leather_armor", item_data["leather_armor"])
        print(f"Sold for {gold_received} gold")
        print("Gold:", test_char["gold"])
        print("Inventory:", test_char["inventory"])
    except Exception as e:
        print("Error:", e)

    print("\n=== TEST 7: Display Inventory ===")
    display_inventory(test_char, item_data)

    # Test adding items
    # test_char = {'inventory': [], 'gold': 100, 'health': 80, 'max_health': 80}
    # 
    # try:
    #     add_item_to_inventory(test_char, "health_potion")
    #     print(f"Inventory: {test_char['inventory']}")
    # except InventoryFullError:
    #     print("Inventory is full!")
    
    # Test using items
    # test_item = {
    #     'item_id': 'health_potion',
    #     'type': 'consumable',
    #     'effect': 'health:20'
    # }
    # 
    # try:
    #     result = use_item(test_char, "health_potion", test_item)
    #     print(result)
    # except ItemNotFoundError:
    #     print("Item not found")

