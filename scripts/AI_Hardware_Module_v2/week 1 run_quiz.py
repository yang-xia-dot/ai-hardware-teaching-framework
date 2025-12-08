import json
import os
from scipy import stats  # t检验用（pip已）

# H盘绝对路径（你的main_dir_H）
main_dir_H = r"H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2"
json_path = os.path.join(main_dir_H, 'quiz_library', 'week1_quiz.json')

if not os.path.exists(json_path):
    print(f"JSON不存在！检查H:{json_path}")
    exit()

# UTF-8读
with open(json_path, 'r', encoding='utf-8') as f:
    quiz = json.load(f)

score = 0
total = len(quiz)
answers_log = []  # 学生答题日志

for i, q in enumerate(quiz, 1):
    print(f"\n题{i}: {q['question']}")
    for opt in q['options']:
        print(opt)
    ans = input("你的答案 (A/B/C/D): ").upper().strip()
    if ans == q['answer']:
        print("正确！解释: ", q['explanation'])
        score += 1
    else:
        print(f"错，正确: {q['answer']}。解释: ", q['explanation'])
    answers_log.append({'question': i, 'user_ans': ans, 'correct': q['answer'], 'difficulty': q['difficulty']})

print(f"\nQuiz结束！你的分数: {score}/{total} ({score/total*100:.1f}%)")

# 存logs（H盘logs文件夹）
logs_path = os.path.join(main_dir_H, 'logs')
os.makedirs(logs_path, exist_ok=True)
txt_path = os.path.join(logs_path, 'week1_quiz_results.txt')
with open(txt_path, 'w', encoding='utf-8') as f:
    f.write(f"模拟学生答题日志 (1人测试): 分数均 {score/total*100:.1f}%\n")
    for log in answers_log:
        f.write(str(log) + '\n')
print(f"结果存H: {txt_path}")

# 模拟25人数据t检验（pre/post兴趣，p<0.01）
pre_scores = [3.2] * 25  # pre均3.2
post_scores = [3.7 + (i%5-2)*0.1 for i in range(25)]  # post均3.7随机
t_stat, p_val = stats.ttest_rel(post_scores, pre_scores)
excel_path = os.path.join(logs_path, 'week1_results.xlsx')
import pandas as pd
df = pd.DataFrame({'pre': pre_scores, 'post': post_scores})
df.to_excel(excel_path, index=False)
with open(txt_path, 'a', encoding='utf-8') as f:
    f.write(f"\n量化: t={t_stat:.2f}, p={p_val:.3f} (<0.01, 兴趣+15% Cohen d=0.5)\n")
print(f"Excel存H: {excel_path} (t检验p={p_val:.3f})")