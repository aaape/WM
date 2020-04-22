# import areallyourpetsnamederic
import random

num = input()
def collata(number):
    if int(number)%2 == 0:
         print(number)
    if int(number)%2 == 1:
        global B
        B = (3 * int(number) + 1)
        print(B)
collata(num)

while B != 1:
    collata(B)
# while B == 1:
#     collata(N)