
from tracker import PerformanceTracker

# Define difficulty levels as constants
EASY = "Easy"
MEDIUM = "Medium"
HARD = "Hard"

DIFFICULTY_LEVELS = [EASY, MEDIUM, HARD]

def update_difficulty(current_difficulty, tracker):
  
    
    # Get the last two results from the tracker
    last_two_results = tracker.get_last_n_results(2)
    
    # Don't change difficulty until we have at least 2 data points
    if len(last_two_results) < 2:
        return current_difficulty
        
    all_correct = all(r["correct"] for r in last_two_results)
    all_incorrect = all(not r["correct"] for r in last_two_results)
    
    # --- Promotion Logic ---
    if all_correct:
        if current_difficulty == EASY:
            return MEDIUM  # Promote from Easy to Medium
        elif current_difficulty == MEDIUM:
            return HARD    # Promote from Medium to Hard
        elif current_difficulty == HARD:
            return HARD    # Stay at max difficulty
            
    # --- Demotion Logic ---
    elif all_incorrect:
        if current_difficulty == HARD:
            return MEDIUM  # Demote from Hard to Medium
        elif current_difficulty == MEDIUM:
            return EASY    # Demote from Medium to Easy
        elif current_difficulty == EASY:
            return EASY    # Stay at min difficulty
            
    # --- No Change ---
    else:
        return current_difficulty