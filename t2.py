__author__ = 'max'
a = int(input())
b = 1
result = []
while b <= a:
    if b % 3 == 0:
        if b % 7 != 0:
            result += (b, b)
        else:
            result.append(b)
    if b % 3 != 0:
        if b % 7 != 0:
            result.append(b)
    b += 1

print(' '.join((str(x) for x in result)))
