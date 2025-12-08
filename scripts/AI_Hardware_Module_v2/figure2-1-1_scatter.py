
import matplotlib.pyplot as plt
import numpy as np
import os

# Data for the scatter plot: Representing integration steps (y: 0-4 steps) vs. progress metrics (x: 0-80)
# Simulated points for tool integration flow: e.g., QEMU (low memory, high compatibility) at step 0-1, Logisim at 1-2, etc.
steps = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4]  # Y-axis: Integration steps (0-4)
progress = [0, 20, 40, 20, 60, 40, 80, 60, 80]  # X-axis: Progress percentages (0,20,40,60,80 range)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))  # Professional size suitable for top-tier journals

# Scatter plot with specified color (RGB 255,99,132 -> #FF6384)
scatter = ax.scatter(progress, steps, c='#FF6384', s=120, alpha=0.8, edgecolors='white', linewidth=1.5, zorder=3)

# Add trend line for flow visualization (optional, to mimic process flow)
z = np.polyfit(progress, steps, 1)
p = np.poly1d(z)
ax.plot(progress, p(progress), "--", color='#FF6384', alpha=0.6, linewidth=2, zorder=2)

# Customize the plot for a clean, publication-ready appearance
ax.set_xlabel('Integration Progress (%)', fontsize=12, fontweight='bold')
ax.set_ylabel('Integration Steps (0-4)', fontsize=12, fontweight='bold')
ax.set_title('AI Simulation Tool Integration Flow', fontsize=14, fontweight='bold', pad=20)

# Set x-ticks to specified values
ax.set_xticks([0, 20, 40, 60, 80])
ax.set_xticklabels([0, 20, 40, 60, 80], fontsize=11)

# Set y-ticks for steps
ax.set_yticks([0, 1, 2, 3, 4])
ax.set_yticklabels(['Step 0: Init', 'Step 1: Simulate', 'Step 2: Optimize', 'Step 3: Integrate', 'Step 4: Validate'], fontsize=10)

# Add grid for readability
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)

# Improve aesthetics: remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_linewidth(1.2)

# Add annotations for key points (e.g., tool examples)
ax.annotate('QEMU Init', (0, 0), xytext=(5, 0.2), textcoords='offset points', fontsize=9, ha='left', arrowprops=dict(arrowstyle='->', color='#FF6384', lw=1))
ax.annotate('Logisim Sim', (40, 1.5), xytext=(-10, 0), textcoords='offset points', fontsize=9, ha='right', arrowprops=dict(arrowstyle='->', color='#FF6384', lw=1))
ax.annotate('FT-Transformer Opt', (60, 3), xytext=(5, -0.3), textcoords='offset points', fontsize=9, ha='left', arrowprops=dict(arrowstyle='->', color='#FF6384', lw=1))

# Tight layout for optimal spacing
plt.tight_layout()

# Create demo directory if it doesn't exist
os.makedirs('demo', exist_ok=True)

# Save the figure in high resolution
plt.savefig(r'H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2\demos\figure2-1-1_scatter.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()  # Optional: display if running interactively
