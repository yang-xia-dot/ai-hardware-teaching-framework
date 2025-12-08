import matplotlib.pyplot as plt
import numpy as np
import os

# Data for the timeline: Years vs. Number of Publications
years = [2023, 2024, 2025]
publications = [9, 12, 6]  # Based on aggregated literature counts from heatmap (2023: ~9, 2024: ~12 peak, 2025: ~6)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 5))  # Professional size suitable for top-tier journals

# Plot the line with markers
ax.plot(years, publications, marker='o', linewidth=2.5, markersize=8, color='#2E86AB', markerfacecolor='#A23B72', markeredgecolor='white', markeredgewidth=1.5)

# Customize the plot for a clean, publication-ready appearance
ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('Number of Publications', fontsize=12, fontweight='bold')
ax.set_title('Figure 2-1: Timeline of Publications in AI for Low-Resource Rural Education (2023-2025)', fontsize=14, fontweight='bold', pad=20)

# Set x-ticks to integer years
ax.set_xticks(years)
ax.set_xticklabels(years, fontsize=11)

# Add grid for readability
ax.grid(True, alpha=0.3, linestyle='--', linewidth=0.8)

# Improve aesthetics: remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.2)
ax.spines['bottom'].set_linewidth(1.2)

# Add value labels on markers for emphasis
for i, (year, pub) in enumerate(zip(years, publications)):
    ax.annotate(f'{pub}', (year, pub), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, fontweight='bold')

# Tight layout for optimal spacing
plt.tight_layout()

# Create demo directory if it doesn't exist
os.makedirs('demo', exist_ok=True)

# Save the figure in high resolution
plt.savefig('demo/figure2-1_timeline.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()  # Optional: display if running interactively