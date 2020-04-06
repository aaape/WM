h = 1.75
w = 82.5

x = w/h
if x < 18.5:
    print('过轻')
elif 18.5 < x <25:
    print('normal')
elif 25 < x < 28 :
    print('too heavy')
elif 28 < x < 32 :
    print('fat')
else :
    print('too fat')
