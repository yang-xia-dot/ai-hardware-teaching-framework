# Chinese version - Combined 2D Plots using Matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Set font to support Chinese characters
plt.rcParams['font.sans-serif'] = ['SimHei']  # Use SimHei for Chinese support
plt.rcParams['axes.unicode_minus'] = False   # Handle minus signs

# Data for Heatmap
years = ['2023', '2024', '2025']
themes = [
    '模拟工具',
    '行为检测',
    '低资源优化',
    '模型兼容性',
    '可解释AI',
    '伦理与包容性',
    '性能量化',
    '反馈机制',
    'LLM本地化',
    '多样性实践'
]

data = np.array([
    [2, 1, 1, 1, 1, 1, 1, 0, 0, 1],  # 2023
    [3, 2, 2, 1, 1, 1, 1, 1, 0, 0],  # 2024
    [1, 0, 1, 0, 0, 1, 0, 1, 1, 1]   # 2025
]).T  # Transpose for themes as rows, years as columns

# Data for Line Chart
stages = [
    '问题识别',
    '基础设施评估',
    '工具集成',
    'VT优化',
    '本地化适应',
    'SEM验证',
    '风险管理',
    '输出创新'
]

low_resource = [0, 5, 20, 35, 50, 65, 80, 95]  # Cyan line
urban = [0, 10, 25, 40, 55, 70, 85, 100]       # Pink line

# Create figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Heatmap on left
sns.heatmap(data, annot=True, fmt='d', cmap='RdBu', ax=ax1,
            xticklabels=years, yticklabels=themes)
ax1.set_title('文献分布热力图')
ax1.set_xlabel('年份')
ax1.set_ylabel('研究主题')

# Line chart on right
ax2.plot(stages, low_resource, color='cyan', marker='o', label='低资源路径')
ax2.plot(stages, urban, color='pink', marker='o', label='城市比较路径')
ax2.set_title('系统路径概述')
ax2.set_xlabel('过程阶段')
ax2.set_ylabel('进度 (%)')
ax2.set_ylim(0, 100)
ax2.tick_params(axis='x', rotation=45)
ax2.legend()
ax2.grid(True)

plt.tight_layout()

# Save the figure
output_path = r'H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2\demos\literature_and_pathway_2d_chinese.png'
plt.savefig(output_path, dpi=300)

print(f'Figure saved to {output_path}')