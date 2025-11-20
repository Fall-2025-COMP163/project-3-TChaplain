"""
COMP 163 - Project 3: Quest Chronicles
Combat System Module - Starter Code

Name: [Your Name Here]

AI Usage: [Document any AI assistance used]

Handles combat mechanics
"""
import random
from custom_exceptions import (
    InvalidTargetError,
    CombatNotActiveError,
    CharacterDeadError,
    AbilityOnCooldownError
)

# ============================================================================
# ENEMY DEFINITIONS
# ============================================================================

def create_enemy(enemy_type):
    """
    Create an enemy based on type
    
    Example enemy types and stats:
    - goblin: health=50, strength=8, magic=2, xp_reward=25, gold_reward=10
    - orc: health=80, strength=12, magic=5, xp_reward=50, gold_reward=25
    - dragon: health=200, strength=25, magic=15, xp_reward=200, gold_reward=100
    
    Returns: Enemy dictionary
    Raises: InvalidTargetError if enemy_type not recognized
    """
    # TODO: Implement enemy creation
    # Return dictionary with: name, health, max_health, strength, magic, xp_reward, gold_reward
    

    et = enemy_type.lower()
    if et == "goblin":
        return {
            "name": "Goblin",
            "type": "goblin",
            "health": 50,
            "max_health": 50,
            "strength": 8,
            "magic": 2,
            "xp_reward": 25,
            "gold_reward": 10
        }
    elif et == "orc":
        return {
            "name": "Orc",
            "type": "orc",
            "health": 80,
            "max_health": 80,
            "strength": 12,
            "magic": 5,
            "xp_reward": 50,
            "gold_reward": 25
        }
    elif et == "dragon":
        return {
            "name": "Dragon",
            "type": "dragon",
            "health": 200,
            "max_health": 200,
            "strength": 25,
            "magic": 15,
            "xp_reward": 200,
            "gold_reward": 100
        }
    else:
        raise InvalidTargetError(f"Unknown enemy type: {enemy_type}")

def get_random_enemy_for_level(character_level):
    """
    Get an appropriate enemy for character's level
    
    Level 1-2: Goblins
    Level 3-5: Orcs
    Level 6+: Dragons
    
    Returns: Enemy dictionary
    """
    # TODO: Implement level-appropriate enemy selection
    # Use if/elif/else to select enemy type
    # Call create_enemy with appropriate type
    

    if character_level <= 2:
        return create_enemy("goblin")
    elif 3 <= character_level <= 5:
        return create_enemy("orc")
    else:
        return create_enemy("dragon")

# ============================================================================
# COMBAT SYSTEM
# ============================================================================

