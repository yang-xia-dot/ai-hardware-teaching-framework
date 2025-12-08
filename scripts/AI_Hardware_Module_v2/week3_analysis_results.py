import pandas as pd
from scipy.stats import ttest_rel
import os

# Define file paths
file_path = r'H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2\logs\week3_pre_post.xlsx'
output_dir = r'H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2\logs'
output_file = os.path.join(output_dir, 'week3_analysis_results.txt')

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Read Excel file
df = pd.read_excel(file_path, sheet_name='Data')

# Extract relevant columns
pre_total = df['Pre-Test Total Score']
post_total = df['Post-Test Total Score']
question_cols = [f'Q{i} Pre' for i in range(1, 11)] + [f'Q{i} Post' for i in range(1, 11)]

# Calculate metrics
# 1. Average pre- and post-test scores
pre_avg = pre_total.mean()
post_avg = post_total.mean()
improvement = post_avg - pre_avg
percent_improvement = (improvement / pre_avg) * 100 if pre_avg != 0 else 0

# 2. Per-student improvement
student_improvements = post_total - pre_total
avg_student_improvement = student_improvements.mean()

# 3. Per-question averages
question_results = {}
for i in range(1, 11):
    pre_col = f'Q{i} Pre'
    post_col = f'Q{i} Post'
    pre_avg_q = df[pre_col].mean()
    post_avg_q = df[post_col].mean()
    question_results[f'Q{i}'] = {
        'Pre Avg': pre_avg_q,
        'Post Avg': post_avg_q,
        'Improvement': post_avg_q - pre_avg_q
    }

# 4. Statistical significance (paired t-test)
t_stat, p_value = ttest_rel(post_total, pre_total)

# 5. Ethics/interest questions (Q5, Q8, Q9, Q10) target check
ethics_questions = ['Q5 Post', 'Q8 Post', 'Q9 Post', 'Q10 Post']
ethics_results = {q: df[q].mean() >= 3.5 for q in ethics_questions}

# Prepare output text
output_text = [
    "Week 3 Pre-Post Test Analysis Results",
    "=====================================",
    f"Number of Students: {len(df)}",
    "",
    "Total Score Analysis:",
    f"  Pre-Test Average Score: {pre_avg:.2f} (Baseline: <30)",
    f"  Post-Test Average Score: {post_avg:.2f} (Target: >=36)",
    f"  Average Improvement: {improvement:.2f} points",
    f"  Percentage Improvement: {percent_improvement:.2f}% (Target: >=20%)",
    f"  Average Per-Student Improvement: {avg_student_improvement:.2f} points",
    "",
    "Statistical Significance (Paired T-Test):",
    f"  T-Statistic: {t_stat:.2f}",
    f"  P-Value: {p_value:.4f} (Significant if p < 0.05)",
    "",
    "Per-Question Analysis:",
]
for q, results in question_results.items():
    output_text.append(f"  {q}:")
    output_text.append(f"    Pre-Test Avg: {results['Pre Avg']:.2f}")
    output_text.append(f"    Post-Test Avg: {results['Post Avg']:.2f}")
    output_text.append(f"    Improvement: {results['Improvement']:.2f}")
output_text.append("")
output_text.append("Ethics/Interest Questions (Target: Post-Test Avg >= 3.5):")
for q, met_target in ethics_results.items():
    avg_score = df[q].mean()
    status = "Met" if met_target else "Not Met"
    output_text.append(f"  {q}: {avg_score:.2f} ({status})")
output_text.append("")
output_text.append(f"Results saved to: {output_file}")

# Save results to text file
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_text))

print(f"Analysis complete. Results saved to {output_file}")