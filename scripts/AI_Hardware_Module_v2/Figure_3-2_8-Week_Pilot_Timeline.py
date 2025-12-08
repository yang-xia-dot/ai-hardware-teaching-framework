import matplotlib.pyplot as plt
import os

# Ensure output directory exists
output_dir = r'H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2\demos'
os.makedirs(output_dir, exist_ok=True)

# Data: Weeks and activity durations (in minutes)
weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 'Week 7', 'Week 8']
activities = [10, 15, 20, 25, 20, 15, 10, 5]

# Color scheme: Blue (intro), Green (practice), Orange (assessment), Red (reflection)
colors = ['#1f77b4', '#2ca02c', '#ff7f0e', '#d62728', '#2ca02c', '#1f77b4', '#ff7f0e', '#d62728']

# Create figure with publication-style settings
fig, ax = plt.subplots(figsize=(10, 6), dpi=300)  # High-res for print
bars = ax.bar(weeks, activities, color=colors, edgecolor='black', linewidth=0.5, alpha=0.8)

# Customize for top-journal quality: Sans-serif font, tight layout, labels
ax.set_xlabel('Pilot Phase', fontsize=12, fontfamily='sans-serif')
ax.set_ylabel('Activity Duration (minutes)', fontsize=12, fontfamily='sans-serif')
ax.set_title('8-Week Pilot Timeline', fontsize=14, fontweight='bold', fontfamily='sans-serif', pad=20)
ax.set_ylim(0, 30)  # Clean y-axis scaling
ax.grid(axis='y', linestyle='--', alpha=0.3)  # Subtle grid for readability

# Annotate key events (e.g., AR peak in Week 4)
ax.annotate('AR Interaction Peak', xy=('Week 4', 25), xytext=('Week 4', 28),
            arrowprops=dict(arrowstyle='->', color='red', lw=1.5),
            ha='center', fontsize=10, fontfamily='sans-serif')

# Legend for color coding (placed outside for clarity)
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color='#1f77b4', lw=4, label='Introduction'),
    Line2D([0], [0], color='#2ca02c', lw=4, label='Practice'),
    Line2D([0], [0], color='#ff7f0e', lw=4, label='Assessment'),
    Line2D([0], [0], color='#d62728', lw=4, label='Reflection')
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=10)

# Rotate x-labels for readability
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save as high-quality PNG and PDF
png_path = os.path.join(output_dir, 'Figure_3-2_8-Week_Pilot_Timeline.png')
pdf_path = os.path.join(output_dir, 'Figure_3-2_8-Week_Pilot_Timeline.pdf')
plt.savefig(png_path, dpi=300, bbox_inches='tight')
plt.savefig(pdf_path, bbox_inches='tight', format='pdf')
plt.close()  # Close to free memory

print(f"Figure saved to: {png_path} and {pdf_path}")