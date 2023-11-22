import matplotlib.pyplot as plt
import time
import random

A = [10, 33, 2, 3, 27, 13, 5, 7]

#zadanie 1
def heapsort(A):
    build_heap(A)
    rozmiar_kopca = len(A)
    for i in range(rozmiar_kopca-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        rozmiar_kopca = rozmiar_kopca - 1
        heapify(A, 0, rozmiar_kopca)
    return A

def build_heap(A):
    rozmiar_kopca = len(A)
    for i in range(rozmiar_kopca//2-1, -1, -1):
        heapify(A, i, rozmiar_kopca)
    return A

def heapify(A, i, rozmiar_kopca):
    l = 2*i + 1
    r = 2*i + 2
    if l < rozmiar_kopca and A[l] > A[i]:
        najwiekszy = l
    else: 
        najwiekszy = i
    if r < rozmiar_kopca and A[r] > A[najwiekszy]:
        najwiekszy = r
    if najwiekszy != i:
        A[i], A[najwiekszy] = A[najwiekszy], A[i]
        heapify(A, najwiekszy, rozmiar_kopca)
    return A


print(f'Heapsort: {heapsort(A)}')



def heapsort_plus(A):
    przypisania, porownania = 0, 0
    A, przypisania, porownania = build_heap_plus(A, przypisania, porownania)
    rozmiar_kopca = len(A)
    for i in range(rozmiar_kopca-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        przypisania += 2
        rozmiar_kopca -= 1
        A, przypisania, porownania = heapify_plus(A, 0, rozmiar_kopca, przypisania, porownania)
    return A, przypisania, porownania

def build_heap_plus(A, przypisania, porownania):
    rozmiar_kopca = len(A)
    for i in range(rozmiar_kopca//2-1, -1, -1):
        A, przypisania, porownania = heapify_plus(A, i, rozmiar_kopca, przypisania, porownania)
    return A, przypisania, porownania

def heapify_plus(A, i, rozmiar_kopca, przypisania, porownania):
    l = 2*i + 1
    r = 2*i + 2
    przypisania += 2
    if l < rozmiar_kopca and A[l] > A[i]:
        najwiekszy = l
        porownania += 2
    else: 
        najwiekszy = i
        porownania += 1
    if r < rozmiar_kopca and A[r] > A[najwiekszy]:
        najwiekszy = r
        porownania += 2
    if najwiekszy != i:
        A[i], A[najwiekszy] = A[najwiekszy], A[i]
        przypisania += 2
        A, przypisania, porownania = heapify_plus(A, najwiekszy, rozmiar_kopca, przypisania, porownania)
    return A, przypisania, porownania

print(f'Heapsort plus: {heapsort_plus(A)}')


#zadanie 2
def heapsort3(A):
    build_heap3(A)
    rozmiar_kopca = len(A)
    for i in range(rozmiar_kopca-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        rozmiar_kopca = rozmiar_kopca - 1
        heapify3(A, 0, rozmiar_kopca)
    return A

def build_heap3(A):
    rozmiar_kopca = len(A)
    for i in range((rozmiar_kopca//3)-1, -1, -1):
        heapify3(A, i, rozmiar_kopca)

def heapify3(A, i, rozmiar_kopca):
    l = 3*i + 1
    m = 3*i + 2
    r = 3*i + 3
    najwiekszy = i
    if l < rozmiar_kopca and A[l] > A[najwiekszy]:
        najwiekszy = l
    if m < rozmiar_kopca and A[m] > A[najwiekszy]:
        najwiekszy = m
    if r < rozmiar_kopca and A[r] > A[najwiekszy]:
        najwiekszy = r
    if najwiekszy != i:
        A[i], A[najwiekszy] = A[najwiekszy], A[i]
        heapify3(A, najwiekszy, rozmiar_kopca)

print(f'Heapsort3: {heapsort3(A)}')


def heapsort3_plus(A):
    przypisania, porownania = 0, 0
    A, przypisania, porownania = build_heap3_plus(A, przypisania, porownania)
    rozmiar_kopca = len(A)
    for i in range(rozmiar_kopca-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        przypisania += 2
        rozmiar_kopca -= 1
        A, przypisania, porownania = heapify3_plus(A, 0, rozmiar_kopca, przypisania, porownania)
    return A, przypisania, porownania

def build_heap3_plus(A, przypisania, porownania):
    rozmiar_kopca = len(A)
    for i in range(rozmiar_kopca//3, -1, -1):
        A, przypisania, porownania = heapify3_plus(A, i, rozmiar_kopca, przypisania, porownania)
    return A, przypisania, porownania

def heapify3_plus(A, i, rozmiar_kopca, przypisania, porownania):
    l = 3*i + 1
    m = 3*i + 2
    r = 3*i + 3
    przypisania += 3
    najwiekszy = i
    if l < rozmiar_kopca and A[l] > A[najwiekszy]:
        najwiekszy = l
        porownania += 2
    if m < rozmiar_kopca and A[m] > A[najwiekszy]:
        najwiekszy = m
        porownania += 2
    if r < rozmiar_kopca and A[r] > A[najwiekszy]:
        najwiekszy = r
        porownania += 2
    if najwiekszy != i:
        A[i], A[najwiekszy] = A[najwiekszy], A[i]
        przypisania += 2
        A, przypisania, porownania = heapify3_plus(A, najwiekszy, rozmiar_kopca, przypisania, porownania)
    return A, przypisania, porownania

print(f'Heapsort3 plus: {heapsort3_plus(A)}')


#zadanie 3
def quicksort(A, p, k):
    if p < k:
        s = partition(A, p, k)
        quicksort(A, p, s-1)
        quicksort(A, s+1, k)
    return A

def partition(A, p, k):
    x = A[k]
    granica = p - 1
    for j in range(p, k):
        if A[j] <= x:
            granica += 1
            A[j], A[granica] = A[granica], A[j]
    A[granica+1], A[k] = A[k], A[granica+1]
    return granica + 1

print(f'Quicksort: {quicksort(A, 0, len(A)-1)}')
    

def quicksort_plus(A, p, k, przypisania=0, porownania=0):
    if p < k:
        s, przypisania, porownania = partition_plus(A, p, k, przypisania, porownania)
        A, przypisania, porownania = quicksort_plus(A, p, s-1, przypisania, porownania)
        A, przypisania, porownania = quicksort_plus(A, s+1, k, przypisania, porownania)
    return A, przypisania, porownania

def partition_plus(A, p, k, przypisania, porownania):
    x = A[k]
    granica = p - 1
    przypisania += 2
    for j in range(p, k):
        porownania += 1
        if A[j] <= x:
            granica += 1
            A[j], A[granica] = A[granica], A[j]
            przypisania += 2
    A[granica+1], A[k] = A[k], A[granica+1]
    przypisania += 2
    return granica + 1, przypisania, porownania

print(f'Quicksort plus: {quicksort_plus(A, 0, len(A)-1)}')

#zadanie 4
def quicksort3(A, p, k):
    if p < k:
        granica1, granica2 = partition3(A, p, k)
        quicksort3(A, p, granica1 - 1)
        quicksort3(A, granica2 + 1, k)
    return A

def partition3(A, p, k):
    x = A[k]
    granica1 = p
    granica2 = k
    i = p
    while i <= granica2:
        if A[i] < x:
            A[i], A[granica1] = A[granica1], A[i]
            i += 1
            granica1 += 1
        elif A[i] > x:
            A[i], A[granica2] = A[granica2], A[i]
            granica2 -= 1
        else:
            i += 1
    return granica1, granica2

print(f'Quicksort3: {quicksort3(A, 0, len(A)-1)}')


def quicksort3_plus(A, p, k, przypisania=0, porownania=0):
    if p < k:
        granica1, granica2, przypisania, porownania = partition3_plus(A, p, k, przypisania, porownania)
        A, przypisania, porownania = quicksort3_plus(A, p, granica1 - 1, przypisania, porownania)
        A, przypisania, porownania = quicksort3_plus(A, granica2 + 1, k, przypisania, porownania)
    return A, przypisania, porownania

def partition3_plus(A, p, k, przypisania, porownania):
    x = A[k]
    granica1 = p
    granica2 = k
    i = p
    przypisania += 4
    while i <= granica2:
        porownania += 1
        if A[i] < x:
            A[i], A[granica1] = A[granica1], A[i]
            i += 1
            granica1 += 1
            porownania += 1
            przypisania += 2
        elif A[i] > x:
            A[i], A[granica2] = A[granica2], A[i]
            granica2 -= 1
            porownania += 1
            przypisania += 2
        else:
            i += 1
    return granica1, granica2, przypisania, porownania

print(f'Quicksort3 plus: {quicksort3_plus(A, 0, len(A)-1)}')

#zadanie 5
def test_algorytmu(algorytm, nazwa_algorytmu):
    rozmiary = [100, 500, 1000, 5000]
    czasy = []
    lista_porownan = []
    lista_przypisan = []
    for rozmiar in rozmiary:
        A = [random.randint(-10000, 10000) for x in range(rozmiar)]
        poczatek = time.time()
        if 'quicksort' in nazwa_algorytmu:
            x, przypisania, porownania = algorytm(A, 0, len(A)-1)
        else:
            x, przypisania, porownania = algorytm(A)
        koniec = time.time()
        czasy.append(koniec - poczatek)
        lista_porownan.append(porownania)
        lista_przypisan.append(przypisania)

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 3, 1)
    plt.plot(rozmiary, czasy, 'o-')
    plt.title('Czas')
    plt.xlabel('Wielkość danych')
    plt.ylabel('Czas [s]')

    plt.subplot(1, 3, 2)
    plt.plot(rozmiary, lista_porownan, 'o-')
    plt.title('Porównania')
    plt.xlabel('Wielkość danych')
    plt.ylabel('Liczba porównań')

    plt.subplot(1, 3, 3)
    plt.plot(rozmiary, lista_przypisan, 'o-')
    plt.title('Przypisania')
    plt.xlabel('Wielkość danych')
    plt.ylabel('Liczba przypisań')

    plt.tight_layout()
    plt.savefig(f'{nazwa_algorytmu}.pdf')


algorytmy = [heapsort_plus, heapsort3_plus, quicksort_plus, quicksort3_plus]

for algorytm in algorytmy:
    nazwa_algorytmu = algorytm.__name__
    test_algorytmu(algorytm, nazwa_algorytmu)
