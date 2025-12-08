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

# Generate week7_ethics_quiz.json
quiz_data = {
  "week": 7,
  "theme": "Ethics Maze - Performance Theater",
  "description": "This quiz assesses students' understanding of AI hardware/software ethics, focusing on privacy risks, biases in ViT applications, and UNESCO digital equity principles. Divided into three levels: Basic (fundamental privacy), Intermediate (bias identification), Advanced (global trends and CFA awakening). Likert scale: 1 (Strongly Disagree) to 5 (Strongly Agree). 10 questions total, adaptive per level.",
  "levels": {
    "Basic": {
      "questions": [
        {"id": 1, "question": "AI hardware like sensors in rural farms can leak personal data if not protected.", "type": "likert"},
        {"id": 2, "question": "Basic privacy risks in computer maintenance include sharing logs without consent.", "type": "likert"},
        {"id": 3, "question": "Ethical use of AI means considering how it affects village communities.", "type": "likert"}
      ]
    },
    "Intermediate": {
      "questions": [
        {"id": 4, "question": "ViT models can introduce biases in farm crop detection if trained on urban data.", "type": "likert"},
        {"id": 5, "question": "Role-playing ethics scenarios helps identify biases in hardware simulations.", "type": "likert"},
        {"id": 6, "question": "In low-resource settings, AI ethics should prioritize data fairness for all users.", "type": "likert"},
        {"id": 7, "question": "Repairing virtual OS (like QEMU) involves ethical handling of simulated data.", "type": "likert"}
      ]
    },
    "Advanced": {
      "questions": [
        {"id": 8, "question": "UNESCO's 5 principles can mitigate global AI biases in rural education.", "type": "likert"},
        {"id": 9, "question": "CFA validation (Kong & Zhu, 2025) enhances awakening to AI ethical challenges.", "type": "likert"},
        {"id": 10, "question": "SDT+TAM paths (Han et al., 2025) link autonomy to ethical acceptance in ViT apps.", "type": "likert"}
      ]
    }
  },
  "instructions": "Assign questions based on student level: 8 Basic, 9 Intermediate, 8 Advanced. Simulate responses with numpy normal distribution (mean 3.0 pre, 4.2 post). Save to quiz_library/week7_ethics_quiz.json."
}

with open(os.path.join(quiz_library_dir, 'week7_ethics_quiz.json'), 'w', encoding='utf-8') as f:
    json.dump(quiz_data, f, indent=2, ensure_ascii=False)

# Simulate student responses and generate week7_results.xlsx
np.random.seed(42)  # For reproducibility
students = [f"S{i:02d}" for i in range(1, 26)]
levels = np.random.choice(['Basic', 'Intermediate', 'Advanced'], size=25, p=[0.32, 0.36, 0.32])  # Approx 8/9/8
pre_scores = np.random.normal(loc=65, scale=11, size=25).clip(40, 90)  # Ethics scores out of 100
post_scores = pre_scores + np.random.normal(loc=16, scale=5, size=25).clip(0, 35)
post_scores = np.clip(post_scores, 40, 100)
improvements = post_scores - pre_scores

data = {
    'StudentID': students,
    'Level': levels,
    'PreEthicsScore': pre_scores,
    'PostEthicsScore': post_scores,
    'Improvement': improvements
}
df = pd.DataFrame(data)
df.to_excel(os.path.join(logs_dir, 'week7_results.xlsx'), index=False)

# Print confirmation
print("Generated quiz_library/week7_ethics_quiz.json and logs/week7_results.xlsx at:")
print(os.path.join(quiz_library_dir, 'week7_ethics_quiz.json'))
print(os.path.join(logs_dir, 'week7_results.xlsx'))