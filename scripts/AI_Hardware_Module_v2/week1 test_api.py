import requests
import os
import re

print("当前目录: ", os.getcwd())  # D:\...v2

# D: config读（你D:有config？指南H:，但D:临时OK；后改H:）
config_path_D = 'config/api_keys.txt'  # D:相对
# 或H:绝对（优先H:正式）
main_dir_H = r"H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2"
config_path_H = os.path.join(main_dir_H, 'config', 'api_keys.txt')

config_path = config_path_H if os.path.exists(config_path_H) else config_path_D
print(f"读config: {config_path} (H优先)")

api_key = None
api_url = None
model = None

if os.path.exists(config_path):
    with open(config_path, 'r', encoding='utf-8') as f:
        content = f.read()
    print("api_keys.txt全内容: ", repr(content))  # 调试：看=空格/乱码（repr秀转义）

    # 宽正则：+匹配任意长sk-/xai-
    deepseek_match = re.search(r'sk-[a-zA-Z0-9]+', content)
    grok_match = re.search(r'xai-[a-zA-Z0-9]+', content)

    if deepseek_match:
        api_key = deepseek_match.group(0)
        api_url = 'https://api.deepseek.com/v1/chat/completions'
        model = 'deepseek-chat'
        print(f"优先DeepSeek: {api_key[:10]}...")
    elif grok_match:
        api_key = grok_match.group(0)
        api_url = 'https://api.x.ai/v1/chat/completions'
        model = 'grok-4-latest'
        print(f"用Grok: {api_key[:10]}...")
    else:
        print("密钥未匹配！规整api_keys.txt（sk-/xai-无=后缀）。")
        exit()
else:
    print(f"config不存在！D:或H:建config，放规整文件。")
    exit()

print(f"API: {model} @ {api_url}")

# 测试
prompt = "Testing. Just say hi and hello world and nothing else."
try:
    response = requests.post(api_url,
                             json={'model': model, 'messages': [{'role': 'user', 'content': prompt}], 'max_tokens': 10,
                                   'temperature': 0},
                             headers={'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'},
                             timeout=20)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        result = response.json()['choices'][0]['message']['content']
        print("成功！AI回: ", result.strip())
    else:
        print("失败详情: ", response.text[:500])
except Exception as e:
    print("异常（网/超时）: ", str(e))