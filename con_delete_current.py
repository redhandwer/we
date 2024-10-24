# 定义文件路径
file_path = 'connection_log4.txt'  # 替换为你的文件路径
output_path = 'connection_log44v1.txt'  # 替换为你想保存的新文件路径

# 读取文件并过滤掉包含"Current"的行
with open(file_path, 'r') as file:
    lines = file.readlines()

# 过滤掉包含'Current'的行
filtered_lines = [line for line in lines if 'Current' not in line]

# 将过滤后的内容写入新文件
with open(output_path, 'w') as output_file:
    output_file.writelines(filtered_lines)

print(f"已成功删除包含 'Current' 的行，并将结果保存到 {output_path}")
