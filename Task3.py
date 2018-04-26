import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def createSet(str, list):
    new_list = []
    code_list = []
    # 遍历list找出被班加罗尔固定电话呼叫的电话
    for li in list:
        if str in li[0]:
            new_list.append(li[1])

    for item in new_list:
        # 判断以 (0 开头的固定电话
        if '(0' in item:
            # 用正则找出()括号内的code
            code_list.append(re.findall(r'[^()]+', item)[0])
        else:
            # 其他移动电话
            code_list.append(item[:4])
    return code_list

# 班加罗尔呼叫的电话list
code_080_list = createSet('(080)', calls)
# 去重
unique_code_list = set(code_080_list)
# 对code排序
sorted_unique_code_list = sorted(unique_code_list)

# 班加罗尔打往班加罗尔的电话list
code_080_to_080 = []
for code in code_080_list:
    if '080' in code:
        code_080_to_080.append(code)

# 求出比率
rate = len(code_080_to_080) / len(code_080_list)
# 保留2位小数的百分比
percentage = '%.2f%%' % (rate * 100)

print("The numbers called by people in Bangalore have codes:")
for code in sorted_unique_code_list:
    print(code)

print("{} percent of calls from fixed lines in Bangalore are " \
        "calls to other fixed lines in Bangalore.".format(percentage))
