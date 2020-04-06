# filter()
# 两个参数，参数一：函数；参数二：序列
# 把函数参数作用于序列中的每个元素，根据返回值（布尔值）决定保留还是丢弃元素
# filter()函数返回的是一个Iterator
def is_odd(n):
    return n % 2 == 1
list(filter(is_odd,[1,2,3,4,5]))

# Python strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列

def not_empty(s):
    return s and s.strip()

list(filter(not_empty,['A', '', 'B', None, 'C', '   ']))