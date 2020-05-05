#函数求值的结果，称为函数的返回值
#用def创建函数时，可以用return指定返回什么值

#return组成：return关键字，函数应该返回的值或表达式

#如果在return中使用了表达式，返回值就是该表达式求值的结果

import random

def getAnswer(num):
    if num == 1:
        return 'skr'
    elif num == 2:
        return 'nana'
    elif num == 3:
        return  'super saya'

r = random.randint(1,3)
fortune = getAnswer(r)
print(fortune)

#导入import模块
#定义getanswer函数，
#因为函数时被定义，而不是被调用,接下来执行 r =random.randint()
#getanswer函数被调用，r作为参数
#程序转移到getAnswer()函数的顶部，参数r被保存到函数的变元(形参)。
#函数体执行，根据参数r返回一个字符串到函数调用处，返回的字符串背负给一个名为fortune的变量
#执行打印函数把fortune打印出来

#表达式时值和操作符的组合，函数调用可以用在表达式中，因为返回值就是该函数要求的值