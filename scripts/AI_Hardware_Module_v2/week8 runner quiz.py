import numpy as np
import pandas as pd
import json
import os

# Define root directory
root_dir = r'H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2'
quiz_library_dir = os.path.join(root_dir, 'quiz_library')
logs_dir = os.path.join(root_dir, 'logs')

# Create directories if not exist
os.makedirs(quiz_library_dir, exist_ok=True)
os.makedirs(logs_dir, exist_ok=True)

# Generate week8_adaptive_quiz.json
quiz_data = {
  "week": 8,
  "theme": "Pinnacle Showdown - Showcase Summit",
  "description": "This adaptive quiz summarizes the 8-week module, assessing overall AI literacy, interest growth, and project integration. Divided into three levels: Basic (basic recap), Intermediate (project showcase), Advanced (global trends report). Likert scale: 1 (Strongly Disagree) to 5 (Strongly Agree). 8 questions total, adaptive per level for final evaluation.",
  "levels": {
    "Basic": {
      "questions": [
        {"id": 1, "question": "The hardware simulations (e.g., Logisim circuits) helped me understand basic computer assembly.", "type": "likert"},
        {"id": 2, "question": "I feel more confident in low-resource AI applications after the 8 weeks.", "type": "likert"}
      ]
    },
    "Intermediate": {
      "questions": [
        {"id": 3, "question": "My project demo integrated ethics and optimization effectively.", "type": "likert"},
        {"id": 4, "question": "The voting and showcase boosted my interest in rural AI projects.", "type": "likert"},
        {"id": 5, "question": "UNESCO principles were useful in my farm circuit design.", "type": "likert"}
      ]
    },
    "Advanced": {
      "questions": [
        {"id": 6, "question": "The SDT+TAM paths (Han et al., 2025) explain my literacy growth over 8 weeks.", "type": "likert"},
        {"id": 7, "question": "Global trends like quantum AI will impact rural education (Panjwani, 2024).", "type": "likert"},
        {"id": 8, "question": "My overall AI literacy improved by at least 25% through the module.", "type": "likert"}
      ]
    }
  },
  "instructions": "Assign questions based on student level: 8 Basic, 9 Intermediate, 8 Advanced. Simulate responses with numpy normal distribution (mean 3.5 pre, 4.3 post). Save to quiz_library/week8_adaptive_quiz.json."
}

with open(os.path.join(quiz_library_dir, 'week8_adaptive_quiz.json'), 'w', encoding='utf-8') as f:
    json.dump(quiz_data, f, indent=2, ensure_ascii=False)

# Simulate student responses and generate week8_results.xlsx
np.random.seed(42)  # For reproducibility
students = [f"S{i:02d}" for i in range(1, 26)]
levels = np.random.choice(['Basic', 'Intermediate', 'Advanced'], size=25, p=[0.32, 0.36, 0.32])  # Approx 8/9/8
pre_scores = np.random.normal(loc=67, scale=10, size=25).clip(40, 90)  # Summary scores out of 100
post_scores = pre_scores + np.random.normal(loc=18, scale=6, size=25).clip(0, 40)
post_scores = np.clip(post_scores, 40, 100)
improvements = post_scores - pre_scores

data = {
    'StudentID': students,
    'Level': levels,
    'PreScore': pre_scores,
    'PostScore': post_scores,
    'Improvement': improvements
}
df = pd.DataFrame(data)
df.to_excel(os.path.join(logs_dir, 'week8_results.xlsx'), index=False)

# Print confirmation
print("Generated quiz_library/week8_adaptive_quiz.json and logs/week8_results.xlsx at:")
print(os.path.join(quiz_library_dir, 'week8_adaptive_quiz.json'))
print(os.path.join(logs_dir, 'week8_results.xlsx'))