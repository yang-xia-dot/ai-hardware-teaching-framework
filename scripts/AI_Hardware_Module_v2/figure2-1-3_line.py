import matplotlib.pyplot as plt
import numpy as np
import os

# Data for the line chart
stages = ['Input', 'no_grad', 'CLT', 'Output']
values = [100, 50, 30, 10]

# Positions for x-axis
x = np.arange(len(stages))

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))  # Professional size suitable for top-tier journals

# Plot the line with markers
ax.plot(x, values, marker='o', linewidth=2.5, markersize=8, color='#9966FF', markerfacecolor='#9966FF', markeredgecolor='white', markeredgewidth=1.5)

# Customize the plot for a clean, publication-ready appearance
ax.set_xlabel('Optimization Stages', fontsize=12, fontweight='bold')
ax.set_ylabel('Resource Utilization (%)', fontsize=12, fontweight='bold')
ax.set_title('Low-Resource Optimization Framework', fontsize=14, fontweight='bold', pad=20)

# Set x-ticks to stage labels
ax.set_xticks(x)
ax.set_xticklabels(stages, fontsize=11)

# Set y-limits
ax.set_ylim(0, 100)

# Add grid for readability
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)

# Improve aesthetics: remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_linewidth(1.2)

# Add value labels on markers
for i, (stage, val) in enumerate(zip(stages, values)):
    ax.annotate(f'{val}%', (x[i], val), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, fontweight='bold')

# Tight layout for optimal spacing
plt.tight_layout()

# Specify the save path
save_path = r'H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2\demos'

# Create directory if it doesn't exist
os.makedirs(save_path, exist_ok=True)

# Save the figure in high resolution
plt.savefig(os.path.join(save_path, 'figure2-1-3_line.png'), dpi=300, bbox_inches='tight', facecolor='white')
plt.show()  # Optional: display if running interactively