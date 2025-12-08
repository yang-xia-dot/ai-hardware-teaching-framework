import json
import os

# Step 1: Load quiz JSON (detailed error check)
quiz_path = 'H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2\quiz_library\week2_quiz .json'
if os.path.exists(quiz_path):
    with open(quiz_path, 'r', encoding='utf-8') as f:
        quiz_data = json.load(f)
    questions = quiz_data.get('questions', [])  # Assume JSON has 'questions' list
    print("Quiz loaded: Week 2 OS Disassembly + CLIP Matching")
else:
    raise FileNotFoundError(f"{quiz_path} not found. Generate it first.")

# Step 2: Simulate running quiz (user input for answers, score calculation)
score = 0
total = len(questions)
results = []  # For logs
for q in questions:
    print(f"\nQuestion: {q['question']}")
    options = q.get('options', [])
    if options:
        for i, opt in enumerate(options, 1):
            print(f"{i}. {opt}")
        answer = input("Your answer (e.g., A or 1): ").strip().upper()
        correct = q['correct'].upper()
        if answer == correct or (answer.isdigit() and int(answer) == ord(correct) - ord('A') + 1):
            score += 1
            results.append(f"Correct: {q['question']} (Answer: {correct})")
        else:
            results.append(f"Incorrect: {q['question']} (Your: {answer}, Correct: {correct})")

# Step 3: Print score and save logs (detailed output)
print(f"\nScore: {score}/{total} ({score/total*100:.2f}%)")
print("Quiz complete. Results saved to logs/week2_quiz_results.txt")

# Save to logs (detailed file creation)
logs_path = '../logs/week2_quiz_results.txt'
os.makedirs(os.path.dirname(logs_path), exist_ok=True)
with open(logs_path, 'w', encoding='utf-8') as f:
    f.write(f"Week 2 Quiz Results:\nScore: {score}/{total}\n")
    f.write('\n'.join(results))
print(f"Logs saved: {logs_path}")