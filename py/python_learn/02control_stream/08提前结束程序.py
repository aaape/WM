#sys.exit();终止程序函数。该函数需要导入sys模块才能使用

#实例：
import sys

while True:
    print('not the end')
    N = input()
    if N == 'STOP':
        sys.exit()
