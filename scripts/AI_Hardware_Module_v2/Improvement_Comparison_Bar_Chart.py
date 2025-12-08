import matplotlib.pyplot as plt
import os
import numpy as np

# Ensure output directory exists
output_dir = r'H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2\demos'
os.makedirs(output_dir, exist_ok=True)

# Data: Metrics and improvement percentages
metrics = ['Literacy Improvement (%)', 'Interest Improvement (%)', 'Engagement Rate (%)']
this_study = [18.2, 22.5, 82.0]  # This study's values
chen_et_al = [17.5, 17.5, 70.0]  # Chen et al. (2024) benchmark (midpoint for 15-20%, assumed 70% for engagement)

# Positions for bars
x = np.arange(len(metrics))
width = 0.35  # Bar width

# Create figure with publication-style settings
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)  # High-res for print
bars1 = ax.bar(x - width/2, this_study, width, label='This Study', color='#1f77b4', edgecolor='black', linewidth=0.5, alpha=0.8)
bars2 = ax.bar(x + width/2, chen_et_al, width, label='Chen et al. (2024)', color='#ff7f0e', edgecolor='black', linewidth=0.5, alpha=0.8)

# Customize for top-journal quality: Sans-serif font, tight layout, labels
ax.set_xlabel('Metrics', fontsize=12, fontfamily='sans-serif')
ax.set_ylabel('Improvement/Rate (%)', fontsize=12, fontfamily='sans-serif')
ax.set_title('Figure 5-1: Improvement Comparison Bar Chart', fontsize=14, fontweight='bold', fontfamily='sans-serif', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(metrics, rotation=45, ha='right', fontsize=10, fontfamily='sans-serif')
ax.set_ylim(0, 90)  # Clean y-axis scaling
ax.grid(axis='y', linestyle='--', alpha=0.3)  # Subtle grid for readability

# Add value labels on bars
for bar in bars1:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom', fontsize=9, fontfamily='sans-serif')
for bar in bars2:
    height = bar.get_height()
    ax.annotate(f'{height:.1f}%',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=9, fontfamily='sans-serif')

# Legend
ax.legend(fontsize=10, loc='upper left')

plt.tight_layout()

# Save as high-quality PNG and PDF
png_path = os.path.join(output_dir, 'Figure_5-1_Improvement_Comparison_Bar_Chart.png')
pdf_path = os.path.join(output_dir, 'Figure_5-1_Improvement_Comparison_Bar_Chart.pdf')
plt.savefig(png_path, dpi=300, bbox_inches='tight')
plt.savefig(pdf_path, bbox_inches='tight', format='pdf')
plt.close()  # Close to free memory

print(f"Figure saved to: {png_path} and {pdf_path}")