'''Generowanie liczb za pomocą petli Filip Adamus ID_33'''

import random
import time

def genenumery(n):
    numery = []
    for i in range(n):
        numery.append(random.randint(1, 100))
    return numery

def genenumery_while(n):
    numery = []
    i = 0
    
    while i < n:
        numery.append(random.randint(1, 100))
        i += 1
    return numery

sizes = [100000, 316000, 1000000]

for size in sizes:
    
    start_time = time.time()
    genenumery(size)
    end_time = time.time()
    print(f"Pętla for: {size} danych - czas: {end_time - start_time:.5f} s")

    start_time = time.time()
    genenumery_while(size)
    end_time = time.time()
    print(f"Pętla while: {size} danych - czas: {end_time - start_time:.5f} s")
