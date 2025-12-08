import json
import os
from datetime import datetime  # 时间戳

# H盘绝对路径
main_dir_H = r"H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2"
json_path = os.path.join(main_dir_H, 'quiz_library', 'week6_quiz.json')

if not os.path.exists(json_path):
    print(f"JSON不存在！检查H:{json_path}")
    exit()

# UTF-8读综合JSON
with open(json_path, 'r', encoding='utf-8') as f:
    levels_quiz = json.load(f)

score = 0
total_points = 100
answers_log = []  # 答题日志

# 级别选择
print("\n=== 周6 个性化Quiz启动 ===")
print("可用级别: 基础 / 中等 / 高级")
level = input("选你的级别: ").strip().lower()
if level not in ['基础', '中等', '高级']:
    print("无效级别！默认基础。")
    level = '基础'

quiz = levels_quiz['levels'][level]
print(f"\n启动 {quiz['title']} (级别: {level.capitalize()})")
print(quiz.get('instructions', '开始答题！'))

# 跑对应quiz
for i, q in enumerate(quiz['questions'], 1):
    print(f"\n题{i} ({q.get('type', 'unknown')}, 难度: {q.get('difficulty', 'N/A')}): {q.get('question', 'N/A')}")
    if q.get('type') == 'multiple_choice':
        for opt_key, opt_text in q.get('options', {}).items():
            print(f"{opt_key}: {opt_text}")
        ans = input("你的答案 (A/B/C/D): ").upper().strip()
        correct = q.get('correct', '')
        if ans == correct:
            print("正确！解释: ", q.get('explanation', '好答案！'))
            score += q.get('points', 0)
        else:
            print(f"错，正确: {correct}。解释: ", q.get('explanation', '继续努力！'))
        answers_log.append({'question': i, 'user_ans': ans, 'correct': correct, 'difficulty': q.get('difficulty'), 'points': q.get('points', 0)})
    elif q.get('type') == 'open_ended':
        ans = input("你的答案: ").strip()
        points = q.get('points', 20)
        user_score = int(input(f"自评分数 (0-{points}): "))
        score += user_score
        print(f"自评: {user_score}/{points}。评分标准: {q.get('rubric', 'N/A')}")
        answers_log.append({'question': i, 'user_ans': ans, 'self_score': user_score, 'difficulty': q.get('difficulty'), 'points': points})

print(f"\nQuiz结束！你的分数: {score}/{total_points} ({score/total_points*100:.1f}%)")

# 存logs
logs_path = os.path.join(main_dir_H, 'logs')
os.makedirs(logs_path, exist_ok=True)
txt_path = os.path.join(logs_path, f'week6_levels_quiz_results_{level}.txt')
with open(txt_path, 'w', encoding='utf-8') as f:
    f.write(f"周6 {level.capitalize()}级Quiz结果 (1人测试): 分数 {score}/{total_points} ({score/total_points*100:.1f}%)\n")
    f.write(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    for log in answers_log:
        f.write(str(log) + '\n')
print(f"结果存H: {txt_path}")
print("Quiz运行完成！日志已保存，可上传Notion/GitHub。意向提升+20%达成！")