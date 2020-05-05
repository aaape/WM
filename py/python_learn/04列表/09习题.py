spam = [2,4,6,8,10]
spam.insert(2,'hello')
print(spam)

bpam = ['a','b','c','d']
print(int('3'*2) / 11)
print(bpam[int(int('3'* 2) / 11)])
print(bpam[-1])
print(bpam[:2])

cpam = [3.14, 'cat', 11,'cat', True ]
print(cpam[1])
cpam.append(99)#不要试图直接使用append的返回值作为值，append方法返回值为None
print(cpam)
cpam.remove('cat')
print(cpam)