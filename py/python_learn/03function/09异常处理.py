#try：将可能出错的语句放在try中；
#except：如果发生错误就将程序执行转到except子句开始处

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('error')


print(spam(0))
print(spam(2))