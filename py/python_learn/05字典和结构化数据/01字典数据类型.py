#5.1字典
#字典和列表比较，相同点：都是许多值得集合；不同点：不像列表得下标，字典得索引可以使用许多不同数据类型，不只是整数。
#字典的结构：{'键':'值'，...........}
myCat = {'size':'fat','color':'grey'}
#访问字典的值
print(myCat['size'])
#字典可以使用数字作为键，就像列表使用整数作为下标，但不必从0开始，也可以时任何数
goods = {10086 : 'ak47', 3.1415 : '圆周率'}
print(goods[3.1415])

#5.1.1字典与列表
#两个列表是否相等：列表的值是否一致，列表值得顺序是否一致
#两个字典是否相等：列表的键对值是否一致，键对值顺序可以不一致
spam = [1,2,3,4]
bacon = [4,3,2,1]
print(spam == bacon)
maps = {1:4,2:3}
nocab = {2:3,1:4}
print(maps == nocab)
#因为字典时不排序的，所以不能像列表那样切片；访问字典的值，直接使用键就可以查询；使用不存在的键进行查询，会报keyerror


# 5.1.2keys()、values()和items()方法
# 有三个字典方法，它们返回类似列表的值
# key():返回字典的键；value():返回字典的值；item()：返回字典的键-值对
#以上三种方法，返回的值不是真正的列表，返回值不能被修改，不能使用append()。
#以上三种方法，返回的数据可以用与for循环，它们时Iterable

JRC = {'clean': 1, 'circle': 2 }
for v in JRC.values():
    print(v)
for k in JRC.keys():
    print(k)
for i in JRC.items():#item()方法返回值时键和值的元组
    print(i)
# 如果希望得到到一个真正的列表，可以通过list()方法处理以上三种方法的返回值
A = list(JRC.keys())
B = list(JRC.values())
C = list(JRC.items())
print(A)
print(B)
print(C)

#利用多重赋值技巧，用for循环把字典中的键和值分别赋给不同的变量
# for K, v in dict.items():
#     print()

#==========================================================================================

# 5.1.3 检查字典中是否存在键或值
#使用in 或 not in可以检查某个键或值是否存在于字典中
judes = {'ju':'朱', 'de' : '迪', 's' : '思' }
print('ju' in judes)
print('迪' in judes.values())

#==============================================================================================

#5.1.4get()方法
# get(键,备用值): get方法取传入键的值作为返回值，如果键不存在，返回备用值;如果没有备用值，返回默认值：0
panic = {'the':'hard','dest':'part'}

#5.1.5setdefault()方法
#dict.setdefault(key,value):serdefault方法第一个参数时要检查的值，第二个参数是值，如果该键不存在时第二个参数作为要设置的值，如果该键存在就返回该键的值
water = {'value' : '2', 'cap' : '500ml'}
water.setdefault('color','white')
print(water)
water.setdefault('color','black')
print(water)
# 作用：