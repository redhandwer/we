import re
from datetime import datetime
import matplotlib.pyplot as plt
a = [0] * 100

# 读取文件内容
def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines


# 解析日志内容，提取时间戳和Inbound Count
def parse_data(lines):
    data = []
    timestamp = None

    for i, line in enumerate(lines):
        # 匹配时间戳
        time_match = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", line)
        if time_match:
            timestamp = datetime.strptime(time_match.group(1), "%Y-%m-%d %H:%M:%S")

        # 匹配Inbound Count: N
        inbound_match = re.search(r"Inbound Count: (\d+)", line)
        if inbound_match:
            inbound_count = int(inbound_match.group(1))
            if 34 >= inbound_count >= 0:
                a[inbound_count]+=1
                if i == len(lines) - 4:
                    print(inbound_count)
                    data.append((timestamp, inbound_count))
                if a[inbound_count]<=1:
                    # 记录时间戳和对应的Inbound Count
                    data.append((timestamp, inbound_count))

    return data


# 计算时间差并绘制图表
def plot_inbound_count(data):
    if not data:
        print("No valid data found.")
        return

    # 找到n=34第一次出现的时间
    first_time = None
    for timestamp, count in data:
        if count == 34:
            first_time = timestamp
            break

    if not first_time:
        print("No initial count of 34 found.")
        return

    # 计算每个n的时间差（与n=34第一次出现的时间的时间差，单位为天）
    time_diffs = [(timestamp - first_time).total_seconds() / (60 * 60 * 24) for timestamp, _ in data]
    inbound_counts = [count for _, count in data]

    # 绘制折线图，保证每两个点之间直接连接
    plt.figure(figsize=(10, 6))
    plt.plot(time_diffs, inbound_counts, marker='o', linestyle='-', color='b')
    plt.xlabel('Time Difference (days)')
    plt.ylabel('Inbound Count (n)')
    plt.title('Inbound Count Drop Over Time (n=34 to n=19)')
    plt.grid(True)
    plt.show()


# 主函数
def main(file_path):
    lines = read_file(file_path)
    data = parse_data(lines)

    # 绘制图表
    plot_inbound_count(data)
    print(data)


# 调用主函数
file_path = 'connection_log4.txt'  # 使用上传的文件路径
main(file_path)
