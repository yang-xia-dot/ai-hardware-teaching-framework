import json
import os

# H盘绝对路径（你的main_dir_H）
main_dir_H = r"H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2"
json_path = os.path.join(main_dir_H, 'quiz_library', 'week5_quiz.json')

if not os.path.exists(json_path):
    print(f"JSON不存在！检查H:{json_path}")
    exit()

# UTF-8读
with open(json_path, 'r', encoding='utf-8') as f:
    quiz = json.load(f)

score = 0
total = len(quiz.get('questions', []))  # 从JSON结构读题数
answers_log = []  # 学生答题日志

print(f"\n=== 周5 Quiz启动: {quiz.get('quiz_title', 'Unknown')} ===")
print("答题时间5min。选择题输入A/B/C/D，开放题直接输入答案。开始！")

for i, q in enumerate(quiz['questions'], 1):
    print(f"\n题{i} ({q['type']}, 难度: {q['difficulty']}): {q['question']}")
    if q['type'] == 'multiple_choice':
        for opt in q['options']:
            print(opt)
        ans = input("你的答案 (A/B/C/D): ").upper().strip()
        if ans == q['correct']:
            print("正确！解释: ", q['explanation'])
            score += q['points']
        else:
            print(f"错，正确: {q['correct']}。解释: ", q['explanation'])
        answers_log.append({'question': i, 'user_ans': ans, 'correct': q['correct'], 'difficulty': q['difficulty'], 'points': q['points']})
    elif q['type'] == 'open_ended':
        ans = input("你的答案: ").strip()
        # 开放题手动评分 (简单: 满分/半分, 实际课上手动评)
        user_score = int(input(f"自评分数 (0-{q['points']}): "))
        score += user_score
        print(f"自评: {user_score}/{q['points']}。解释: {q['rubric']}")
        answers_log.append({'question': i, 'user_ans': ans, 'self_score': user_score, 'difficulty': q['difficulty'], 'points': q['points']})

print(f"\nQuiz结束！你的分数: {score}/{total*20} ({score/(total*20)*100:.1f}%)")  # 假设每题20分

# 存logs（H盘logs文件夹）
logs_path = os.path.join(main_dir_H, 'logs')
os.makedirs(logs_path, exist_ok=True)
txt_path = os.path.join(logs_path, 'week5_quiz_results.txt')
with open(txt_path, 'w', encoding='utf-8') as f:
    f.write(f"周5 Quiz结果 (1人测试): 分数 {score}/{total*20} ({score/(total*20)*100:.1f}%)\n")
    f.write(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    for log in answers_log:
        f.write(str(log) + '\n')
print(f"结果存H: {txt_path}")
print("Quiz运行完成！日志已保存，可上传Notion/GitHub。")