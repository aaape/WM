#Iterable:可迭代对象。
# 一：集型数据类型，list tuple dict string set ;
# 二：gernertor，包括generator和 generator function
# ****使用instance(args,interable)**********

# 被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# ************使用instance(args, interator)判别是否为interator类型********
# generator都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator

# 把非Iterator的Iterable对象，转成Iterator对象，用iter()方法进行转换