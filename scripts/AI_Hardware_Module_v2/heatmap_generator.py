import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import os

# 设置主目录路径
base_dir = Path(r'H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2')
logs_dir = base_dir / 'logs'
demos_dir = base_dir / 'demos'

# 确保目录存在
os.makedirs(demos_dir, exist_ok=True)

# 读取协作数据文件 (假设文件已存在，列为Week_1到Week_8，行索引为学生ID)
file_path = logs_dir / 'your_collaboration_data.xlsx'
try:
    df = pd.read_excel(file_path, index_col=0)  # index_col=0假设第一列是学生ID
    print(f'已读取文件 {file_path}')
except FileNotFoundError:
    print(f'错误：文件 {file_path} 不存在。请确保文件已准备好。')
    exit(1)

# 假设df列名为 'Week_1' 到 'Week_8'，如果是中文 '周1' 等，调整columns
df.columns = [f'周{j}' for j in range(1, len(df.columns) + 1)]  # 标准化为中文周

# 生成总协作热图 (中文版)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(df, annot=True, fmt='.2f', cmap='YlGnBu', ax=ax)
ax.set_title('总协作热图 (25学生 × 8周)')
ax.set_xlabel('周次')
ax.set_ylabel('学生ID')
plt.savefig(demos_dir / 'total_heatmap_cn.png')
plt.close()
print(f'中文总热图保存到 {demos_dir / "total_heatmap_cn.png"}')

# 生成总协作热图 (英文版)
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
df.columns = [f'Week {j}' for j in range(1, len(df.columns) + 1)]
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(df, annot=True, fmt='.2f', cmap='YlGnBu', ax=ax)
ax.set_title('Total Collaboration Heatmap (25 Students × 8 Weeks)')
ax.set_xlabel('Week')
ax.set_ylabel('Student ID')
plt.savefig(demos_dir / 'total_heatmap_en.png')
plt.close()
print(f'英文总热图保存到 {demos_dir / "total_heatmap_en.png"}')

# 计算分级热图 (假设Excel有'Level'列；如果没有，添加Level列或手动调整)
# 示例：如果没有Level，模拟添加 (随机分配Basic/Intermediate/Advanced)
if 'Level' not in df.columns:
    levels = np.random.choice(['Basic', 'Intermediate', 'Advanced'], size=len(df))
    df['Level'] = levels
    print('警告：文件中无Level列，已模拟添加。')

# Group by Level计算平均
level_df = df.groupby('Level').mean()
level_df.columns = [f'周{j}' for j in range(1, len(level_df.columns) + 1)]  # 标准化

# 生成分级协作热图 (中文版)
plt.rcParams['font.sans-serif'] = ['SimHei']
fig, ax = plt.subplots(figsize=(10, 4))
sns.heatmap(level_df, annot=True, fmt='.2f', cmap='YlGnBu', ax=ax)
ax.set_title('分级协作热图 (3级别 × 8周)')
ax.set_xlabel('周次')
ax.set_ylabel('级别')
plt.savefig(demos_dir / 'level_heatmap_cn.png')
plt.close()
print(f'中文分级热图保存到 {demos_dir / "level_heatmap_cn.png"}')

# 生成分级协作热图 (英文版)
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
level_df.columns = [f'Week {j}' for j in range(1, len(level_df.columns) + 1)]
fig, ax = plt.subplots(figsize=(10, 4))
sns.heatmap(level_df, annot=True, fmt='.2f', cmap='YlGnBu', ax=ax)
ax.set_title('Level Collaboration Heatmap (3 Levels × 8 Weeks)')
ax.set_xlabel('Week')
ax.set_ylabel('Level')
plt.savefig(demos_dir / 'level_heatmap_en.png')
plt.close()
print(f'英文分级热图保存到 {demos_dir / "level_heatmap_en.png"}')