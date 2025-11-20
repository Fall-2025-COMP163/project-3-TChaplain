"""
COMP 163 - Project 3: Quest Chronicles
Quest Handler Module - Starter Code

Name: Tajaunie Chaplain

AI Usage: Completed with assistance from ChatGPT

This module handles quest management, dependencies, and completion.
"""

from custom_exceptions import (
    QuestNotFoundError,
    QuestRequirementsNotMetError,
    QuestAlreadyCompletedError,
    QuestNotActiveError,
    InsufficientLevelError
)

# ============================================================================
# QUEST MANAGEMENT
# ============================================================================

def accept_quest(character, quest_id, quest_data_dict):
    """
    Accept a new quest
    
    Args:
        character: Character dictionary
        quest_id: Quest to accept
        quest_data_dict: Dictionary of all quest data
    
    Requirements to accept quest:
    - Character level >= quest required_level
    - Prerequisite quest completed (if any)
    - Quest not already completed
    - Quest not already active
    
    Returns: True if quest accepted
    Raises:
        QuestNotFoundError if quest_id not in quest_data_dict
        InsufficientLevelError if character level too low
        QuestRequirementsNotMetError if prerequisite not completed
        QuestAlreadyCompletedError if quest already done
    """
    # TODO: Implement quest acceptance
    # Check quest exists
    # Check level requirement
    # Check prerequisite (if not "NONE")
    # Check not already completed
    # Check not already active
    # Add to character['active_quests']
    pass

    """
    Accept a new quest if requirements are met.
    Raises appropriate errors if not allowed.
    """

    # --- Validate quest exists ---
    if quest_id not in quest_data_dict:
        raise QuestNotFoundError(f"Quest '{quest_id}' does not exist.")

    quest = quest_data_dict[quest_id]

    # --- Already completed? ---
    if quest_id in character["completed_quests"]:
        raise QuestAlreadyCompletedError(f"Quest '{quest_id}' already completed.")

    # --- Already active? ---
    if quest_id in character["active_quests"]:
        raise QuestRequirementsNotMetError(f"Quest '{quest_id}' already active.")

    # --- Level requirement ---
    if character.get("level", 1) < quest["required_level"]:
        raise InsufficientLevelError(
            f"Level {quest['required_level']} required to accept quest '{quest_id}'."
        )

    # --- Prerequisite requirement ---
    prereq = quest["prerequisite"]
    if prereq != "NONE" and prereq not in character["completed_quests"]:
        raise QuestRequirementsNotMetError(
            f"Must complete prerequisite quest '{prereq}' first."
        )

    # --- Accept quest ---
    character["active_quests"].append(quest_id)
    return True

def complete_quest(character, quest_id, quest_data_dict):
    """
    Complete an active quest and grant rewards
    
    Args:
        character: Character dictionary
        quest_id: Quest to complete
        quest_data_dict: Dictionary of all quest data
    
    Rewards:
    - Experience points (reward_xp)
    - Gold (reward_gold)
    
    Returns: Dictionary with reward information
    Raises:
        QuestNotFoundError if quest_id not in quest_data_dict
        QuestNotActiveError if quest not in active_quests
    """
    # TODO: Implement quest completion
    # Check quest exists
    # Check quest is active
    # Remove from active_quests
    # Add to completed_quests
    # Grant rewards (use character_manager.gain_experience and add_gold)
    # Return reward summary
    pass

    """
    Complete an active quest and grant rewards.
    Returns a dictionary: {'xp': X, 'gold': Y}
    """

    # --- Validate quest exists ---
    if quest_id not in quest_data_dict:
        raise QuestNotFoundError(f"Quest '{quest_id}' does not exist.")

    # --- Must be active ---
    if quest_id not in character["active_quests"]:
        raise QuestNotActiveError(f"Cannot complete '{quest_id}' — not active.")

    quest = quest_data_dict[quest_id]

    # --- Remove from active & add to completed ---
    character["active_quests"].remove(quest_id)
    character["completed_quests"].append(quest_id)

    # --- Apply rewards ---
    xp_reward = quest["reward_xp"]
    gold_reward = quest["reward_gold"]

    character["experience"] += xp_reward
    character["gold"] += gold_reward

    return {"xp": xp_reward, "gold": gold_reward}

