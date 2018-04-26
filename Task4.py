import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# 向其他人拨出电话的号码
call_others_list = [x[0] for x in calls]

# 发过或接收过短信的号码
texts_phone_list = sum([[x[0], x[1]] for x in texts], [])

# 接过其他电话的号码
answer_others_list = [x[1] for x in calls]

# 发过短信、接收过短信的号码和收到过其他电话的号码总的list
impossible_phone_list = texts_phone_list + answer_others_list

# 求向其他人拨出电话的号 和 接、收短信、接电话的号码 做差集
telemarketers_set = set(call_others_list) - set(impossible_phone_list)

# sorted对set得出排序后的list
telemarketer_set_sorted = sorted(telemarketers_set)

print("These numbers could be telemarketers: ")
for telemarketer in telemarketer_set_sorted:
    print(telemarketer)