#5.2 漂亮打印模块
# pprint.pprint(dict)将当前字典的的键对值一行一对打印出来
# print(pprint.pformat(dict))将当前字典的键对值一行一对成打印成字符串
import pprint
D = 'it is been a long time'
cal = {}
for word in D:
    cal.setdefault(word, 0)
    cal[word] = cal[word] + 1
print(pprint.pformat(cal))