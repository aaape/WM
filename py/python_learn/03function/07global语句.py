#global，修改函数内的局部变量为全局变量

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
#执行流程，定义spam函数，全局变量eggs赋值为global，调用spam函数：把函数体局部作用域内的eggs变量修改为全局变量
#将局域作用域内的全局变量eggs赋值为spam。这时全局变量eggs指向spam，执行打印函数print

# 1．如果变量在全局作用域中使用（即在所有函数之外），它就总是全局变量。
# 2．如果在一个函数中，有针对该变量的global语句，它就是全局变量。
# 3．否则，如果该变量用于函数中的赋值语句，它就是局部变量。
# 4．但是，如果该变量没有用在赋值语句中，它就是全局变量。

def spam():
    global eggs
    eggs = 'spam'
def bacon():
    eggs = 'bacon'
def ham():
    print(eggs)

eggs = 42
spam()
print(eggs)

def spam():
    global eggs
    print(eggs)

eggs = 'global'
spam()