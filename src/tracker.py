

class PerformanceTracker:
  
    def __init__(self):
        # History will store dictionaries for each puzzle attempt
        self.history = []
        
    def log(self, difficulty, question, is_correct, time_taken):
       
        self.history.append({
            "difficulty": difficulty,
            "question": question,
            "correct": is_correct,
            "time_taken": time_taken
        })
        print(f"Logged: {difficulty}, Correct: {is_correct}, Time: {time_taken:.2f}s")

    def get_last_n_results(self, n=2):
        
        return self.history[-n:]

    def get_summary(self):
      
        if not self.history:
            return {
                "total_questions": 0,
                "total_correct": 0,
                "accuracy": 0.0,
                "average_time": 0.0
            }
            
        total_questions = len(self.history)
        total_correct = sum(1 for record in self.history if record["correct"])
        total_time = sum(record["time_taken"] for record in self.history)
        
        accuracy = (total_correct / total_questions) * 100
        average_time = total_time / total_questions
        
        return {
            "total_questions": total_questions,
            "total_correct": total_correct,
            "accuracy": accuracy,
            "average_time": average_time
        }