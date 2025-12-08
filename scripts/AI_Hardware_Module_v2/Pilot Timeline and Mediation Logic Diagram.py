# Chinese version - Pilot Timeline and Mediation Logic Diagram using Plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Set font for Chinese support
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False

# Data for left side: 8-week timeline bar heatmap
weeks = list(range(1, 9))
categories = ['学生参与', '活动时长', '协作强度']

# Fictional data: activity durations (minutes), collaboration scores (0-1)
durations = np.array([
    [30, 45, 60, 50, 55, 40, 35, 20],  # 学生参与
    [45, 60, 75, 65, 70, 55, 50, 30],  # 活动时长
    [20, 35, 50, 85, 70, 60, 75, 80]   # 协作强度 (scaled for bars, but use scores for heatmap)
])  # Rows: categories, Columns: weeks

collab_scores = np.array([
    [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],  # 学生参与 scores
    [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.8],  # 活动时长 scores
    [0.1, 0.2, 0.3, 0.85, 0.7, 0.6, 0.75, 0.8] # 协作强度 scores
])

# Phase colors for bars
phase_colors = ['blue']*2 + ['green']*3 + ['orange']*2 + ['red']*1  # Weeks 1-2 blue, 3-5 green, 6-7 orange, 8 red

# Data for right side: 3D scatter plot (25 students)
np.random.seed(42)
autonomy = np.random.uniform(0, 10, 25)
interest = np.random.uniform(0, 30, 25)
participation = np.random.uniform(0, 100, 25)
week_colors = np.linspace(0, 1, 25)  # Gradient from blue (low week) to red (high week)

# Create subplots: 1 row, 2 columns (left 2D, right 3D)
fig = make_subplots(
    rows=1, cols=2,
    specs=[[{"type": "xy"}, {"type": "scene"}]],
    column_widths=[0.5, 0.5],
    horizontal_spacing=0.1,
    subplot_titles=('8周试点时间线柱状热力图', '结果中介逻辑三维散点图')
)

# Left: Bar chart with heatmap overlay
for i, cat in enumerate(categories):
    for w in range(len(weeks)):
        # Add bars
        fig.add_trace(go.Bar(
            x=[weeks[w]],
            y=[durations[i, w]],
            marker_color=phase_colors[w],
            name=cat if w == 0 else None,
            showlegend=(w == 0),
            legendgroup=cat
        ), row=1, col=1)

# For heatmap overlay, use Heatmap on same subplot
fig.add_trace(go.Heatmap(
    z=collab_scores,
    x=weeks,
    y=categories,
    colorscale='RdBu',
    colorbar=dict(title='协作分数', x=0.45),
    showscale=True,
    zmin=0, zmax=1
), row=1, col=1)

# Annotations for peaks
fig.add_annotation(
    text="周4 AR峰值0.85",
    x=4, y='协作强度',
    showarrow=True,
    arrowhead=1,
    row=1, col=1
)
fig.add_annotation(
    text="周8 反思0.80",
    x=8, y='协作强度',
    showarrow=True,
    arrowhead=1,
    row=1, col=1
)
fig.add_annotation(
    text="周3 拐点兴趣+13.5%",
    x=3, y='学生参与',
    showarrow=True,
    arrowhead=1,
    row=1, col=1
)

# Update left axes
fig.update_xaxes(title_text="周次", row=1, col=1)
fig.update_yaxes(title_text="类别 / 时长 (分钟)", row=1, col=1)

# Right: 3D Scatter
fig.add_trace(go.Scatter3d(
    x=autonomy,
    y=interest,
    z=participation,
    mode='markers',
    marker=dict(
        size=participation / 10,  # Size based on participation
        color=week_colors,
        colorscale='RdBu',
        colorbar=dict(title='周次渐变', x=1.05),
        showscale=True
    ),
    text=[f'学生 {i+1}' for i in range(25)]
), row=1, col=2)

# Add mediation arrows (simplified as lines)
fig.add_trace(go.Scatter3d(
    x=[2, 8], y=[5, 25], z=[20, 80],
    mode='lines+text',
    line=dict(color='black', width=4),
    text=['', 'β=0.38'],
    textposition='top center',
    name='自主性 → 兴趣'
), row=1, col=2)

# Update right axes
fig.update_layout(
    scene=dict(
        xaxis_title='自主性得分 (0-10)',
        yaxis_title='兴趣提升 (0-30%)',
        zaxis_title='参与率 (0-100%)'
    )
)

# Add connecting arrow between subplots
fig.add_annotation(
    x=0.45, y=0.5,
    xref="paper", yref="paper",
    ax=0.55, ay=0.5,
    axref="paper", ayref="paper",
    showarrow=True,
    arrowhead=2,
    arrowsize=1.5,
    arrowwidth=2,
    arrowcolor="black",
    text="从试点过程到中介结果路径"
)

# Overall layout
fig.update_layout(
    title='图4: 试点时间线与结果中介逻辑图',
    width=1000, height=600,
    paper_bgcolor='lightblue'
)

# Save the figure
output_path = r'H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2\demos\pilot_timeline_mediation_logic_chinese.html'
fig.write_html(output_path)

print(f'Figure saved to {output_path}')