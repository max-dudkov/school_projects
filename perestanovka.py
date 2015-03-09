__author__ = 'max'


def swap_char(l, a1, a2):
    c = l[a1]
    l[a1] = l[a2]
    l[a2] = c


def reverse_list(l):
    if len(l) < 2:
        return l
    i1 = 0
    i2 = len(l) - 1

    while i1 < len(l) / 2:
        swap_char(l, i1, i2)
        i1 += 1
        i2 -= 1

    return l


assert reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]
assert reverse_list([1, 2, 3]) == [3, 2, 1]
assert reverse_list([1]) == [1]
assert reverse_list([]) == []