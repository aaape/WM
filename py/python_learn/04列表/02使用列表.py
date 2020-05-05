#4.9使用列表
# 为什么使用列表:为了保存一组类似的值。变量赋值可以保存一个值，使用列表可以保存多个值
#使用列表的好处：列表的数据都放在一个结构中，所以程序能更灵活的处理数据
catName = []
while True:
    print("please enter the catname "+ str(len(catName) + 1) + ':')
    name = input()
    if name == '':
        break
    catName = catName + [name]
    print(catName)
    for name in catName:
        print('' + name)


#4.10列表用于for循环
#遍历列表中的每一项，每次遍历执行一次for语句的子语句代码
supplies = ['pen','staplers', 'flame-throwers']
print(range(len(supplies)))
for i in range(len(supplies)):#加上range把3生成列表，这个时候就是[1,2,3,],for只能遍历Iterable类型
    print('index ' + str(i) + ' supplies value:' + supplies[i] )


#4.11 in 和not in 操作符
#in 和 not in：连接两个值：一个是要在列表中查找的值，另一个是带查找的列表；in和not in表达式求值为布尔类型
myPets = ['dragon', 'snake', 'whorm']
print('please input your petName')
petName = input()
#只要要值是布尔类型，就可以在控制流语句中作为条件
if petName in myPets:
    print(petName + ' that\'s my petName')
else:
    print('i don\' have a pet name ' + petName)


#4.12 多重赋值技巧
#用列表中的值为多个变量赋值
cat_c = ['fat', 'black', 'loud']
size, color, disposition = cat_c
print(size)
