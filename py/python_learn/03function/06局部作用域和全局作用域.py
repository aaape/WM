# 在函数内赋值的变元和变量，比如参数,函数体的变量，处于函数的局部作用域
# 局部变量-局部作用域内的变量
# 全局变量-全局作用域内的变量
# 任一变量必是以上两种变量中的一种

# 局部作用域的形成：当一个函数被调用，就创建了一个局部作用域。在这个函数内赋值的所有变量都是局部变量


# 作用域的作用
# 全局作用域中的代码 不能使用任何一个局部作用域内的变量
# 局部作用域可以使用全局变量
# 一个局部作用域内的代码，不能使用其它局部作用域中的变量
# 在不同作用域中，可以使用相同的名字命名不同的变量


#Python有不同的作用域，而不是让所有东西都成全局变量，这是有理由的。这样一来，当特定函数调用中的代码修改变量时，该函数与程序其他部分的交互，只能通过它的参数和返回值。这缩小了可能导致缺陷的代码作用域。如果程序只包含全局变量，又有一个变量赋值错误的缺陷，那就很难追踪这个赋值错误发生的位置。它可能在程序的任何地方赋值，而你的程序可能有几百到几千行！但如果缺陷是因为局部变量错误赋值，你就会知道，只有那一个函数中的代码可能产生赋值错误。

#要注意作用域的销毁，作用域内的变量也会一起销毁
