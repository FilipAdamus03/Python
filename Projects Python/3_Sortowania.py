'''Filip Adamus'''

from random import randint
from time import time

A = [randint(1,10000) for i in range(5)]
D=A.copy()
D.sort()
t0= time()

B = [randint(1,10000) for i in range(5)]
E=B.copy()
E.sort()
t0= time()

C = [randint(1,10000) for i in range(5)]
F=C.copy()
F.sort()
t0= time()

print("Sortowanie wyboru:")
print("")
print(A)

def wybIn(A):
    for i in range(len(A)):
        mn = i
        for j in range(i, len(A)):
            if A[j]<A[mn] : mn = j
        A[i], A[mn] = A[mn],A[i]
    return B
    
wybIn(A)
print(A)

if A == D : print ("Czas obliczen:",time()-t0)

print("")
print("Sortowanie bąbelkowe:")
print("")
print(B)

def bubble(B):
    for i in range(len(B)):
        for j in range(1,len(B) - i):
            if B[j-1] > B[j]:
                B[j-1], B[j] = B[j], B[j-1]

bubble(B)
print(B)

if B == E : print ("Czas obliczen:",time()-t0)

print("")
print("Sortowanie wstawiania:")
print("")
print(C)

def wstaw(C):
    for i in range(1,len(C)):
        klo=C[i]; j = i - 1
        while j>=0 and C[j]>klo :
            C[j+1]=C[j]
            j -= 1
        C[j+1] = klo

wstaw(C)
print(C)
        
if C == F : print ("Czas obliczen:",time()-t0)
