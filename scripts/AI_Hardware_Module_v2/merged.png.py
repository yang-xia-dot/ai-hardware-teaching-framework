import os
from PIL import Image

# 设置文件夹路径（如果运行在 D:，可修改为 r"D:\pythonProject\AI_Hardware_Module_v2\demos"）
demos_path = r"H:\杨霞博士期间计划书\主2\子2.1\AI_Hardware_Module_v2\demos"

# 文件名列表（替换为实际文件名，如果不对）
files = [
    "interest_trend_ch.png",  # 图1
    "group_heatmap.png",  # 图2
    "timeline_bar.png",  # 图3
    "vit_performance.png",  # 图4
    "optimization_line.png",  # 图5
    "total_heatmap.png",  # 图6
    "tool_integration_scatter.png",  # 图7
    "improvement_bar.png"  # 图8
]

# 调试：检查路径和文件
print("Current working directory:", os.getcwd())
print("Demos path:", demos_path)
print("Does demos path exist?", os.path.exists(demos_path))

existing_files = []
for f in files:
    full_path = os.path.join(demos_path, f)
    if os.path.exists(full_path):
        existing_files.append(f)
    print(f"File {f} exists? {os.path.exists(full_path)}")

print("Existing files:", existing_files)
print("Number of existing files:", len(existing_files))

# 加载图像（只加载存在的）
images = []
for f in existing_files:
    try:
        img = Image.open(os.path.join(demos_path, f))
        images.append(img)
    except Exception as e:
        print(f"Error loading {f}: {e}")

if len(images) < 8:
    print("Warning: Only found", len(images), "images. Fusion may be incomplete. Check filenames or path.")


# 融合函数
def merge_images(img_list, direction='vertical', output_name='merged.png'):
    if not img_list:
        print(f"No images for {output_name}. Skipping.")
        return
    try:
        widths, heights = zip(*(i.size for i in img_list))
        if direction == 'vertical':
            total_height = sum(heights)
            max_width = max(widths)
            new_img = Image.new('RGB', (max_width, total_height), (255, 255, 255))
            y_offset = 0
            for img in img_list:
                new_img.paste(img, (0, y_offset))
                y_offset += img.height
        else:  # horizontal
            total_width = sum(widths)
            max_height = max(heights)
            new_img = Image.new('RGB', (total_width, max_height), (255, 255, 255))
            x_offset = 0
            for img in img_list:
                new_img.paste(img, (x_offset, 0))
                x_offset += img.width
        full_output = os.path.join(demos_path, output_name)
        new_img.save(full_output)
        print(f"Saved {output_name} to {full_output}")
    except Exception as e:
        print(f"Error merging for {output_name}: {e}")


# 执行融合（使用索引，如果图像少于8会跳过部分）
if len(images) >= 8:
    # 融合1: 图1 上, 图3 下
    merge_images([images[0], images[2]], 'vertical', 'dynamic_trend_merged.png')

    # 融合2: 图2 左, 图6 右
    merge_images([images[1], images[5]], 'horizontal', 'collaboration_heatmap_merged.png')

    # 融合3: 图4 左, 图8 右
    merge_images([images[3], images[7]], 'horizontal', 'performance_improvement_merged.png')

    # 融合4: 图5 上, 图7 下
    merge_images([images[4], images[6]], 'vertical', 'optimization_flow_merged.png')
else:
    print("Not enough images to merge all. Please check files.")

print("Done. Check demos folder for merged PNGs.")