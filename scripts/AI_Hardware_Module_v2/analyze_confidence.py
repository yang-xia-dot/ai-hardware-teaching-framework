import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
# 新增：设置中文字体支持（修复警告）
plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei']  # 支持中文
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号
# 设置基本目录
BASE_DIR = r"H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2"
LOGS_DIR = os.path.join(BASE_DIR, "logs")
OUTPUT_DIR = os.path.join(BASE_DIR, "demos")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# 文件路径
pest_file = os.path.join(LOGS_DIR, "week4_detection_results.xlsx")
healthy_file = os.path.join(LOGS_DIR, "healthy_detection_results.xlsx")

# 读取Excel文件
try:
    pest_df = pd.read_excel(pest_file)
    healthy_df = pd.read_excel(healthy_file)
    print("两个Excel文件读取成功！")
except Exception as e:
    print(f"读取文件出错: {e}. 请检查logs文件夹下的文件。")
    exit(1)

# 分析Pest组 (1-5.jpg, 假设标签为"pest damage"即正确)
pest_conf = pest_df["Confidence (%)"].values
pest_avg_conf = np.mean(pest_conf)
pest_accuracy = 1.0 if all(pest_df["Predicted Label"] == "pest damage") else 0.0  # 简单准确率
print(f"\n=== Pest组分析 (1-5.jpg) ===")
print(f"平均置信度: {pest_avg_conf:.2f}%")
print(f"准确率: {pest_accuracy * 100:.0f}% (全预测为pest damage)")
print(f"最高置信: {np.max(pest_conf):.2f}% (图片: {pest_df.loc[np.argmax(pest_conf), 'Image']})")
print(f"最低置信: {np.min(pest_conf):.2f}% (图片: {pest_df.loc[np.argmin(pest_conf), 'Image']})")

# 分析Healthy组 (6-10.jpg, 正确标签为"healthy crop")
healthy_conf = healthy_df["Confidence (%)"].values
healthy_correct = (healthy_df["Predicted Label"] == "healthy crop").sum() / len(healthy_df)
healthy_avg_conf = np.mean(healthy_conf)
print(f"\n=== Healthy组分析 (6-10.jpg) ===")
print(f"平均置信度: {healthy_avg_conf:.2f}%")
print(f"准确率: {healthy_correct * 100:.0f}% ({healthy_correct * 5}/5 正确)")
print(f"最高置信: {np.max(healthy_conf):.2f}% (图片: {healthy_df.loc[np.argmax(healthy_conf), 'Image']})")
print(f"最低置信: {np.min(healthy_conf):.2f}% (图片: {healthy_df.loc[np.argmin(healthy_conf), 'Image']})")

# 整体对比
print(f"\n=== Pest vs Healthy 对比 ===")
comparison = pd.DataFrame({
    "组别": ["Pest", "Healthy"],
    "平均置信度 (%)": [pest_avg_conf, healthy_avg_conf],
    "准确率 (%)": [pest_accuracy * 100, healthy_correct * 100]
})
print(comparison)

# 保存对比到新Excel
analysis_df = pd.concat([pest_df, healthy_df], ignore_index=True)
analysis_df["组别"] = ["Pest"] * len(pest_df) + ["Healthy"] * len(healthy_df)
output_analysis_path = os.path.join(LOGS_DIR, "confidence_analysis.xlsx")
analysis_df.to_excel(output_analysis_path, index=False)
print(f"\n详细分析结果保存到: {output_analysis_path}")

# 生成柱状图对比平均置信度
plt.figure(figsize=(8, 5))
groups = ["Pest", "Healthy"]
avgs = [pest_avg_conf, healthy_avg_conf]
bars = plt.bar(groups, avgs, color=['red', 'green'], alpha=0.7)
plt.title("Pest vs Healthy 平均置信度对比")
plt.ylabel("平均置信度 (%)")
plt.ylim(0, 100)
for bar, avg in zip(bars, avgs):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, f"{avg:.1f}%",
             ha='center', va='bottom')
output_chart_path = os.path.join(OUTPUT_DIR, "confidence_comparison.png")
plt.savefig(output_chart_path)
plt.close()
print(f"对比柱状图保存到: {output_chart_path}")