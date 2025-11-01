

import random


EASY = "Easy"
MEDIUM = "Medium"
HARD = "Hard"

def generate_puzzle(difficulty):
    """
    Generates a math puzzle (question string and answer) based on the
    difficulty level.
    
    
    """
    if difficulty == EASY:
        # Easy: Single-digit addition [cite: 9]
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        question = f"{a} + {b}"
        answer = a + b
        return question, answer
        
    elif difficulty == MEDIUM:
        # Medium: Double-digit addition or subtraction
        a = random.randint(10, 50)
        b = random.randint(10, 50)
        
        if random.choice([True, False]):
            # Addition
            question = f"{a} + {b}"
            answer = a + b
        else:
            # Subtraction, ensure positive result
            if a < b:
                a, b = b, a  # Swap to make sure a is larger
            question = f"{a} - {b}"
            answer = a - b
        return question, answer
        
    elif difficulty == HARD:
        # Hard: Single-digit multiplication [cite: 9]
        a = random.randint(2, 12)
        b = random.randint(2, 9)
        question = f"{a} * {b}"
        answer = a * b
        return question, answer
        
    else:
        raise ValueError(f"Unknown difficulty level: {difficulty}")

if __name__ == '__main__':
    # Test the generator
    print(f"Easy puzzle:   {generate_puzzle(EASY)}")
    print(f"Medium puzzle: {generate_puzzle(MEDIUM)}")
    print(f"Hard puzzle:   {generate_puzzle(HARD)}")