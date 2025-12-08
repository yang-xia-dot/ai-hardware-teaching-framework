import requests
import json
import os
from datetime import datetime

# 绝对路径
main_dir_H = r"H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2"
config_path = os.path.join(main_dir_H, 'config', 'api_keys.txt')
logs_path = os.path.join(main_dir_H, 'logs')
os.makedirs(logs_path, exist_ok=True)

# 读API密钥
with open(config_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
grok_key = next((line.split('=')[1].strip() for line in lines if line.startswith('grok_api_key')), None)
if not grok_key:
    print("未找到grok_api_key！检查config/api_keys.txt。")
    exit()

# Grok API端点
url = "https://api.x.ai/v1/chat/completions"  # Grok 4
headers = {
    "Authorization": f"Bearer {grok_key}",
    "Content-Type": "application/json"
}


def generate_level_quiz(level):
    # 级别prompt (自适应生成5题JSON)
    prompts = {
        "基础": "生成高中弱生基础农场路径quiz: 5题 (3选择+2开放), 简单安装+2G缓存, 无Transformer复杂. JSON格式: title, instructions, questions (id/type/question/options/correct/points/explanation/rubric). 总100分, 易用语言.",
        "中等": "生成高中中等生中等农场路径quiz: 5题 (3选择+2开放), 加Transformer故事+湿度检测, 意向+20%. JSON格式: title, instructions, questions. 总100分, 趣味故事.",
        "高级": "生成高中强生高级农场路径quiz: 5题 (3选择+2开放), 优化挑战+伦理辩论+SEM模拟, CFA觉醒. JSON格式: title, instructions, questions. 总100分, 深度思考."
    }
    prompt = prompts.get(level, prompts["基础"])
    data = {
        "model": "grok-4",  # 或grok-beta
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 500,
        "temperature": 0.7  # 创意平衡
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        content = response.json()['choices'][0]['message']['content']
        # 尝试解析JSON (API返回JSON字符串)
        try:
            quiz_json = json.loads(content)
            return quiz_json
        except json.JSONDecodeError:
            return {"error": "API返回非JSON", "raw": content}
    else:
        return {"error": f"API错误 {response.status_code}", "raw": response.text}


# 运行
if __name__ == "__main__":
    level = input("你的水平 (基础/中等/高级): ").strip().lower()
    quiz = generate_level_quiz(level.capitalize())

    print(f"\n=== {level.capitalize()}级Quiz生成完成！ ===")
    print(json.dumps(quiz, indent=2, ensure_ascii=False))

    # 保存logs
    output_path = os.path.join(logs_path, f'week6_generated_quiz_{level}.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(quiz, f, indent=2, ensure_ascii=False)
    print(f"保存: {output_path} (时间: {datetime.now().strftime('%H:%M:%S')})")
    print("运行OK！课上分享你的路径，意向+20%达成。")