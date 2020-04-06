# range(start, stop[, step])
# start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
# stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
# step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)

# 生成list l
l = list(range(1,10))
# 另一种生成法
L= []
for x in range(1,11):
    L.append(x*x)
# 简写
L = [x*x for y in range(1,11)]

# 两层循环
str = [m+n for m in 'ABC' for n in 'EFG']
print(str)

# for可以循环两个或多个变量，这样可以生成键对值的list
d = {'a':'c','b':'e'}
z = [x +'='+ y for x,y in d.items()]
print(z)

# 把列表的大写变小写
c = ['FUCK','THE','REGULATIONS']
k = [s.lower() for s in c]
print(k)

# if...else加入到列表生成式中，筛选元素.
# if写在for后面不能带else，这是因为for前面的部分是一个表达式
p = [x for x in range(1,100) if x % 2 == 0]
print(p)
# if写在for前面必须带else
q = [x if x % 2 == 0 else -x for x in range(5,45)]
print(q)