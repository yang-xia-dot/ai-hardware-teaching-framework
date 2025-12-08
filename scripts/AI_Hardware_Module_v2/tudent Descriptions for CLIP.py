import random
import os

# 准备计算机部件列表（扩展自示例）
computer_parts = [
    "Chip", "CPU", "Memory box", "ALU", "Control unit", "Signal wire",
    "Register", "Bus", "Cache", "GPU", "RAM", "Hard drive", "Motherboard",
    "Fan", "Power supply", "Port", "Circuit board", "Transistor", "Capacitor",
    "Resistor", "Clock signal", "Instruction fetch", "Data path", "Pipeline", "Core"
]

# 准备农场/农机比喻列表（扩展自示例）
farm_items = [
    "farmland screw", "nail fixing", "workbench drawer", "farm tool calculator", "tractor steering wheel",
    "plow blade", "harvest basket", "irrigation pipe", "barn door hinge", "fence post",
    "seed drill", "hay bale tie", "milking machine valve", "chicken coop latch", "windmill gear",
    "crop row marker", "fertilizer spreader wheel", "silo grain chute", "livestock feeder trough",
    "compost bin shovel", "orchard ladder rung", "greenhouse vent", "beehive frame", "pond pump filter",
    "vine trellis wire"
]

# 随机生成25个描述，按学生ID
descriptions = []
for student_id in range(1, 26):  # Student 1 to 25
    part = random.choice(computer_parts)
    item = random.choice(farm_items)
    description = f"{part} like {item}"  # 随机组合
    descriptions.append(f"Student {student_id}: {description}")

# 打印生成的描述（模拟输出）
print("Generated 25 student descriptions:")
for desc in descriptions:
    print(desc)

# 保存到合适的位置：假设项目结构，存到 logs/student_descriptions.txt
save_path = os.path.join("H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2\logs\student_descriptions.txt")  # 相对路径，从scripts到logs
os.makedirs(os.path.dirname(save_path), exist_ok=True)  # 创建文件夹如果不存在
with open(save_path, 'w', encoding='utf-8') as f:
    f.write("Simulated Student Descriptions for CLIP Matching:\n")
    f.write('\n'.join(descriptions))
print(f"\nDescriptions saved to: {save_path}")