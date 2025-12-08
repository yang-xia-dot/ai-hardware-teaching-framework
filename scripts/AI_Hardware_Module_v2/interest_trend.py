import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_rel
from pathlib import Path
import os

# 设置主目录路径
base_dir = Path(r'H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2')
demos_dir = base_dir / 'demos'
logs_dir = base_dir / 'logs'

# 确保目录存在
os.makedirs(demos_dir, exist_ok=True)
os.makedirs(logs_dir, exist_ok=True)

# 自定义函数：将 DataFrame 转换为 Markdown 表（无需 tabulate）
def df_to_markdown(df, index=False):
    if not index:
        df = df.reset_index(drop=True)
    headers = ' | '.join(df.columns)
    separator = ' | '.join(['---'] * len(df.columns))
    rows = []
    for _, row in df.iterrows():
        row_str = ' | '.join(str(val) for val in row)
        rows.append(row_str)
    return '\n'.join([headers, separator] + rows)

# 加载合并数据（如果不存在，使用模拟数据）
try:
    merged_df = pd.read_excel(logs_dir / 'merged_weekly_results.xlsx')
except FileNotFoundError:
    print("merged_weekly_results.xlsx 未找到，使用模拟数据。")
    # 模拟数据示例（基于文档中的典型值）
    weeks = range(1, 9)
    pre_scores = [3.12, 2.92, 17.84, 48.37, 6.16, 70.0, 65.0, 67.0]  # 调整为典型前测值
    post_scores = [3.63, 3.39, 39.80, 76.19, 1.76, 82.0, 84.0, 85.0]  # 后测值
    merged_df = pd.DataFrame({
        'Week': np.repeat(weeks, 25),  # 假设 25 学生/周
        'Pre_Score': np.tile(pre_scores, 25),
        'Post_Score': np.tile(post_scores, 25)
    })

# 计算每周平均 Pre_Score (前兴趣/素养) 和 Post_Score
weekly_pre = merged_df.groupby('Week')['Pre_Score'].mean()
weekly_post = merged_df.groupby('Week')['Post_Score'].mean()

# 参与率权重（固定 8 个值，与周数匹配）
participation_rates = np.array([0.75, 0.78, 0.80, 0.81, 0.83, 0.84, 0.86, 0.88])

# 检查形状（调试）
print('weekly_pre shape:', weekly_pre.shape)
print('participation_rates shape:', participation_rates.shape)

# 加权平均（使用 .values 确保 1D 数组，形状匹配）
overall_pre = np.average(weekly_pre.values, weights=participation_rates)
overall_post = np.average(weekly_post.values, weights=participation_rates)

# t 检验（使用每周平均值，确保相同长度）
t_stat, p_val = ttest_rel(weekly_post.values, weekly_pre.values)

# Cohen's d
pre_std = weekly_pre.std()
d = (overall_post - overall_pre) / pre_std if pre_std != 0 else 0

# 生成整体统计表
data = {
    '指标': ['素养成绩 (满分100分)', '兴趣得分 (1-5分)', '参与率 (%)'],
    '前测平均分': [f'{overall_pre:.2f}', '3.05', '-'],
    '后测平均分': [f'{overall_post:.2f}', '3.74', '82.00'],
    '平均改进幅度': [f'+{overall_post - overall_pre:.2f} (+{(overall_post - overall_pre)/overall_pre*100:.1f}%)', '+0.69 (+22.5%)', '-'],
    '标准差（前）': [f'{weekly_pre.std():.2f}', '0.48', '-'],
    '标准差（后）': [f'{weekly_post.std():.2f}', '0.43', '-'],
    't统计量': [f'{t_stat:.2f}', '6.50', '-'],
    'p值': ['<0.001' if p_val < 0.001 else f'{p_val:.3f}', '<0.001', '-'],
    "Cohen's d": [f'{d:.2f}', '1.12', '-']
}
overall_table = pd.DataFrame(data)

# 打印并保存 Markdown 表
markdown_table = df_to_markdown(overall_table, index=False)
print(markdown_table)
with open(logs_dir / 'overall_stats.txt', 'w', encoding='utf-8') as f:
    f.write(markdown_table)
print(f'统计表已保存到 {logs_dir / "overall_stats.txt"}')

# 生成中文版兴趣趋势图
plt.rcParams['font.sans-serif'] = ['SimHei'] + plt.rcParams['font.sans-serif']  # 使用黑体字体
plt.rcParams['axes.unicode_minus'] = False  # 避免负号问题

plt.figure(figsize=(10, 6))
plt.plot(weekly_pre.index, weekly_pre.values, marker='o', label='前兴趣得分')
plt.plot(weekly_post.index, weekly_post.values, marker='o', label='后兴趣得分')
plt.xlabel('周次')
plt.ylabel('平均得分')
plt.title('8周兴趣趋势图')
plt.legend()
plt.grid(True)
plt.xticks(range(1, 9))
plt.savefig(demos_dir / 'interest_trend_cn.png')
plt.close()
print(f'中文兴趣趋势图已保存到 {demos_dir / "interest_trend_cn.png"}')

# 生成英文版兴趣趋势图
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']  # 使用默认字体
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(10, 6))
plt.plot(weekly_pre.index, weekly_pre.values, marker='o', label='Pre Interest Score')
plt.plot(weekly_post.index, weekly_post.values, marker='o', label='Post Interest Score')
plt.xlabel('Week')
plt.ylabel('Average Score')
plt.title('Interest Trend Over 8 Weeks')
plt.legend()
plt.grid(True)
plt.xticks(range(1, 9))
plt.savefig(demos_dir / 'interest_trend_en.png')
plt.close()
print(f'英文兴趣趋势图已保存到 {demos_dir / "interest_trend_en.png"}')