import os

# 获取当前工作目录
current_dir = os.getcwd()

# 设置图片文件夹路径
image_folder = current_dir  # 如果图片在子文件夹中，可以修改为 './img/background'

# 支持的图片扩展名
valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']

# 遍历目录中的所有文件
for filename in os.listdir(image_folder):
    # 获取文件的扩展名
    file_extension = os.path.splitext(filename)[1].lower()

    # 如果是有效的图片文件
    if file_extension in valid_extensions:
        # 生成 Markdown 图片语法
        image_path = f"/img/background/{filename}"
        markdown_syntax = f"[]()![{filename}]({image_path})"
        print(markdown_syntax)
