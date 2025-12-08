import plotly.graph_objects as go
import numpy as np

# 创建3D路径图的整体布局
fig = go.Figure()

# 起点: 城乡差距热力图 (简化成3D表面热力图)
x_heat = ['AI应用率', '系统稳定性', '协作准确率']
y_heat = ['农村', '城市', '全球']
z_heat = np.array([[30, 70, 50], [55, 95, 75], [45, 85, 65]])  # 示例数据百分比（可替换为真实差距值）
fig.add_trace(go.Surface(z=z_heat, x=x_heat, y=y_heat, colorscale='Reds', name='起点: 城乡差距热力图',
                         colorbar=dict(title='差距%'), showscale=True))

# 中间: 模块路径 (用3D散点和线连接模块)
modules = ['MobileViT', 'QEMU', 'Logisim-evolution', 'Tinkercad AR', 'MagicSchool.ai', 'Blender', 'UNESCO原则']
x_modules = np.arange(len(modules)) + 3  # 偏移到热力右边
y_modules = np.zeros(len(modules))
z_modules = np.linspace(0, 50, len(modules))  # 向上延伸
fig.add_trace(go.Scatter3d(x=x_modules, y=y_modules, z=z_modules, mode='lines+markers+text',
                           marker=dict(size=10, color='green'), line=dict(color='green', width=5),
                           text=modules, textposition='top center', name='中间: 工具模块'))

# 添加数据流标注 (用额外的Scatter3d文本trace，因为3D注解不支持z直接)
ann_texts = ['离线fallback确保2G兼容', '本土训练最小化偏见']
ann_x = [3.5, 4.5]
ann_y = [0.5, 0.5]  # 轻微偏移y以避免重叠
ann_z = [10, 20]
fig.add_trace(go.Scatter3d(x=ann_x, y=ann_y, z=ann_z, mode='text',
                           text=ann_texts, textfont=dict(size=12, color='black'), name='数据流标注'))

# 终点: 量化提升柱状图 (用3D Cone或Bar模拟，但Plotly 3D Bar有限，用Scatter3d柱模拟)
indicators = ['效率+30%', '准确率+25%', '参与率+28%']
x_bar = np.array([len(modules) + 2] * 3)
y_bar = np.arange(3)
z_bar = [30, 25, 28]  # 高度作为z
fig.add_trace(go.Scatter3d(x=x_bar, y=y_bar, z=[0]*3, mode='markers', marker=dict(size=1), showlegend=False))  # 底
fig.add_trace(go.Scatter3d(x=x_bar, y=y_bar, z=z_bar, mode='markers+text', marker=dict(size=10, color='orange'),
                           text=indicators, textposition='top center', name='终点: 量化提升'))

# 添加时间维度z轴演进 (渐变线)
weeks = np.linspace(0, 8, 9)
x_time = np.full(9, len(modules) + 3)
y_time = np.full(9, -1)
z_time = weeks * 5  # 缩放
fig.add_trace(go.Scatter3d(x=x_time, y=y_time, z=z_time, mode='lines', line=dict(color='blue', width=3, dash='dot'),
                           name='时间维度: 周1到周8'))

# 整体布局设置
fig.update_layout(
    title='整体系统框架与工具整合路径图',
    scene=dict(
        xaxis_title='路径步骤',
        yaxis_title='模块/地区',
        zaxis_title='差距/提升%',
        bgcolor='lightgray',
        aspectmode='cube'
    ),
    width=800, height=600
)

# 保存为HTML (互动版本)
fig.write_html('H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2\demos\system_framework_path.html')

# 打印确认（可选，用于检查）
print("图已生成并保存为 'system_framework_path.html'。打开HTML文件查看互动3D图。")