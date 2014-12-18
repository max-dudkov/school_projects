__author__ = 'max'

b = None

for s in open('min.in', 'r'):
    s = int(s)
    if b is None or b > s:
        b = s
print(b)