class SimpleBattle:
    """
    Simple turn-based combat system
    
    Manages combat between character and enemy
    """
    
    def __init__(self, character, enemy):
        """Initialize battle with character and enemy"""
        # TODO: Implement initialization
        # Store character and enemy
        # Set combat_active flag
        # Initialize turn counter
        
        
        """Initialize battle state."""
        # store references (mutations affect provided dicts)
        self.character = character
        self.enemy = enemy
        self.combat_active = True
        self.turn = 0
        # simple place to store ability cooldowns if needed
        self.cooldowns = {}
        # Record log messages
        self.log = []
    
    def start_battle(self):
        """
        Start the combat loop
        
        Returns: Dictionary with battle results:
                {'winner': 'player'|'enemy', 'xp_gained': int, 'gold_gained': int}
        
        Raises: CharacterDeadError if character is already dead
        """
        # TODO: Implement battle loop
        # Check character isn't dead
        # Loop until someone dies
        # Award XP and gold if player wins
        

        if self.character.get("health", 0) <= 0:
            raise CharacterDeadError("Character is dead and cannot fight.")

        # Continue until combat ends
        while self.combat_active:
            self.turn += 1
            # Player's action: basic attack (non-interactive)
            self.player_basic_attack()

            end = self.check_battle_end()
            if end:
                break

            # Enemy's turn
            self.enemy_turn()

            end = self.check_battle_end()
            if end:
                break

        # Determine outcome
        result = self.check_battle_end()
        if result == "player":
            rewards = get_victory_rewards(self.enemy)
            xp = rewards.get("xp", 0)
            gold = rewards.get("gold", 0)
            # award player
            self.character["experience"] = self.character.get("experience", 0) + xp
            self.character["gold"] = self.character.get("gold", 0) + gold
            self.combat_active = False
            return {"winner": "player", "xp_gained": xp, "gold_gained": gold}
        elif result == "enemy":
            self.combat_active = False
            return {"winner": "enemy", "xp_gained": 0, "gold_gained": 0}
        else:
            # escaped or other end
            self.combat_active = False
            return {"winner": "escaped", "xp_gained": 0, "gold_gained": 0}

    # ---- internal actions ----

    def player_basic_attack(self):
        """Perform a basic attack from player to enemy."""
        if not self.combat_active:
            raise CombatNotActiveError("Combat is not active.")
        dmg = self.calculate_damage(self.character, self.enemy)
        self.apply_damage(self.enemy, dmg)
        display_battle_log(f"{self.character.get('name', 'Player')} hits {self.enemy.get('name', 'Enemy')} for {dmg} damage.")
        display_combat_stats(self.character, self.enemy)
    
    def player_turn(self):
        """
        Handle player's turn
        
        Displays options:
        1. Basic Attack
        2. Special Ability (if available)
        3. Try to Run
        
        Raises: CombatNotActiveError if called outside of battle
        """
        # TODO: Implement player turn
        # Check combat is active
        # Display options
        # Get player choice
        # Execute chosen action
        

        return self.player_basic_attack()
    
    def enemy_turn(self):
        """
        Handle enemy's turn - simple AI
        
        Enemy always attacks
        
        Raises: CombatNotActiveError if called outside of battle
        """
        # TODO: Implement enemy turn
        # Check combat is active
        # Calculate damage
        # Apply to character
        

        """Enemy always attacks once per turn."""
        if not self.combat_active:
            raise CombatNotActiveError("Combat is not active.")
        dmg = self.calculate_damage(self.enemy, self.character)
        self.apply_damage(self.character, dmg)
        display_battle_log(f"{self.enemy.get('name', 'Enemy')} hits {self.character.get('name', 'Player')} for {dmg} damage.")
        display_combat_stats(self.character, self.enemy)
    
    def calculate_damage(self, attacker, defender):
        """
        Calculate damage from attack
        
        Damage formula: attacker['strength'] - (defender['strength'] // 4)
        Minimum damage: 1
        
        Returns: Integer damage amount
        """
        # TODO: Implement damage calculation
        

        """
        Damage = attacker['strength'] - (defender['strength'] // 4)
        Minimum damage is 1.
        """
        atk = int(attacker.get("strength", 0))
        def_str = int(defender.get("strength", 0))
        raw = atk - (def_str // 4)
        return max(1, raw)
    
    def apply_damage(self, target, damage):
        """
        Apply damage to a character or enemy
        
        Reduces health, prevents negative health
        """
        # TODO: Implement damage application
        

        """Apply damage to target dict; ensure health doesn't go below 0."""
        current = int(target.get("health", 0))
        new = max(0, current - int(damage))
        target["health"] = new
    
    def check_battle_end(self):
        """
        Check if battle is over
        
        Returns: 'player' if enemy dead, 'enemy' if character dead, None if ongoing
        """
        # TODO: Implement battle end check
        

        """
        Return 'player' if enemy dead, 'enemy' if player dead, None if ongoing.
        """
        if self.enemy.get("health", 0) <= 0:
            return "player"
        if self.character.get("health", 0) <= 0:
            return "enemy"
        # combat_active could be False if escaped
        if not self.combat_active:
            return "escaped"
        return None
    
    def attempt_escape(self):
        """
        Try to escape from battle
        
        50% success chance
        
        Returns: True if escaped, False if failed
        """
        # TODO: Implement escape attempt
        # Use random number or simple calculation
        # If successful, set combat_active to False
        

        """
        50% chance to escape. If successful, set combat_active False and return True.
        """
        if not self.combat_active:
            raise CombatNotActiveError("Combat is not active.")
        success = random.choice([True, False])
        if success:
            self.combat_active = False
            display_battle_log(f"{self.character.get('name', 'Player')} escaped successfully!")
            return True
        else:
            display_battle_log(f"{self.character.get('name', 'Player')} failed to escape!")
            return False

# ============================================================================
# SPECIAL ABILITIES
# ============================================================================

def use_special_ability(character, enemy):
    """
    Use character's class-specific special ability
    
    Example abilities by class:
    - Warrior: Power Strike (2x strength damage)
    - Mage: Fireball (2x magic damage)
    - Rogue: Critical Strike (3x strength damage, 50% chance)
    - Cleric: Heal (restore 30 health)
    
    Returns: String describing what happened
    Raises: AbilityOnCooldownError if ability was used recently
    """
    # TODO: Implement special abilities
    # Check character class
    # Execute appropriate ability
    # Track cooldowns (optional advanced feature)
    

    """
    Dispatch the class-specific special ability.
    Returns a string describing effect.
    This simplified implementation does not track cooldowns.
    """
    cls = character.get("class", "")
    if cls == "Warrior":
        return warrior_power_strike(character, enemy)
    elif cls == "Mage":
        return mage_fireball(character, enemy)
    elif cls == "Rogue":
        return rogue_critical_strike(character, enemy)
    elif cls == "Cleric":
        return cleric_heal(character)
    else:
        raise InvalidTargetError(f"No special ability for class: {cls}")

def warrior_power_strike(character, enemy):
    """Warrior special ability"""
    # TODO: Implement power strike
    # Double strength damage
    

    """Warrior: deals 2x strength as damage to enemy."""
    dmg = max(1, int(character.get("strength", 0)) * 2)
    enemy["health"] = max(0, enemy.get("health", 0) - dmg)
    display_battle_log(f"{character.get('name')} uses Power Strike for {dmg} damage!")
    return f"Power Strike dealt {dmg} damage"

def mage_fireball(character, enemy):
    """Mage special ability"""
    # TODO: Implement fireball
    # Double magic damage
    

    """Mage: deals 2x magic as damage to enemy."""
    dmg = max(1, int(character.get("magic", 0)) * 2)
    enemy["health"] = max(0, enemy.get("health", 0) - dmg)
    display_battle_log(f"{character.get('name')} casts Fireball for {dmg} damage!")
    return f"Fireball dealt {dmg} damage"


def rogue_critical_strike(character, enemy):
    """Rogue special ability"""
    # TODO: Implement critical strike
    # 50% chance for triple damage
    

    """Rogue: 50% chance to deal 3x strength, otherwise normal strength damage."""
    chance = random.random()
    if chance < 0.5:
        dmg = max(1, int(character.get("strength", 0)) * 3)
        enemy["health"] = max(0, enemy.get("health", 0) - dmg)
        display_battle_log(f"{character.get('name')} lands a CRITICAL STRIKE for {dmg} damage!")
        return f"Critical Strike dealt {dmg} damage"
    else:
        dmg = max(1, int(character.get("strength", 0)))
        enemy["health"] = max(0, enemy.get("health", 0) - dmg)
        display_battle_log(f"{character.get('name')} attacks for {dmg} damage (no crit).")
        return f"Attack dealt {dmg} damage"

def cleric_heal(character):
    """Cleric special ability"""
    # TODO: Implement healing
    # Restore 30 HP (not exceeding max_health)
    

    """Cleric: restore 30 health (not exceeding max_health)."""
    max_h = int(character.get("max_health", 0))
    cur = int(character.get("health", 0))
    heal_amount = min(30, max_h - cur)
    character["health"] = cur + heal_amount
    display_battle_log(f"{character.get('name')} casts Heal and restores {heal_amount} HP.")
    return f"Healed {heal_amount} HP"

# ============================================================================
# COMBAT UTILITIES
# ============================================================================

def can_character_fight(character):
    """
    Check if character is in condition to fight
    
    Returns: True if health > 0 and not in battle
    """
    # TODO: Implement fight check
    

    try:
        return int(character.get("health", 0)) > 0
    except Exception:
        return False

def get_victory_rewards(enemy):
    """
    Calculate rewards for defeating enemy
    
    Returns: Dictionary with 'xp' and 'gold'
    """
    # TODO: Implement reward calculation
    

    """Return dict {'xp': int, 'gold': int} from enemy fields."""
    return {"xp": int(enemy.get("xp_reward", 0)), "gold": int(enemy.get("gold_reward", 0))}

def display_combat_stats(character, enemy):
    """
    Display current combat status
    
    Shows both character and enemy health/stats
    """
    # TODO: Implement status display
    
    

    """Print a compact status line for both combatants."""
    print(f"\n{character.get('name', 'Player')}: HP={character.get('health',0)}/{character.get('max_health',0)}")
    print(f"{enemy.get('name', 'Enemy')}: HP={enemy.get('health',0)}/{enemy.get('max_health',0)}")


def display_battle_log(message):
    """
    Display a formatted battle message
    """
    # TODO: Implement battle log display
    

    """Print a formatted battle message and also keep it simple for tests."""
    print(f">>> {message}")
    

# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== COMBAT SYSTEM TEST ===")
    print("=== COMBAT SYSTEM TEST ===")
    
# Create a test character and enemy and run a simple battle
    test_char = {
        "name": "TestHero",
        "class": "Warrior",
        "health": 120,
        "max_health": 120,
        "strength": 15,
        "magic": 5,
        "experience": 0,
        "gold": 0
    }

    goblin = create_enemy("goblin")
    battle = SimpleBattle(test_char, goblin)
    result = battle.start_battle()
    print("Battle result:", result)
    print("Post-battle character state:", test_char)
    # Test enemy creation
    # try:
    #     goblin = create_enemy("goblin")
    #     print(f"Created {goblin['name']}")
    # except InvalidTargetError as e:
    #     print(f"Invalid enemy: {e}")
    
    # Test battle
    # test_char = {
    #     'name': 'Hero',
    #     'class': 'Warrior',
    #     'health': 120,
    #     'max_health': 120,
    #     'strength': 15,
    #     'magic': 5
    # }
    #
    # battle = SimpleBattle(test_char, goblin)
    # try:
    #     result = battle.start_battle()
    #     print(f"Battle result: {result}")
    # except CharacterDeadError:
    #     print("Character is dead!")

