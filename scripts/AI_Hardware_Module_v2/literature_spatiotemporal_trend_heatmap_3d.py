# English version - Combined 2D Plots using Matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data for Heatmap
years = ['2023', '2024', '2025']
themes = [
    'Simulation Tools',
    'Behavioral Detection',
    'Low-Resource Optimization',
    'Model Compatibility',
    'Explainable AI',
    'Ethics & Inclusivity',
    'Performance Quantification',
    'Feedback Mechanisms',
    'LLM Localization',
    'Diversity Practices'
]

data = np.array([
    [2, 1, 1, 1, 1, 1, 1, 0, 0, 1],  # 2023
    [3, 2, 2, 1, 1, 1, 1, 1, 0, 0],  # 2024
    [1, 0, 1, 0, 0, 1, 0, 1, 1, 1]   # 2025
]).T  # Transpose for themes as rows, years as columns

# Data for Line Chart
stages = [
    'Problem Identification',
    'Infrastructure Assessment',
    'Tool Integration',
    'VT Optimization',
    'Localization Adaptation',
    'SEM Validation',
    'Risk Management',
    'Output Innovation'
]

low_resource = [0, 5, 20, 35, 50, 65, 80, 95]  # Cyan line
urban = [0, 10, 25, 40, 55, 70, 85, 100]       # Pink line

# Create figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Heatmap on left
sns.heatmap(data, annot=True, fmt='d', cmap='RdBu', ax=ax1,
            xticklabels=years, yticklabels=themes)
ax1.set_title('Literature Distribution Heatmap')
ax1.set_xlabel('Year')
ax1.set_ylabel('Research Themes')

# Line chart on right
ax2.plot(stages, low_resource, color='cyan', marker='o', label='Low-Resource Pathway')
ax2.plot(stages, urban, color='pink', marker='o', label='Urban Comparison Pathway')
ax2.set_title('System Pathway Overview')
ax2.set_xlabel('Process Stages')
ax2.set_ylabel('Progress (%)')
ax2.set_ylim(0, 100)
ax2.tick_params(axis='x', rotation=45)
ax2.legend()
ax2.grid(True)

plt.tight_layout()

# Save the figure
output_path = r'H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2\demos\literature_and_pathway_2d_english.png'
plt.savefig(output_path, dpi=300)

print(f'Figure saved to {output_path}')