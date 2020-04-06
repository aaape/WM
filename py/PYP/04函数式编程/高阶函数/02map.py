# map函数
# 两个参数，参数一：函数；参数二：Iterable
# 实现：map函数将传入的参数函数依次作用到Iterable的每个元素，并把结果作为新的Iterator返回

def f(x):
    return x * x

r = map(f,[1, 3, 5, 7, 9]) # r是一个Iterator，惰性序列.
L = list(r)  # 把Iterator，转为Iterable：list

# 此函数也实现上面map函数的运算，map函数把运算规则抽象了
C = []
for n in [1, 3, 5, 7, 9]:
    C.append(f(n))


# reduce函数
# 两个参数：参数一：函数；参数二：interable
# reduce函数会把传入的的序列依次代入函数参数中（参数函数必须接收两个参数），并把函数参数的返回值和序列下一个元素做累积计算
# reduce(f,[1,2,3,4]) = f(f(f(1，2),3), 4)