def abandon_quest(character, quest_id):
    """
    Remove a quest from active quests without completing it
    
    Returns: True if abandoned
    Raises: QuestNotActiveError if quest not active
    """
    # TODO: Implement quest abandonment
    pass

    """
    Remove a quest from active quests without completing it.
    """

    if quest_id not in character["active_quests"]:
        raise QuestNotActiveError(f"Quest '{quest_id}' is not active.")

    character["active_quests"].remove(quest_id)
    return True



def get_active_quests(character, quest_data_dict):
    """
    Get full data for all active quests
    
    Returns: List of quest dictionaries for active quests
    """
    # TODO: Implement active quest retrieval
    # Look up each quest_id in character['active_quests']
    # Return list of full quest data dictionaries
    pass

    """
    Return full data dictionaries for all active quests.
    """
    return [quest_data_dict[qid] for qid in character["active_quests"]]


def get_completed_quests(character, quest_data_dict):
    """
    Get full data for all completed quests
    
    Returns: List of quest dictionaries for completed quests
    """
    # TODO: Implement completed quest retrieval
    pass

    """
    Return full data dictionaries for all completed quests.
    """
    return [quest_data_dict[qid] for qid in character["completed_quests"]]

def get_available_quests(character, quest_data_dict):
    """
    Get quests that character can currently accept
    
    Available = meets level req + prerequisite done + not completed + not active
    
    Returns: List of quest dictionaries
    """
    # TODO: Implement available quest search
    # Filter all quests by requirements
    pass

    """
    Return list of quests character can accept right now.
    This does NOT raise errors — simply returns valid ones.
    """

    available = []

    for qid, quest in quest_data_dict.items():
        # Skip completed
        if qid in character["completed_quests"]:
            continue

        # Skip active
        if qid in character["active_quests"]:
            continue

        # Level requirement
        if character["level"] < quest["required_level"]:
            continue

        # Prerequisite
        prereq = quest["prerequisite"]
        if prereq != "NONE" and prereq not in character["completed_quests"]:
            continue

        available.append(quest)

    return available

# ============================================================================
# QUEST TRACKING
# ============================================================================

def is_quest_completed(character, quest_id):
    """
    Check if a specific quest has been completed
    
    Returns: True if completed, False otherwise
    """
    # TODO: Implement completion check
    pass

    """Return True if quest_id is in completed_quests."""
    return quest_id in character["completed_quests"]

def is_quest_active(character, quest_id):
    """
    Check if a specific quest is currently active
    
    Returns: True if active, False otherwise
    """
    # TODO: Implement active check
    pass

    """Return True if quest_id is in active_quests."""
    return quest_id in character["active_quests"]


def can_accept_quest(character, quest_id, quest_data_dict):
    """
    Check if character meets all requirements to accept quest
    
    Returns: True if can accept, False otherwise
    Does NOT raise exceptions - just returns boolean
    """
    # TODO: Implement requirement checking
    # Check all requirements without raising exceptions
    pass

    """
    Same checks as accept_quest, but returns True/False instead of raising.
    """

    if quest_id not in quest_data_dict:
        return False

    quest = quest_data_dict[quest_id]

    if quest_id in character["completed_quests"]:
        return False

    if quest_id in character["active_quests"]:
        return False

    if character["level"] < quest["required_level"]:
        return False

    prereq = quest["prerequisite"]
    if prereq != "NONE" and prereq not in character["completed_quests"]:
        return False

    return True

def get_quest_prerequisite_chain(quest_id, quest_data_dict):
    """
    Get the full chain of prerequisites for a quest
    
    Returns: List of quest IDs in order [earliest_prereq, ..., quest_id]
    Example: If Quest C requires Quest B, which requires Quest A:
             Returns ["quest_a", "quest_b", "quest_c"]
    
    Raises: QuestNotFoundError if quest doesn't exist
    """
    # TODO: Implement prerequisite chain tracing
    # Follow prerequisite links backwards
    # Build list in reverse order
    pass

    """
    Return ordered list of prerequisite quest IDs leading to quest_id.
    Raises error if quest_id does not exist.
    """

    if quest_id not in quest_data_dict:
        raise QuestNotFoundError(f"Quest '{quest_id}' does not exist.")

    chain = []
    current = quest_id

    while True:
        if current not in quest_data_dict:
            raise QuestNotFoundError(f"Quest '{current}' in chain does not exist.")

        chain.append(current)

        prereq = quest_data_dict[current]["prerequisite"]
        if prereq == "NONE":
            break

        current = prereq

    chain.reverse()
    return chain

