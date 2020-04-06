#一边循环一边计算的机制，称为生成器：generator
# 创建一个generator：把[]生成器 改成（）就创建了一个generator
# [x for x in range(10)]
# (x for x in range(10))

# generator可以用next()函数调用，是可迭代对象，所以可以用for循环

# 斐波那契:当前数字等于后两位之和
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
fib(10)

