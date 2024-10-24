import re
from datetime import datetime
import matplotlib.pyplot as plt
a = [0] * 100
# 读取文件内容
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

# 解析日志内容，提取时间戳和Outbound Count
def parse_data(lines):
    data = []
    timestamp_16 = None

    for i in range(len(lines)):
        # 匹配时间戳
        time_match = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", lines[i])
        if time_match:
            timestamp = datetime.strptime(time_match.group(1), "%Y-%m-%d %H:%M:%S")

        # 匹配Outbound Count: N
        outbound_match = re.search(r"Outbound Count: (\d+)", lines[i])
        if outbound_match:
            outbound_count = int(outbound_match.group(1))
            if outbound_count <= 16 and outbound_count >= 1:
                if outbound_count == 16 and not timestamp_16:
                    timestamp_16 = timestamp  # 保存n=16的时间戳
                # 记录时间戳和Outbound Count
                if timestamp_16:
                    a[outbound_count]+=1
                    if i == len(lines) - 3:
                        print(outbound_count)
                        data.append((timestamp, outbound_count))
                    if a[outbound_count]<=1:
                        data.append((timestamp, outbound_count))

    return data, timestamp_16

# 计算时间差并绘制图表
def plot_outbound_count(data, first_time):
    if not data:
        print("No valid data found.")
        return

    # 计算每个n的时间差（与n=16第一次出现的时间的时间差，单位为天）
    time_diffs = [(timestamp - first_time).total_seconds() / (60 * 60 * 24) for timestamp, _ in data]
    outbound_counts = [count for _, count in data]

    # 绘制折线图
    plt.figure(figsize=(10, 6))
    plt.plot(time_diffs, outbound_counts, marker='o', linestyle='-', color='blue')
    plt.xlabel('Time Difference (days)')
    plt.ylabel('Outbound Count (n)')
    plt.title('Outbound Count Over Time (from n=16)')
    plt.grid(True)
    plt.show()

# 主函数
def main(file_path):
    lines = read_file(file_path)
    data, timestamp_16 = parse_data(lines)

    if timestamp_16:
        # 绘制图表
        plot_outbound_count(data, timestamp_16)
        print(data)
    else:
        print("No outbound count of 16 found.")

# 调用主函数
file_path = 'connection_log4.txt'  # 替换为你的文件路径
main(file_path)
