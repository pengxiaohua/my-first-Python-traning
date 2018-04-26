import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

texts_records = []
calls_records = []

# 遍历短信内容，取出其中的所有电话号码
texts_records = sum([[x[0], x[1]] for x in texts], [])

# 遍历电话内容，取出其中的所有电话号码
calls_records = sum([[x[0], x[1]] for x in calls], [])

# 合并短信和电话号码
all_records = texts_records + calls_records
# 生成set，去除重复电话号码
all_different_records = set(all_records)
# 求去重后的电话号码数量
count = len(all_different_records)

print("There are {} different telephone numbers in the records.".format(count))
