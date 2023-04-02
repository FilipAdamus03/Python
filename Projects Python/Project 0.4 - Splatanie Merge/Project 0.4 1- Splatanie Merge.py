'''Splatanie / Merge'''

import random
from bisect import bisect_left, insort_left
from heapq import merge

lista1= sorted([random.randint(1,100) for i in range(10)])
lista2= sorted([random.randint(1,100) for i in range(10)])

lista3 = list(merge(lista1, lista2))

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista 3 (po scaleniu):", lista3)
