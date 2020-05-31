import unittest
from BSTestRunner import BSTestRunner
import sys
import time

#sys.path 当我们导入一个模块时：import  xxx，默认情况下python解析器会搜索当前目录、已安装的内置模块和第三方模块，搜索路径存放在sys模块的path中
#当我们要添加自己的搜索目录时，可以通过列表的append()方法
sys.path.append(r"D:\WM\appium_learn\Test_frame")
test_dir = "../test_case"
report_dir = "../report"

unittest.defaultTestLoader.discover(test_dir,pattern='tes*.py')

now = time.strftime('%Y-%M-%D %h_%m_%s')
report_name = report_dir + now + 'test_report.html'

