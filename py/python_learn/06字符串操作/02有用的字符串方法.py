#6.2.1 upper() lower() isupper() islower()
spam = 'hello, World'
print(spam.upper())#字符串全部转换为大写,返回转换后得字符串，所以可以在这方法后面再加上操作字符串得方法
print(spam.lower())#字符串全部转换为小写
print(spam.islower())#判断字符串是否全是大写
print(spam.isupper())#判断字符串是否全是小写
#这些方法不会改变原字符串的值，如果向改变得：
spam = spam.upper()
print(spam)
spam.lower().upper()


#6.2.2 is* 字符串方法
VC = 'Vitamin '
print(VC.isalpha())#如果字符串只包含字母，并且非空；返回True
print(VC.isalnum())#如果字符串有且仅有含字母和数字，并且非空；返回True
print(VC.isdecimal())#如果字符串只包含数字字符，并且非空；返回True
print(VC.isspace())#如果字符串只包含空格、制表符和换行，并且非空；返回True

# while True:
#     print('enter your age')
#     ak = input()
#     if ak.isdecimal():
#         print('your age is:' + ak)
#         break;
#     else:
#         print('please enter the right num')
#
# while True:
#     print('please enter your password')
#     pw = input()
#     if pw.isalnum():
#         print('that\'s your password' + pw)
#         break
#     else:
#         print("please enter the right password")

#6.2.3 字符串startswith()和endswith()方法
#传入该方法得字符串，如果是调用该法的字符串的开头或者解为；返回True
print('exit'.startswith('e'))
print('exit_1'.endswith('1'))
print('exit'.startswith('exit'))
print('exit'.endswith('exit'))

#6.2.4 字符串join() 和 split()方法
#join()方法：字符串可以调用该方法，该方法的参数为一个字符串列表，该方法返回值是一个字符串
print(','.join(['a','b','c']))
print('abc'.join(['a','b', 'c']))
print(' '.join(['a','b','c']))
# 请注意，调用join()方法的字符串，被插入到列表参数中每个字符串的中间

#split()方法：把调用的字符串分解成一个字符串列表;参数就是分割符
print('my name is tommy'.split('y'))

#6.2.5 用r just() \ l just() 和center()方法对齐文本
#rjust()和lJust()方法：返回调用该方法字符串的填充版本，通过插入空格来对其文本;
#第一个参数为插入空格的个数(int)，第二个参数为可选参数，指定一个填充字符取代空格
print('skr'.rjust(10,'.'))
print('skrsssssssss'.rjust(10,'.'))
print('skr'.ljust(10))
print('skr'.rjust(20))
print('skr'.rjust(20,'s'))
#center()方法：让文本居中
print('skr'.center(10))#左5右5
#场景：
def printpicnic(itemsDict,leftWidth,rightWidth):
    print('picnic items'.center(leftWidth + rightWidth, '-'))
    for k,v in itemsDict.items():
        print(k.ljust(leftWidth,'.') + str(v).rjust(rightWidth))
picnicItems = {'sandwiches' : 4, 'banana': 12, 'cups': 6,'cookies' : 8000}
printpicnic(picnicItems,12,5)

#6.2.6用strip()、rstrip()、lscrip()删除空白字符
#返回一个新的字符串，该字符串的开头和结尾没有空白字符
blanks = ' this is th e new shit '
print(blanks)
print(blanks.strip())
#有一个可选字符串参数，指定两边的哪些字符串应该删除,直到第一个或最后一个非参数中的字母
spam = 'spamspamspamBaconSpamEggsSPamSpam'
print(spam.strip('spma'))

#6.2.7用pyperclip模块拷贝粘贴字符串
# pyperclip模块的copy和paste函数，可以向计算机的剪贴板发送文本
# import pyperclip
# pyperclip.copy('abc')
# print(pyperclip.paste())