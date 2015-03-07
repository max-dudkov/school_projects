#!/usr/bin/env python

l = [49 ,942 , 155 ,0 ,-2 ,8]

def swap(l, n1, n2):
    c = l[n1]
    l[n1] = l[n2]
    l[n2] = c

def sort(l):
    a = 1
    n = 1
    for i in range(len(l)):
        swap_was_used = False
        for j in range(len(l) - a):
            if l[j] > l[j + 1]:
                swap(l, j, j+1)
                swap_was_used = True   
        a = a + 1       
        if not swap_was_used:
               return n
        n += 1
    return n
    
n = sort(l)
print l, n  
