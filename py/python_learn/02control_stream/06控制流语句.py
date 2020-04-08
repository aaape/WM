# #控制流是由控制流语句和条件表达式构成的
#
# #所有控制流语句都是以冒号结尾,后面跟着一个新的代码块（子句）
# #所有条件表达式的值都是布尔值
#
# #if 语句； 组成：if关键字、条件、冒号、下一行开始缩进代码块，称为if子句。中午翻译如果
# name = 'skr'
# if name == 'skr':
#     print(1)
#
# #else语句； 组成：else关键字、冒号、下一行开始缩进代码块，称为else子句。中文翻译否则
# name = 'skra'
# if name == 'skr':
#     print(1)
# else:
#     print(0)
#
# #elif语句；组成：elif关键字、条件表达式、冒号、下一行开始缩进代码块，称为elif子句。中文翻译为否则如果
# name = 'skra'
# if name == 'skr':
#     print(1)
# elif name == 'skra':
#     print(1)
# # =========================================================================================
#
#
# #while语句；组成：关键字while、条件表达式、冒号、下一行开始缩进代码块，称为while子句
# spam = 0
# while spam < 5:
#     print('hello,world')
#     spam = spam + 1
# #在while循环中，条件总是在每次“迭代”开始时检查（也就是每次循环执行时）。
# # 如果条件为True，子句就会执行，然后，再次检查条件。
# # 当条件第一次为False时，while子句就跳过。
#
#
# #if和while的异同：
# #共同点：if和while都会检查条件表达式的布尔值，如果为True，执行子句代码
# #不同点：if只会执行一次子句代码；while会循环子句代码，直到条件表达式的值为False
#
#
# #break语句；组成：仅break关键字
# while True:
#     print('please enter your name.')
#     name = input()
#     if name  == 'your name':
#         break
#     print('ty')
#
# spam = 0
# while spam < 5:
#     print('hello,world')
#     break
# #while循环可以通过break来中断循环，执行会跳出循环
#
# #continue语句。组成：仅continue关键字
# #像break语句一样，continue语句用于循环内部。
# # 如果程序执行遇到continue语句，就会马上跳回到循环开始处，重新对循环条件求值（这也是执行到达循环末尾时发生的事情）
# while True:
#     print('please enter your name.')
#     name = input()
#     if name  != 'your name':
#         continue
#     break

# ========================================================================================================#

#类真


#for语句 组成：for关键字、一个变量名、in关键字、可迭代对象、冒号、从下一行开始缩进代码块，称为for的子句
#for循环和while循环比较：
#while循环只要条件为真会一直循环执行子代码块
#for循环可以执行固定次数子代码块
#for循环
for i in range(6):
    print(i)
#while循环
N = 0;
while N < 6:
    print(N)
    N = N + 1

# range(start, end, step)：翻译成中文意思是：从起始值开始，到中止值结束，每隔多少个数字取一个
#range()不仅能用作递增生成序列，也能递减，递减结束值小于起始值，步长为负数