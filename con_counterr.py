import re
from collections import Counter

# 定义从日志行中提取信息的正则表达式
log_pattern = re.compile(r'Removing p2p peer.*duration=([0-9.]+)([a-z]+).*err="([^"]+)"')

# 存储符合条件的行的列表
matching_lines = []

# 错误统计
error_counter = Counter()

# 打开并读取文件时指定编码为 'utf-8'
with open('shiyan0.log', 'r', encoding='utf-8') as file:
    for line in file:
        # 查找包含 "Removing p2p peer" 的行并匹配正则表达式
        match = log_pattern.search(line)
        if match:
            duration_value = float(match.group(1))  # 提取 duration 数值
            duration_unit = match.group(2)         # 提取 duration 单位
            err_message = match.group(3)           # 提取 err 错误信息

            # 将时间单位转换为毫秒
            if duration_unit == 'ms':
                duration_ms = duration_value
            elif duration_unit == 's':
                duration_ms = duration_value * 1000
            elif duration_unit == 'm':
                duration_ms = duration_value * 60000
            elif duration_unit == 'h':
                duration_ms = duration_value * 60*60000

            # 筛选出 duration >= 5 分钟的行
            if duration_ms >= 300000:
                matching_lines.append(line)
                error_counter[err_message] += 1

# 输出符合条件的行
print("符合条件的行:")
for line in matching_lines:
    print(line.strip())

# 输出错误类型统计结果
print("\n错误类型统计:")
for err, count in error_counter.items():
    print(f"{err}: {count}")
