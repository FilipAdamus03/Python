''' F A id_33 bubbleSort'''

from random import randint
from time import time

A = [randint(1,1000) for id_33 in range(3000)]
B = sorted(A.copy())
t0=time()

sw = True; gap = len(A)
while sw :
    sw = False
    if gap > 1 : gap = gap*10//13
    for i in range(gap,len(A)):
        if A[i-gap] > A[i]:
            A[i-gap],A[i] = A[i], A[i-gap]
            sw = True
            
if A == B: print('To działa. CZAS:', time()-t0)