# ============================================================================
# QUEST STATISTICS
# ============================================================================

def get_quest_completion_percentage(character, quest_data_dict):
    """
    Calculate what percentage of all quests have been completed
    
    Returns: Float between 0 and 100
    """
    # TODO: Implement percentage calculation
    # total_quests = len(quest_data_dict)
    # completed_quests = len(character['completed_quests'])
    # percentage = (completed / total) * 100
    pass

    """
    Percentage of all quests completed (0–100).
    """

    total = len(quest_data_dict)
    if total == 0:
        return 0.0

    completed = len(character["completed_quests"])
    return (completed / total) * 100

def get_total_quest_rewards_earned(character, quest_data_dict):
    """
    Calculate total XP and gold earned from completed quests
    
    Returns: Dictionary with 'total_xp' and 'total_gold'
    """
    # TODO: Implement reward calculation
    # Sum up reward_xp and reward_gold for all completed quests
    pass

    """
    Add up rewards of all completed quests.
    Returns: {'total_xp': X, 'total_gold': Y}
    """

    total_xp = 0
    total_gold = 0

    for qid in character["completed_quests"]:
        if qid in quest_data_dict:
            quest = quest_data_dict[qid]
            total_xp += quest["reward_xp"]
            total_gold += quest["reward_gold"]

    return {"total_xp": total_xp, "total_gold": total_gold}

def get_quests_by_level(quest_data_dict, min_level, max_level):
    """
    Get all quests within a level range
    
    Returns: List of quest dictionaries
    """
    # TODO: Implement level filtering
    pass

    """
    Return all quests whose required_level is between min_level and max_level.
    """
    return [
        quest
        for quest in quest_data_dict.values()
        if min_level <= quest["required_level"] <= max_level
    ]


# ============================================================================
# DISPLAY FUNCTIONS
# ============================================================================

def display_quest_info(quest_data):
    """
    Display formatted quest information
    
    Shows: Title, Description, Rewards, Requirements
    """
    # TODO: Implement quest display
    print(f"\n=== {quest_data['title']} ===")
    print(f"Description: {quest_data['description']}")
    # ... etc
    pass

    """Pretty-formatted output for a single quest."""
    print(f"\n=== {quest_data['title']} ===")
    print(f"Description: {quest_data['description']}")
    print(f"Required Level: {quest_data['required_level']}")
    print(f"Prerequisite: {quest_data['prerequisite']}")
    print(f"Rewards: {quest_data['reward_xp']} XP, {quest_data['reward_gold']} Gold")

def display_quest_list(quest_list):
    """
    Display a list of quests in summary format
    
    Shows: Title, Required Level, Rewards
    """
    # TODO: Implement quest list display
    pass

    """Show list of quests in summary form."""
    print("\n=== Quest List ===")
    for quest in quest_list:
        print(f"- {quest['title']} (Lvl {quest['required_level']})  "
              f"[Rewards: {quest['reward_xp']} XP, {quest['reward_gold']} Gold]")

def display_character_quest_progress(character, quest_data_dict):
    """
    Display character's quest statistics and progress
    
    Shows:
    - Active quests count
    - Completed quests count
    - Completion percentage
    - Total rewards earned
    """
    # TODO: Implement progress display
    pass

    """Display active/completed quests + stats."""
    total = len(quest_data_dict)
    completed = len(character["completed_quests"])
    active = len(character["active_quests"])
    percent = get_quest_completion_percentage(character, quest_data_dict)
    rewards = get_total_quest_rewards_earned(character, quest_data_dict)

    print("\n=== Quest Progress ===")
    print(f"Active Quests: {active}")
    print(f"Completed Quests: {completed}/{total}")
    print(f"Completion: {percent:.2f}%")
    print(f"Total Rewards Earned: {rewards['total_xp']} XP, {rewards['total_gold']} Gold")


# ============================================================================
# VALIDATION
# ============================================================================

