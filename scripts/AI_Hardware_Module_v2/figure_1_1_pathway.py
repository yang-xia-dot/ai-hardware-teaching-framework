import matplotlib.pyplot as plt
import numpy as np

# Data setup
labels = ["Problem Identification", "Infrastructure Assessment", "Tool Integration",
          "ViT Optimization", "Localization Adaptation", "SEM Validation",
          "Risk Management", "Output Innovation"]
x = np.arange(len(labels))  # X positions for the 8 points
low_resource_data = [0, 15, 30, 50, 65, 80, 90, 100]
urban_data = [0, 20, 40, 60, 70, 85, 95, 100]
error = [5] * len(low_resource_data)  # ±5% error bars for both pathways to indicate urban-rural variability
plt.rcParams['font.family'] = 'serif'
# Create figure and axis with professional styling for top-tier publication
fig, ax = plt.subplots(figsize=(10, 4))  # Width for 8 labels, height ~300px at 100 dpi (4 inches * 75 dpi ≈ 300px)
ax.set_xlim(-0.5, len(labels) - 0.5)
ax.set_ylim(0, 100)

# Plot lines with error bars - Fixed colors to hex format for matplotlib compatibility
line1 = ax.errorbar(x, low_resource_data, yerr=error, fmt='-o', linewidth=2, markersize=6,
                    capsize=5, capthick=2, label='Low-Resource Pathway',
                    color='#4BC0C0', markerfacecolor='#4BC0C0',
                    markeredgecolor='white', markeredgewidth=1)
line2 = ax.errorbar(x, urban_data, yerr=error, fmt='-s', linewidth=2, markersize=6,
                    capsize=5, capthick=2, label='Urban Comparison Pathway',
                    color='#FF6384', markerfacecolor='#FF6384',
                    markeredgecolor='white', markeredgewidth=1)

# Customize axes and labels for publication quality
ax.set_xlabel('Process Stages', fontsize=12, fontweight='bold')
ax.set_ylabel('Progress (%)', fontsize=12, fontweight='bold')
ax.set_title('System Pathway Overview (Low-Resource vs. Urban Pathway)', fontsize=14, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(labels, rotation=45, ha='right', fontsize=10)
ax.set_yticks(np.arange(0, 101, 20))
ax.grid(True, linestyle='--', alpha=0.7, axis='y')  # Light grid for readability
ax.legend(loc='lower right', frameon=True, fancybox=True, shadow=True)

# Tight layout and high-resolution save
plt.tight_layout()
save_path = r"H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2\demos\figure_1_1_pathway.png"
plt.savefig(save_path, dpi=300, bbox_inches='tight', facecolor='white')  # High DPI for publication
plt.show()  # Optional: display in interactive environment
print(f"Figure saved to: {save_path}")