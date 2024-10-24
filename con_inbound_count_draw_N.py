import datetime

import matplotlib.pyplot as plt

# 示例数据，替换为你的实际数据
data1 = [(datetime.datetime(2024, 9, 17, 16, 1, 14), 50), (datetime.datetime(2024, 9, 17, 16, 4, 14), 48), (datetime.datetime(2024, 9, 17, 16, 17, 16), 47), (datetime.datetime(2024, 9, 17, 16, 26, 17), 46), (datetime.datetime(2024, 9, 17, 16, 28, 17), 45), (datetime.datetime(2024, 9, 17, 16, 29, 17), 44), (datetime.datetime(2024, 9, 17, 17, 5, 21), 43), (datetime.datetime(2024, 9, 17, 17, 57, 26), 42), (datetime.datetime(2024, 9, 17, 18, 20, 29), 41), (datetime.datetime(2024, 9, 17, 19, 4, 34), 40), (datetime.datetime(2024, 9, 17, 20, 15, 41), 39), (datetime.datetime(2024, 9, 17, 20, 28, 43), 38), (datetime.datetime(2024, 9, 17, 20, 34, 43), 37), (datetime.datetime(2024, 9, 18, 1, 1, 10), 36), (datetime.datetime(2024, 9, 18, 3, 11, 23), 35), (datetime.datetime(2024, 9, 18, 7, 24, 48), 34), (datetime.datetime(2024, 9, 18, 7, 57, 51), 33), (datetime.datetime(2024, 9, 18, 8, 17, 53), 32), (datetime.datetime(2024, 9, 18, 9, 16, 58), 31), (datetime.datetime(2024, 9, 18, 11, 12, 10), 30), (datetime.datetime(2024, 9, 18, 13, 49, 27), 29), (datetime.datetime(2024, 9, 18, 14, 31, 31), 28), (datetime.datetime(2024, 9, 18, 14, 51, 33), 27), (datetime.datetime(2024, 9, 18, 19, 2, 57), 26), (datetime.datetime(2024, 9, 19, 14, 35, 54), 25), (datetime.datetime(2024, 9, 23, 21, 0, 16), 24), (datetime.datetime(2024, 9, 24, 2, 5, 47), 23), (datetime.datetime(2024, 9, 24, 9, 0, 28), 22), (datetime.datetime(2024, 9, 24, 15, 50, 11), 22)]

data2 =[(datetime.datetime(2024, 9, 17, 17, 33, 41), 50), (datetime.datetime(2024, 9, 17, 17, 40, 42), 49), (datetime.datetime(2024, 9, 17, 18, 19, 46), 48), (datetime.datetime(2024, 9, 17, 19, 7, 51), 47), (datetime.datetime(2024, 9, 17, 19, 36, 54), 45), (datetime.datetime(2024, 9, 17, 20, 35, 1), 44), (datetime.datetime(2024, 9, 17, 22, 21, 11), 43), (datetime.datetime(2024, 9, 18, 0, 41, 25), 42), (datetime.datetime(2024, 9, 18, 2, 1, 33), 41), (datetime.datetime(2024, 9, 18, 3, 2, 39), 40), (datetime.datetime(2024, 9, 18, 6, 6, 56), 39), (datetime.datetime(2024, 9, 18, 7, 58, 7), 38), (datetime.datetime(2024, 9, 18, 13, 49, 43), 36), (datetime.datetime(2024, 9, 18, 14, 51, 49), 35), (datetime.datetime(2024, 9, 18, 21, 24, 28), 34), (datetime.datetime(2024, 9, 18, 22, 19, 33), 33), (datetime.datetime(2024, 9, 19, 9, 28, 40), 32), (datetime.datetime(2024, 9, 19, 13, 4, 2), 31), (datetime.datetime(2024, 9, 19, 20, 56, 49), 30), (datetime.datetime(2024, 9, 19, 22, 38, 59), 29), (datetime.datetime(2024, 9, 20, 4, 55, 37), 28), (datetime.datetime(2024, 9, 20, 5, 24, 40), 25), (datetime.datetime(2024, 9, 20, 5, 52, 43), 24), (datetime.datetime(2024, 9, 20, 14, 27, 36), 23), (datetime.datetime(2024, 9, 20, 19, 10, 4), 22), (datetime.datetime(2024, 9, 20, 19, 46, 8), 21), (datetime.datetime(2024, 9, 21, 12, 55, 52), 20), (datetime.datetime(2024, 9, 22, 9, 13, 55), 19), (datetime.datetime(2024, 9, 24, 12, 31, 10), 18), (datetime.datetime(2024, 9, 24, 15, 50, 1), 18)]
data3 =[(datetime.datetime(2024, 9, 17, 20, 5, 56), 50), (datetime.datetime(2024, 9, 17, 20, 20, 58), 49), (datetime.datetime(2024, 9, 17, 20, 23, 58), 48), (datetime.datetime(2024, 9, 17, 20, 59, 2), 47), (datetime.datetime(2024, 9, 17, 21, 24, 4), 46), (datetime.datetime(2024, 9, 17, 22, 36, 11), 45), (datetime.datetime(2024, 9, 18, 1, 0, 26), 44), (datetime.datetime(2024, 9, 18, 5, 32, 53), 43), (datetime.datetime(2024, 9, 18, 6, 2, 56), 42), (datetime.datetime(2024, 9, 18, 6, 4, 56), 41), (datetime.datetime(2024, 9, 18, 6, 58, 1), 40), (datetime.datetime(2024, 9, 18, 7, 15, 3), 39), (datetime.datetime(2024, 9, 18, 7, 17, 3), 38), (datetime.datetime(2024, 9, 18, 7, 58, 7), 37), (datetime.datetime(2024, 9, 18, 11, 12, 26), 36), (datetime.datetime(2024, 9, 18, 12, 0, 31), 35), (datetime.datetime(2024, 9, 18, 13, 49, 43), 33), (datetime.datetime(2024, 9, 18, 14, 51, 49), 32), (datetime.datetime(2024, 9, 18, 15, 13, 51), 31), (datetime.datetime(2024, 9, 18, 17, 46, 7), 30), (datetime.datetime(2024, 9, 18, 21, 59, 31), 29), (datetime.datetime(2024, 9, 19, 7, 33, 29), 28), (datetime.datetime(2024, 9, 19, 10, 0, 44), 27), (datetime.datetime(2024, 9, 19, 16, 0, 19), 26), (datetime.datetime(2024, 9, 19, 16, 51, 24), 25), (datetime.datetime(2024, 9, 19, 18, 0, 31), 24), (datetime.datetime(2024, 9, 19, 18, 53, 36), 23), (datetime.datetime(2024, 9, 20, 5, 5, 38), 22), (datetime.datetime(2024, 9, 20, 5, 52, 43), 21), (datetime.datetime(2024, 9, 21, 12, 23, 48), 20), (datetime.datetime(2024, 9, 21, 22, 34, 51), 19), (datetime.datetime(2024, 9, 22, 12, 43, 16), 18), (datetime.datetime(2024, 9, 23, 1, 12, 32), 17), (datetime.datetime(2024, 9, 24, 12, 31, 10), 16), (datetime.datetime(2024, 9, 24, 15, 54, 1), 16)]

