import numpy as np
import matplotlib.pyplot as plt
import os

# 设置路径（H盘主目录）
base_path = r'H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2'
demos_dir = os.path.join(base_path, 'demos')
os.makedirs(demos_dir, exist_ok=True)

# 手动重建热图数据（基于你的图片颜色梯度，值从0.1低到0.9高）
# 行0-4: 组索引；列0-4: ID
heatmap_data = np.array([
    [0.15, 0.45, 0.85, 0.05, 0.75],  # 行0: 浅黄-黄-红-黑-红
    [0.75, 0.55, 0.65, 0.95, 0.65],  # 行1: 红-黄-黄-白-橙
    [0.05, 0.55, 0.45, 0.55, 0.25],  # 行2: 黑-黄-黄-橙-黄
    [0.45, 0.45, 0.75, 0.05, 0.05],  # 行3: 橙-橙-橙-黑-黑
    [0.05, 0.45, 0.85, 0.45, 0.95]   # 行4: 黑-黄-红-橙-白
])

# 生成热图（英文标题/标签，确保文字清晰）
plt.figure(figsize=(8, 6))
plt.rcParams['font.family'] = ['Arial', 'sans-serif']  # 字体fallback，避免glyph问题
im = plt.imshow(heatmap_data, cmap='hot', vmin=0.1, vmax=0.9, aspect='equal')
plt.title('ViT(III) Collaboration Heatmap [Penchala 97.58% Accuracy, >=80%]')
plt.xlabel('ID')
plt.ylabel('Group')
plt.xticks(range(5), ['0', '1', '2', '3', '4'])
plt.yticks(range(5), ['0', '1', '2', '3', '4'])
cbar = plt.colorbar(im, label='Intensity')
cbar.set_ticks([0.1, 0.3, 0.5, 0.7, 0.9])
plt.tight_layout()

# 保存到demos
plt.savefig(os.path.join(demos_dir, 'vit_collaboration_heatmap.png'), dpi=300, bbox_inches='tight')
plt.close()

print("Heatmap recreated and saved to H:\...v2\demos\vit_collaboration_heatmap.png with clear English text.")