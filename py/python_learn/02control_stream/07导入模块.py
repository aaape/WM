#内建函数：python程序可以调用的基本函数，如print(),input(),len()
#模块：包含一组相关函数的一个python程序，可以嵌入到你的程序中

#使用模块，以math模块为例：
import random #使用import导入random模块，可以一次性添加多个模块用逗号隔开
random.randint() #randint为random模块的一个函数，参数：整数A,整数B；作用：求两个整数间的一个随机整数；
#因为randint函数属于random模块，所以必须在函数名称前加上random，告诉python在random 模块中寻找这个函数


#另一种形式：from random import *；这种形式导入random，调用random模块中的函数就不需要random.作为前缀；但是代码可读性会降低
