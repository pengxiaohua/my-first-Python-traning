import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# 创建一个生成{号码: 时长}的字典的函数
def createDict(list):
    new_dict = {}
    for li in list:
        # 判断主叫号码
        if li[0] in new_dict:
            new_dict[li[0]] += int(li[3])
        elif li[0] not in new_dict:
            new_dict[li[0]] = int(li[3])
         # 判断被叫号码
        if li[1] in new_dict:
            new_dict[li[1]] += int(li[3])
        elif li[1] not in new_dict:
            new_dict[li[1]] = int(li[3])
    
    return new_dict

calls_dict = createDict(calls)

# 根据callDict的value对callDict进行排序,生成value由小到大对应的key的list
calls_key_sorted = sorted(calls_dict, key = lambda k: calls_dict[k])

# 找出通话总时长最多的号码，即最后一个
longest_time_number = calls_key_sorted[-1]

# 通话最长的时长
longest_time = calls_dict[longest_time_number]

print("{} spent the longest time, {} seconds, on the phone during"\
        "September 2016.".format(longest_time_number, longest_time))
