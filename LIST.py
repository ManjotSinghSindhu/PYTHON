# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 08:37:45 2018

@author: Manjot singh
"""

lst=[10,20,'manjot',-10,30.5]
print(lst)
print(lst[3])
print(lst[3:5])
print(lst*4)
print(len(lst))

lst.append('40')
print(lst)

lst.remove('40')
print(lst)

del(lst[1])

lst.insert(3,99)

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)