def validate_quest_prerequisites(quest_data_dict):
    """
    Validate that all quest prerequisites exist
    
    Checks that every prerequisite (that's not "NONE") refers to a real quest
    
    Returns: True if all valid
    Raises: QuestNotFoundError if invalid prerequisite found
    """
    # TODO: Implement prerequisite validation
    # Check each quest's prerequisite
    # Ensure prerequisite exists in quest_data_dict
    pass

    """
    Ensure all prerequisites exist.
    """

    for qid, quest in quest_data_dict.items():
        prereq = quest["prerequisite"]
        if prereq != "NONE" and prereq not in quest_data_dict:
            raise QuestNotFoundError(
                f"Quest '{qid}' has invalid prerequisite '{prereq}'."
            )

    return True


# ============================================================================
# TESTING
# ============================================================================

if __name__ == "__main__":
    print("=== QUEST HANDLER TEST ===")

    # ---------------------------------------------------------
    # Test Character
    # ---------------------------------------------------------
    test_char = {
        "name": "Tester",
        "class": "Warrior",
        "level": 1,
        "health": 100,
        "max_health": 100,
        "strength": 10,
        "magic": 5,
        "experience": 0,
        "gold": 100,
        "inventory": [],
        "active_quests": [],
        "completed_quests": []
    }

    # ---------------------------------------------------------
    # Test Quest Data
    # ---------------------------------------------------------
    test_quests = {
        "first_quest": {
            "quest_id": "first_quest",
            "title": "First Steps",
            "description": "Complete your first quest.",
            "reward_xp": 50,
            "reward_gold": 25,
            "required_level": 1,
            "prerequisite": "NONE"
        },
        "second_quest": {
            "quest_id": "second_quest",
            "title": "A Harder Path",
            "description": "Complete the next challenge.",
            "reward_xp": 100,
            "reward_gold": 50,
            "required_level": 2,
            "prerequisite": "first_quest"
        }
    }

    print("\n--- TEST: Accepting first quest ---")
    try:
        accept_quest(test_char, "first_quest", test_quests)
        print("SUCCESS: First quest accepted.")
    except QuestRequirementsNotMetError as e:
        print(f"FAIL: Could not accept first quest: {e}")

    print("\n--- TEST: Completing first quest ---")
    try:
        complete_quest(test_char, "first_quest", test_quests)
        print("SUCCESS: First quest completed.")
        print(f"XP: {test_char['experience']} | GOLD: {test_char['gold']}")
    except QuestRequirementsNotMetError as e:
        print(f"FAIL: Could not complete quest: {e}")

    print("\n--- TEST: Attempting to accept second quest BEFORE level up ---")
    try:
        accept_quest(test_char, "second_quest", test_quests)
        print("ERROR: Should NOT have accepted second quest yet!")
    except QuestRequirementsNotMetError as e:
        print(f"Correct behavior: {e}")

    print("\n--- Simulating Level Up to Level 2 ---")
    test_char["level"] = 2
    print(f"Character is now level {test_char['level']}")

    print("\n--- TEST: Accepting second quest AFTER reaching required level ---")
    try:
        accept_quest(test_char, "second_quest", test_quests)
        print("SUCCESS: Second quest accepted.")
    except QuestRequirementsNotMetError as e:
        print(f"FAIL: Should have accepted second quest: {e}")

    print("\n--- TEST: Completing second quest ---")
    try:
        complete_quest(test_char, "second_quest", test_quests)
        print("SUCCESS: Second quest completed.")
        print(f"XP: {test_char['experience']} | GOLD: {test_char['gold']}")
    except QuestRequirementsNotMetError as e:
        print(f"FAIL: Could not complete second quest: {e}")

    print("\n=== TESTING COMPLETE ===")
    
    # Test data
    # test_char = {
    #     'level': 1,
    #     'active_quests': [],
    #     'completed_quests': [],
    #     'experience': 0,
    #     'gold': 100
    # }
    #
    # test_quests = {
    #     'first_quest': {
    #         'quest_id': 'first_quest',
    #         'title': 'First Steps',
    #         'description': 'Complete your first quest',
    #         'reward_xp': 50,
    #         'reward_gold': 25,
    #         'required_level': 1,
    #         'prerequisite': 'NONE'
    #     }
    # }
    #
    # try:
    #     accept_quest(test_char, 'first_quest', test_quests)
    #     print("Quest accepted!")
    # except QuestRequirementsNotMetError as e:
    #     print(f"Cannot accept: {e}")

