import time
import random
from math import floor

#zadanie1
def countingsort(A, miejsce, podstawa):
    B = [0] * len(A)
    C = [0] * podstawa
    for i in range(len(A)):
        index = (A[i] // miejsce)
        C[index % podstawa] += 1
    for i in range(1, podstawa):
        C[i] += C[i-1]
    for i in range(len(A)-1, -1, -1):
        index = (A[i] // miejsce)
        B[C[index % podstawa] - 1] = A[i]
        C[index % podstawa] -= 1
    for i in range(len(A)):
        A[i] = B[i]

def radixsort(A, podstawa):
    max_wart = max(A)
    miejsce = 1
    while max_wart // miejsce > 0:
        countingsort(A, miejsce, podstawa)
        miejsce *= podstawa
    return A

print(f'Radixsort: {radixsort([123, 456, 789, 321, 654, 987, 345, 678], 10)}')


def porownaj_czasy_radix(n, podstawy):
    wyniki = []
    for podstawa in podstawy:
        A = [random.randint(0, 1000) for _ in range(n)]
        start = time.time()
        radixsort(A, podstawa)
        koniec = time.time()
        czas = koniec - start
        wyniki.append(f"Podstawa {podstawa} - czas: {czas}")
    return wyniki

print(porownaj_czasy_radix(100000, [2, 10, 16]))


#zadanie2
def bucketsort(A):
    n = len(A)
    B = [[] for _ in range(n)]
    for i in range(n):
        B[floor(n*A[i])].append(A[i])
    for i in range(n):
        B[i] = insertion_sort(B[i])
    k = 0
    for i in range(n):
        for j in range(len(B[i])):
            A[k] = B[i][j]
            k += 1
    return A

def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    return A

print(f'Bucketsort: {bucketsort([0.19, 0.15, 0.31, 0.11, 0.84, 0.38, 0.12, 0.47, 0.91, 0.32])}')

algorytmy = [bucketsort, radixsort, insertion_sort]

for algorytm in algorytmy:
    A = [random.random() for _ in range(10000)]
    start = time.time()
    if algorytm == bucketsort or algorytm == insertion_sort:
        algorytm(A)
    else:
        algorytm(A, 10)
    koniec = time.time()
    czas = koniec - start
    print(f"test {algorytm.__name__} - czas: {czas}")