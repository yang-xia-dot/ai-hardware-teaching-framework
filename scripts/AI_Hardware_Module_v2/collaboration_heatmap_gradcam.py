import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import os
from sklearn.preprocessing import MinMaxScaler  # For normalizing simulated data
import webbrowser  # For specifying browser

# Simulate collaboration intensity data (25 students x 8 weeks)
# In real scenario, load from 'precomputed_intensity.npy' or compute via Grad-CAM
np.random.seed(42)  # For reproducibility
collab_intensity = np.random.uniform(0.1, 0.9, size=(25, 8))  # Simulated peaks, e.g., weeks 4-6 higher for collaboration
# Simulate Grad-CAM peaks: Boost weeks 4-6 for student collaboration hotspots
collab_intensity[:, 3:6] *= 1.2  # Emphasize AR interaction intensity
collab_intensity = np.clip(collab_intensity, 0, 1)  # Normalize to [0,1]

# Create DataFrame for heatmap
weeks = [f'Week {i+1}' for i in range(8)]
students = [f'Student {i+1}' for i in range(25)]
df_heatmap = pd.DataFrame(collab_intensity, index=students, columns=weeks)

# Create the heatmap
fig = px.imshow(
    df_heatmap.values,
    labels=dict(x="Week", y="Student ID", color="Collaboration Intensity"),
    x=weeks,
    y=students,
    color_continuous_scale='RdYlBu_r',  # Red-Yellow-Blue reversed for hot spots
    aspect="auto",
    title="Figure: 8-Week Heatmap with Grad-CAM Collaboration Peaks"
)

# Enhance for publication quality: Add annotations for Grad-CAM insights
fig.add_annotation(
    text="Grad-CAM Peak (>0.8): High AR Group Interaction",
    x=4, y=0,  # Position near week 4-6
    xref="x", yref="paper",
    showarrow=True,
    arrowhead=2,
    ax=20, ay=-30,
    font=dict(size=10, color="white")
)

# Update layout for top-tier journal style
fig.update_layout(
    title={
        'text': "8-Week Heatmap with Grad-CAM Collaboration Peaks",
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 16, 'family': 'Arial Black'}
    },
    xaxis_title="Week",
    yaxis_title="Student ID",
    coloraxis_colorbar=dict(
        title=dict(side="right", text="Intensity"),
        tickvals=[0, 0.5, 1],
        ticktext=['Low', 'Medium', 'High']
    ),
    width=800,
    height=600,
    font=dict(size=12),
    plot_bgcolor='white',
    paper_bgcolor='white'
)

# Hover template for Grad-CAM explanation
fig.update_traces(
    hovertemplate='<b>%{y}</b><br>Week: %{x}<br>Intensity: %{z:.2f}<br>Grad-CAM Insight: %{customdata}<extra></extra>',
    customdata=np.where(collab_intensity > 0.8, 'High Collaboration Hotspot', 'Standard Interaction')
)

# Specify the save path
save_path = r'H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2\demos'
os.makedirs(save_path, exist_ok=True)

# Save as HTML (backup, open manually in Chrome if needed)
html_path = os.path.join(save_path, 'collaboration_heatmap_gradcam.html')
fig.write_html(html_path)
print(f"HTML saved to: {html_path} (Open in Chrome manually if show() fails)")

# Fixed show(): Force open in Google Chrome on Windows (full path)
temp_html = os.path.join(save_path, 'temp_plot.html')
plotly_url = fig.to_html(include_plotlyjs='cdn')  # Generate HTML string
with open(temp_html, 'w') as f:
    f.write(plotly_url)

# Windows-specific: Use full path to chrome.exe (adjust if your install path differs)
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
try:
    webbrowser.get(f'{chrome_path} %s').open(f'file://{temp_html}')
    print("Opened in Chrome successfully!")
except webbrowser.Error:
    # Fallback: Use default browser
    webbrowser.open(f'file://{temp_html}')
    print("Fallback: Opened in default browser (may be 360). Use manual open for Chrome.")

# For PNG save (Kaleido issue): Retry after pip install kaleido
try:
    fig.write_image(os.path.join(save_path, 'collaboration_heatmap_gradcam.png'), scale=3, width=800, height=600)
    print("PNG saved successfully.")
except Exception as e:
    print(f"PNG save failed: {e}. Ensure 'pip install --upgrade kaleido' and retry.")

# Clean up temp file
if os.path.exists(temp_html):
    os.remove(temp_html)

print("Script complete. Check console for paths.")