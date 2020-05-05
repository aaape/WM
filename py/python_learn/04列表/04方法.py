# 4.1
#方法：和函数一回事，函数有它的功能，方法也有其功能
#每种数据类型都有它自己的一组方法，如列表数据类型有增apend（），删removel()，查index()，改操作列表的方法
# appen和insert，sort的返回值是None，因为使用该方法列表被立马修改；PS：可变和不可变数据类型
#======================================================

#4.2index（）方法查找列表中的值
 #index()方法可以传入一个值，如果该值存在于列表中，就返回它这个值的下标；如果查找值不在列表中，报ValueError错误
spam = ['hello', 'hi','bonjour','heyas']
print(spam.index("hello"))
spam.index('bonjour')

#如果列表中存在重复的值，就返回第一次出现的下标
aka = ['up side down','up side down']
print(aka.index('up side down'))

# ==========================================

# 4.3使用append()和insert()方法
#append():将传入到append的参数，作为列表的值添加到列表末端
dogs = ['general','president','master']
dogs.append('sir')
print(dogs)
#insert(index，vlaue):参数一：插入值的下标；参数二：插入值；
walch = ['water','chemical']
walch.insert(1,'bottom')
print(walch)
# appen和insert的返回值是None，因为使用该方法列表被立马修改;PS：可变和不可变数据类型

#=====================================================

#4.4使用remove(）方法从列表中删除值
#remove()传入一个列表中的值，这个值将从被调用的列表中删除；试图删除列表中不存在的值会报错
Edifier = ['woods','line','electric']
Edifier.remove('woods')
print(Edifier)

#使用sort()方法将列表的值排序、
#sort()可以将数字列表的值按大小进行正反向的排序；将字母列表的值按ASCII字符顺序进行正反向的排序
num = [1,5,2,8,-3]
str = ['apple','banana','cell','dog','even']
num.sort()
str.sort()
num.sort(reverse=True)
str.sort(reverse=True)
print(num)
print(str)

#不要写num = num.sort()这样的代码，试图记录返回值
#不能对既有数字又有字符串的列表排序
#sort()方法对字符串排序时，按ASCII字符顺序排序；如果需要按字母顺序排序使用。关键字参数key=str.lower

