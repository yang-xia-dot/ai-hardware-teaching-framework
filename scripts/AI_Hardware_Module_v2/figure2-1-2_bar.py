import matplotlib.pyplot as plt
import numpy as np
import os

# Data for the bar chart
metrics = ['Memory (GB)', 'Delay (s)', 'Accuracy (%)']
vit_values = [4, 10, 95]
mobilevit_values = [2, 5, 97.58]

# Set positions for side-by-side bars
x = np.arange(len(metrics))
width = 0.35  # Width of the bars

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))  # Professional size suitable for top-tier journals

# Plot bars
bars1 = ax.bar(x - width/2, vit_values, width, label='ViT', color='#1f77b4', alpha=0.8, edgecolor='white', linewidth=1.2)
bars2 = ax.bar(x + width/2, mobilevit_values, width, label='MobileViT', color='#2ca02c', alpha=0.8, edgecolor='white', linewidth=1.2)

# Customize the plot for a clean, publication-ready appearance
ax.set_xlabel('Metrics', fontsize=12, fontweight='bold')
ax.set_ylabel('Values', fontsize=12, fontweight='bold')
ax.set_title('Performance Comparison of ViT and MobileViT', fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(metrics, fontsize=11)

# Add value labels on top of bars
for bar in bars1:
    height = bar.get_height()
    ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10, fontweight='bold')
for bar in bars2:
    height = bar.get_height()
    ax.annotate(f'{height}', xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10, fontweight='bold')

# Add legend
ax.legend(loc='upper right', fontsize=11)

# Add grid for readability
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.8, axis='y')

# Improve aesthetics: remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_linewidth(1.2)

# Tight layout for optimal spacing
plt.tight_layout()

# Specify the save path
save_path = r'H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2\demos'

# Create directory if it doesn't exist
os.makedirs(save_path, exist_ok=True)

# Save the figure in high resolution
plt.savefig(os.path.join(save_path, 'figure2-1-2_bar.png'), dpi=300, bbox_inches='tight', facecolor='white')
plt.show()  # Optional: display if running interactively