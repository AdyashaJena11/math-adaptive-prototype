

import time
import puzzle_generator
import adaptive_engine
from tracker import PerformanceTracker

# --- Configuration ---
NUM_QUESTIONS = 10
DIFFICULTY_LEVELS = {
    "EASY": adaptive_engine.EASY,
    "MEDIUM": adaptive_engine.MEDIUM,
    "HARD": adaptive_engine.HARD
}
# ---

def get_initial_difficulty():
    """
    Asks the user to select an initial difficulty level. [cite: 17]
    """
    print("Welcome to Math Adventures! [cite: 2]")
    name = input("Please enter your name: ")
    
    while True:
        print("\nChoose your starting difficulty:")
        print("1: Easy")
        print("2: Medium")
        print("3: Hard")
        choice = input("Enter number (1-3): ")
        
        if choice == '1':
            return name, DIFFICULTY_LEVELS["EASY"]
        elif choice == '2':
            return name, DIFFICULTY_LEVELS["MEDIUM"]
        elif choice == '3':
            return name, DIFFICULTY_LEVELS["HARD"]
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def main():
    """
    Main application loop.
    """
    player_name, current_difficulty = get_initial_difficulty()
    player_tracker = PerformanceTracker()
    
    print(f"\nAlright {player_name}, let's start! You are on {current_difficulty} difficulty.")
    
    for i in range(NUM_QUESTIONS):
        print(f"\n--- Question {i + 1}/{NUM_QUESTIONS} | Difficulty: {current_difficulty} ---")
        
        # 1. Generate puzzle [cite: 11]
        question, correct_answer = puzzle_generator.generate_puzzle(current_difficulty)
        
        # 2. Track performance (time and correctness) [cite: 12, 19]
        start_time = time.time()
        user_answer_str = input(f"What is {question}? ")
        end_time = time.time()
        
        time_taken = end_time - start_time
        
        # Basic input validation
        try:
            user_answer_int = int(user_answer_str)
            is_correct = (user_answer_int == correct_answer)
        except ValueError:
            is_correct = False
            
        if is_correct:
            print(f"Correct! You took {time_taken:.2f} seconds.")
        else:
            print(f"Incorrect. The correct answer was {correct_answer}.")
            
        # 3. Log performance 
        player_tracker.log(current_difficulty, question, is_correct, time_taken)
        
        # 4. Adapt difficulty [cite: 13, 21]
        new_difficulty = adaptive_engine.update_difficulty(current_difficulty, player_tracker)
        
        if new_difficulty != current_difficulty:
            print(f"Your difficulty has been adjusted to: {new_difficulty}")
            current_difficulty = new_difficulty
            
    # 5. Display summary [cite: 14, 25]
    print("\n--- Session Complete! ---")
    summary = player_tracker.get_summary()
    print(f"Here's your summary, {player_name}:")
    print(f"  Total Questions: {summary['total_questions']}")
    print(f"  Accuracy: {summary['accuracy']:.2f}%")
    print(f"  Average Time: {summary['average_time']:.2f} seconds per question")
    print(f"  Next recommended level: {current_difficulty}")  # [cite: 26]

if __name__ == "__main__":
    main()