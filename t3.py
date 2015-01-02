__author__ = 'max'
b = 0
c = 1
for s in open('turns'):
    s = int(s)
    b += s
    if b < 100:
        c += 1
if c % 2 == 0:
    print('ENDER')
else:
    print('VALENTINE')
