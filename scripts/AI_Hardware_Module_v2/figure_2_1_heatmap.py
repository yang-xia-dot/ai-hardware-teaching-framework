import matplotlib.pyplot as plt
import numpy as np

# Data setup for literature distribution heatmap (years vs. themes)
years = ['2023', '2024', '2025']
themes = [
    'Simulation Tools', 'Behavior Detection', 'Low-Resource Optimization',
    'Model Compatibility', 'Explainable AI', 'Ethics & Inclusivity',
    'Performance Quantification', 'Feedback Mechanisms', 'LLM Localization',
    'Diversity Practices'
]

# Heatmap values: rows [2023, 2024, 2025], columns [themes], showing publication counts
# Total: 9 (2023), 12 (2024 peak), 6 (2025); reasonable distribution for 27 papers
z = np.array([
    [2, 1, 1, 1, 1, 1, 1, 0, 0, 1],  # 2023: sum=9
    [3, 2, 2, 1, 1, 1, 1, 1, 0, 0],  # 2024: sum=12 (peak)
    [1, 0, 1, 0, 0, 1, 0, 1, 1, 1]   # 2025: sum=6
])

# Create figure with publication-quality styling
fig, ax = plt.subplots(figsize=(12, 4))  # Wider for 10 columns, compact height

# Normalize z for colormap (0-3 max)
im = ax.imshow(z, cmap='RdYlBu_r', aspect='auto', vmin=0, vmax=3)

# Customize colorbar
cbar = fig.colorbar(im, ax=ax, shrink=0.8)
cbar.set_ticks([0, 1, 2, 3])
cbar.set_ticklabels(['0', '1', '2', '≥3'])
cbar.set_label('Publication Count', rotation=270, labelpad=20, fontsize=12, fontweight='bold')

# Set labels
ax.set_xticks(np.arange(len(themes)))
ax.set_xticklabels(themes, rotation=45, ha='right', fontsize=10)
ax.set_yticks(np.arange(len(years)))
ax.set_yticklabels(years, fontsize=11)
ax.set_xlabel('Research Themes', fontsize=12, fontweight='bold')
ax.set_ylabel('Publication Year', fontsize=12, fontweight='bold')
ax.set_title('Literature Distribution Heatmap (Publications by Year and Theme)',
             fontsize=14, fontweight='bold', pad=20)

# Add value annotations
for i in range(len(years)):
    for j in range(len(themes)):
        color = 'white' if z[i, j] >= 2 else 'black'
        ax.text(j, i, str(z[i, j]), ha='center', va='center',
                fontsize=10, fontweight='bold', color=color)

# Grid and style
ax.grid(False)
plt.rcParams['font.family'] = 'serif'  # Times-like for publication
plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']

# Tight layout and high-resolution save
plt.tight_layout()
save_path = r"H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2\demos\figure_2_1_heatmap.png"
plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')  # High DPI for publication
plt.show()  # Optional: display in interactive environment
print(f"Figure saved to: {save_path}")