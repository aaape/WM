import os
#os.path.dirname(__file__)输出当前py文件的绝对路径去掉文件名
#os.path.dirname(os.path.dirname(__file__))os.path.dirname去掉
#os.path.dirname()去掉括号内路径的最后一层然后输出
print(os.path.dirname(__file__))
print(os.path.dirname(os.path.dirname(__file__)))