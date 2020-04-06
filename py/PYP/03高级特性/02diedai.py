# 无论有无下标，只要是可迭代对象都可以用for...in迭代
# list[]有索引，tuple:(),dict{}键对值
# for i in list 迭代list中的每一项
l = [1, 2, 3]
for i in l:
    print(i)
# for key in dict 迭代dict默认迭代key，如果要迭代value
d = {'a':1, 2:'b', 3:4}
for k in d:
    print(k)
for v in d.values():
    print(v)
for k,w in d.items():
    print(k,v)

# 从collections模块导入Iterable类,判断数据是否为可迭代对象
# from collections import Iterable
# isinstance('abc',Iterable)
# isinstance(123, Iterable)

# 如果要迭代list的下标，需要用enumerate函数，把元素变成index-value的形式
for i,v in enumerate(['A', 'B', 'C']):
    print(i, v)

# 同时引用了两个变量
for x,y in [(1,2),(3,4)]:
    print(x,y)