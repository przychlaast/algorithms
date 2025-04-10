import time
import random
import numpy as np


#zadanie 1
def insertion_sort(A: np.ndarray) -> np.ndarray:
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key
    return A

test = insertion_sort([5.1, 2.2, 4.3, 6.4, 1.5, 3.6])
print(f"Insertion-sort: {test}")


#zadanie 2
def insertion_sort_plus(A: np.ndarray) -> np.ndarray:
    liczba_przypisan = 0
    liczba_porownan = 0
    for j in range(1, len(A)):
        key = A[j]
        liczba_przypisan += 1
        i = j - 1
        while i >= 0:
            liczba_porownan += 1
            if A[i] > key:
                A[i+1] = A[i]
                liczba_przypisan += 1
                i = i - 1
            else:
                break
        A[i+1] = key
        liczba_przypisan += 1
    return A, liczba_porownan, liczba_przypisan

test = insertion_sort_plus([5, 2, 4])
print(f"Insertion-sort-plus: {test}")

#zadanie 3
def bubble_sort(A: np.ndarray) -> np.ndarray:
    for i in range(0,len(A)-1):
        for j in range(0, len(A)-i-1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
    return A

test = bubble_sort([5, 2, 4, 6, 1, 33])
print(f"Bubble-sort: {test}")


def bubble_sort_plus(A: np.ndarray) -> np.ndarray:
    liczba_przypisan = 0
    liczba_porownan = 0
    for i in range(0,len(A)-1):
        for j in range(0, len(A)-i-1):
            liczba_porownan += 1
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                liczba_przypisan += 2
    return A, liczba_porownan, liczba_przypisan

test = bubble_sort_plus([5, 2, 4, 6, 1, 33])
print(f"Bubble-sort-plus: {test}")


#zadanie 4
def merge(A: np.ndarray, p, s, k) -> np.ndarray:
    L = A[p-1:s]
    R = A[s:k]
    L.append(np.inf)
    R.append(np.inf)
    i = 0
    j = 0
    for l in range(p-1, k):
        if L[i] <= R[j]:
            A[l] = L[i]
            i = i + 1
        else:
            A[l] = R[j]
            j = j + 1

def merge_sort(A: np.ndarray, p, k) -> np.ndarray:
    if p < k:
        s = (p+k)//2
        merge_sort(A, p, s)
        merge_sort(A, s+1, k)
        merge(A, p, s, k)
    return A

test = merge_sort([3, 2, 4, 6, 1, 5], 1, 6)
print(f"Merge-sort: {test}")


def merge_plus(A: np.ndarray, p, s, k ) -> np.ndarray:
    L = A[p-1:s]
    R = A[s:k]
    L.append(np.inf)
    R.append(np.inf)
    i = 0
    j = 0
    liczba_porownan = 0
    liczba_przypisan = 0
    for l in range(p-1, k):
        liczba_porownan += 1
        if L[i] <= R[j]:
            A[l] = L[i]
            i = i + 1
            liczba_przypisan += 1
        else:
            A[l] = R[j]
            j = j + 1
            liczba_przypisan += 1
    return A, liczba_porownan, liczba_przypisan

def merge_sort_plus(A: np.ndarray, p, k) -> np.ndarray:
    liczba_porownan = 0
    liczba_przypisan = 0
    if p < k:
        s = (p+k)//2
        A, liczba_porownan1, liczba_przypisan1 = merge_sort_plus(A, p, s)
        A, liczba_porownan2, liczba_przypisan2 = merge_sort_plus(A, s+1, k)
        A, liczba_porownan3, liczba_przypisan3 = merge_plus(A, p, s, k)
        liczba_porownan = liczba_porownan1 + liczba_porownan2 + liczba_porownan3
        liczba_przypisan = liczba_przypisan1 + liczba_przypisan2 + liczba_przypisan3
    return A, liczba_porownan, liczba_przypisan


test = merge_sort_plus([3, 2, 4, 6, 1, 5], 1, 6)
print(f"Merge-sort-plus: {test}")


#zadanie 5
def merge_sort21(A: np.ndarray, p, k) -> np.ndarray: 
    if p < k:
        s = p + 2*(k-p)//3
        merge_sort(A, p, s)
        merge_sort(A, s+1, k)
        merge(A, p, s, k)
    return A

test = merge_sort21([3, 2, 4, 6, 1, 5], 1, 6)
print(f"Merge-sort21: {test}")


def merge_sort21_plus(A: np.ndarray, p, k) -> np.ndarray:
    liczba_porownan = 0
    liczba_przypisan = 0
    if p < k:
        s = p + 2*(k-p)//3
        A, liczba_porownan1, liczba_przypisan1 = merge_sort21_plus(A, p, s)
        A, liczba_porownan2, liczba_przypisan2 = merge_sort21_plus(A, s+1, k)
        A, liczba_porownan3, liczba_przypisan3 = merge_plus(A, p, s, k)
        liczba_porownan = liczba_porownan1 + liczba_porownan2 + liczba_porownan3
        liczba_przypisan = liczba_przypisan1 + liczba_przypisan2 + liczba_przypisan3
    return A, liczba_porownan, liczba_przypisan

test = merge_sort21_plus([3, 2, 4, 6, 1, 5], 1, 6)
print(f"Merge-sort21-plus: {test}")

#zadanie 6
def test_alg(algorytmy):
    wyniki = []
    macierz = []
    rozmiar = 1000
    for liczba in range(rozmiar):
        macierz.append(random.randint(1, 1000000))
    for algorytm in algorytmy:
        poczatek = time.time()
        if algorytm in [merge_sort_plus, merge_sort21_plus]:
            x, liczba_porownan, liczba_przypisan = algorytm(macierz.copy(), 1, len(macierz))
        else:
            x, liczba_porownan, liczba_przypisan = algorytm(macierz.copy())
        koniec = time.time()
        czas_dzialania = koniec - poczatek
        wyniki.append([czas_dzialania, liczba_porownan, liczba_przypisan])
    return wyniki

algorytmy = [insertion_sort_plus, bubble_sort_plus, merge_sort_plus, merge_sort21_plus]


test = test_alg(algorytmy)
print(test)
for algorytm, index in zip(algorytmy, range(len(algorytmy))):
    print(algorytm.__name__, test[index])

