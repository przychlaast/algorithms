import random
import time
from math import inf

#zadanie 1
def naive_cut_rod(cena, n):
    if n == 0:
        return 0
    q = -inf
    for i in range(1, n + 1):
        q = max(q, cena[i - 1] + naive_cut_rod(cena, n - i))
    return q

def generator_pret_cena(n, max_cena):
    return [random.randint(1, max_cena) for _ in range(n)]


cennik = generator_pret_cena(50, 100)
print(f'Tablica cen: {cennik}')
print(f"Zadanie 1 - Naiwny algorytm(rekurencyjny) maksymalny zysk: {naive_cut_rod(cennik, 10)} dla losowego cennika")

cennik_test = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
print(f"Zadanie 1 - Naiwny algorytm(rekurencyjny) maksymalny zysk: {naive_cut_rod(cennik_test, 4)} dla cennika {cennik_test}")


#zadanie 2
def memorized_cut_rod(price, n):
    r = [-1] * (n + 1)
    s = [-1] * (n + 1)

    def cut_rod_aux(price, n):
        if r[n] >= 0:
            return r[n]
        if n == 0:
            q = 0
        else:
            q = -inf
            for i in range(1, n + 1):
                tym_q = price[i - 1] + cut_rod_aux(price, n - i)
                if tym_q > q:
                    q = tym_q
                    s[n] = i
        r[n] = q
        return q

    def extended_cut_rod_solution(price, n):
        if n == 0:
            return []
        return extended_cut_rod_solution(price, n - s[n]) + [s[n]]

    max_zysk = cut_rod_aux(price, n)
    optymalne_rozw = extended_cut_rod_solution(price, n)
    return max_zysk, optymalne_rozw

def print_cut_rod_solution(price, n):
    max_zysk, optymalne_rozw = memorized_cut_rod(price, n)
    for i in optymalne_rozw:
        print(i)

print(f"Zadanie 2 - Algorytm z pamięcią maksymalny zysk: {memorized_cut_rod(cennik_test, 4)}")
print(f"Zadanie 2 - Optymalne rozwiązanie: ")
print_cut_rod_solution(cennik_test, 4)

poczatek_memorized = time.time()
max_zysk, optymalne_rozw = memorized_cut_rod(cennik, 50)
koniec_memorized = time.time()
czas_memorized = koniec_memorized - poczatek_memorized

print(f"Zadanie 2 - Algorytm z pamięcią maksymalny zysk: {max_zysk}")


#zadanie 3
def cut_rod(p,n):
    r = [0] * (n + 1)
    for j in range(1, n + 1):
        q = -inf
        for i in range(1, j + 1):
            q = max(q, p[i-1] + r[j - i])
        r[j] = q
    return r[n]


def ext_cut_rod(p, n):
    r = [0] * (n + 1)
    s = [0] * (n + 1)
    for j in range(1, n + 1):
        q = -inf
        for i in range(1, j + 1):
            if q < p[i - 1] + r[j - i]:
                q = p[i - 1] + r[j - i]
                s[j] = i
        r[j] = q
    return r, s


def print_cut_rod_solution(p, n):
    r, s = ext_cut_rod(p, n)
    while n > 0:
        print(s[n])
        n = n - s[n]


print(f"Zadanie 3 - Algorytm iteracyjny maksymalny zysk: {cut_rod(cennik, 10)}")
print(f"Zadanie 3 - Optymalne rozwiązanie: ")
print_cut_rod_solution(cennik, 8)

poczatek_cut_rod = time.time()
wynik = cut_rod(cennik, 50)
koniec_cut_rod = time.time()
czas_cut_rod = koniec_cut_rod - poczatek_cut_rod


print(f"Czas działania memorized_cut_rod: {czas_memorized}")
print(f"Czas działania cut_rod: {czas_cut_rod}")



#zadanie 4
def lcs_naive(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m-1] == Y[n-1]:
        return 1 + lcs_naive(X, Y, m-1, n-1)
    else:
        return max(lcs_naive(X, Y, m, n-1), lcs_naive(X, Y, m-1, n))
    

def generator_dane_wejsciowe(n, m, k):
    X = [random.randint(1, k) for _ in range(n)]
    Y = [random.randint(1, k) for _ in range(m)]
    return X, Y

X_test, Y_test = generator_dane_wejsciowe(13, 15, 10)
print(f"Zadanie 4 - Długość najdłuższego podciągu: {lcs_naive('abcbdab', 'bdcaba', 7, 6)} dla X = {'abcbdab'} i Y = {'bdcaba'}")
print(f"Zadanie 4 - Długość najdłuższego podciągu: {lcs_naive(X_test, Y_test, len(X_test), len(Y_test))} dla X = {X_test} i Y = {Y_test}")


#zadanie 5
def memorized_lcs(X, Y):
    m = len(X)
    n = len(Y)
    cache = [[-1] * (n + 1) for _ in range(m + 1)]

    def lcs(X, Y, i, j):
        if cache[i][j] != -1:
            return cache[i][j]
        if i == 0 or j == 0:
            result = 0
        elif X[i-1] == Y[j-1]:
            result = 1 + lcs(X, Y, i-1, j-1)
        else:
            result = max(lcs(X, Y, i, j-1), lcs(X, Y, i-1, j))
        cache[i][j] = result
        return result

    return lcs(X, Y, m, n)

print(f"Zadanie 5 - Długość najdłuższego podciągu: {memorized_lcs('abcbdab', 'bdcaba')} dla X = {'abcbdab'} i Y = {'bdcaba'}")
print(f"Zadanie 5 - Długość najdłuższego podciągu: {memorized_lcs(X_test, Y_test)} dla X = {X_test} i Y = {Y_test}")

#zadanie 6
def lcs_iteracyjnie(X, Y):
    m = len(X)
    n = len(Y)
    L = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    index = L[m][n]
    lcs_rozw = [''] * (index+1)
    lcs_rozw[index] = ''

    i = m
    j = n
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs_rozw[index-1] = X[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1

    return L[m][n], ''.join(map(str, lcs_rozw))


print(f"Zadanie 6 - Optymalne rozwiązanie: {lcs_iteracyjnie(X_test, Y_test)} dla X = {X_test} i Y = {Y_test}")
print(f"Zadanie 6 - Optymalne rozwiązanie: {lcs_iteracyjnie('sanie', 'basi')} dla X = {'sanie'} i Y = {'basi'}")

