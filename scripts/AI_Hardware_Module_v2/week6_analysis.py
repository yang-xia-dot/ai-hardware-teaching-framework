import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from scipy.stats import linregress

# Define root directory
root_dir = r'H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2'
logs_dir = os.path.join(root_dir, 'logs')
demos_dir = os.path.join(root_dir, 'demos')

# Create directories if not exist
os.makedirs(demos_dir, exist_ok=True)

# Read results from week6_results.xlsx
results_path = os.path.join(logs_dir, 'week6_results.xlsx')
df = pd.read_excel(results_path)

# Simulate visualization impact (proxy: 1 for high-impact AR demo, 0 for none)
np.random.seed(42)
df['Visualization'] = np.random.choice([0, 1], size=len(df), p=[0.3, 0.7])

# Linear regression: Improvement ~ Visualization
slope, intercept, r_value, p_value, std_err = linregress(df['Visualization'], df['Improvement'])
print(f"Regression: β = {slope:.2f}, p = {p_value:.4f}")

# Group by level for heatmap
pivot = df.pivot_table(values='Improvement', index='Level', aggfunc=['mean', 'std']).reset_index()
pivot.columns = ['Level', 'Mean_Improvement', 'Std_Improvement']
pivot['Level'] = pd.Categorical(pivot['Level'], categories=['Basic', 'Intermediate', 'Advanced'], ordered=True)
pivot = pivot.sort_values('Level')

# Generate heatmap (simplified: 1D-like heatmap for levels)
plt.figure(figsize=(6, 2))
sns.heatmap(pivot[['Mean_Improvement']].T, annot=True, fmt='.2f', cmap='YlGn',
            xticklabels=pivot['Level'], yticklabels=['Improvement'], cbar_kws={'label': 'Mean Improvement'})
plt.title('Week 6 Improvement by Level')
plt.tight_layout()

# Save heatmap
heatmap_path = os.path.join(demos_dir, 'week6_level_heatmap.png')
plt.savefig(heatmap_path, dpi=300, bbox_inches='tight')
plt.close()

# Print confirmation
print("Generated demos/week6_level_heatmap.png at:")
print(heatmap_path)