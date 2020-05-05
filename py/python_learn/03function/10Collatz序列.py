# import areallyourpetsnamederic
import random

num = input()
def collata(number):
    if int(number)%2 == 0:
        A = (number / 2)
        return number
    elif int(number)%2 == 1:
        B = 3 * int(number) + 1
        return B
C = collata(num)
print(C)
while C != 1:
    collata(collata())