data4 =[(datetime.datetime(2024, 9, 17, 20, 52, 38), 50), (datetime.datetime(2024, 9, 17, 21, 42, 43), 49), (datetime.datetime(2024, 9, 18, 0, 24, 59), 48), (datetime.datetime(2024, 9, 18, 1, 51, 8), 47), (datetime.datetime(2024, 9, 18, 5, 21, 28), 46), (datetime.datetime(2024, 9, 18, 5, 24, 28), 45), (datetime.datetime(2024, 9, 18, 5, 47, 31), 42), (datetime.datetime(2024, 9, 18, 7, 17, 39), 41), (datetime.datetime(2024, 9, 18, 7, 57, 43), 40), (datetime.datetime(2024, 9, 18, 8, 55, 48), 39), (datetime.datetime(2024, 9, 18, 13, 49, 18), 38), (datetime.datetime(2024, 9, 18, 14, 51, 24), 37), (datetime.datetime(2024, 9, 18, 19, 46, 53), 36), (datetime.datetime(2024, 9, 18, 22, 50, 11), 35), (datetime.datetime(2024, 9, 18, 23, 21, 14), 34), (datetime.datetime(2024, 9, 19, 2, 1, 30), 33), (datetime.datetime(2024, 9, 20, 3, 8, 2), 32), (datetime.datetime(2024, 9, 20, 5, 25, 16), 30), (datetime.datetime(2024, 9, 20, 5, 39, 18), 31), (datetime.datetime(2024, 9, 20, 19, 45, 46), 29), (datetime.datetime(2024, 9, 22, 9, 13, 37), 28), (datetime.datetime(2024, 9, 24, 0, 28, 37), 27), (datetime.datetime(2024, 9, 24, 15, 33, 10), 26), (datetime.datetime(2024, 9, 24, 15, 50, 11), 26)]

all_data = [data1, data2, data3, data4]
colors = ['purple', 'green', 'lightblue', 'orange']
labels = ['2 hours', '4 hours', '8 hours', '1 day']
# 找到每个数据集中n=34第一次出现的时间
def get_first_time(data):
    for timestamp, count in data:
        if count == 50:
            return timestamp
    return None

# 绘制多个数据集
plt.figure(figsize=(10, 6))

for idx, data in enumerate(all_data):
    if not data:
        continue

    first_time = get_first_time(data)
    if not first_time:
        print(f"No initial count of 34 found in dataset {idx + 1}.")
        continue

    # 计算每个n的时间差（与n=34第一次出现的时间的时间差，单位为天）
    time_diffs = [(timestamp - first_time).total_seconds() / (60 * 60 * 24) for timestamp, _ in data]
    inbound_counts = [count for _, count in data]

    # 绘制折线图
    plt.plot(time_diffs, inbound_counts, marker='o', linestyle='-', color=colors[idx], label=labels[idx])

plt.xlabel('Time (days)')
plt.ylabel('Total Count (n)')
plt.title('total counts of clients with different online durations over time')
plt.grid(True)
plt.legend()
plt.show()
