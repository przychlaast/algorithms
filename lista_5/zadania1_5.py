import random
import time

#zadanie 1
def generator_zajec(n):
    s = [random.uniform(0, 24) for _ in range(n)]
    f = [si + random.uniform(0.5, 2) for si in s]
    
    zajecia = list(zip(s, f))
    zajecia.sort(key=lambda x: x[1])
    
    s_sorted, f_sorted = zip(*zajecia)
    s_sorted = list(s_sorted)
    f_sorted = list(f_sorted)
    
    return s_sorted, f_sorted

s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
f = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

s_test, f_test = generator_zajec(100)

#zadanie 2
def activity_selector_pd(s, f):
    n = len(f)
    pd = [0]*(n+1)
    zajecia = [[] for _ in range(n+1)]

    s = [0] + s
    f = [0] + f
    
    for i in range(1, n+1):
        pd[i] = max(pd[j] + 1 for j in range(i) if s[i] >= f[j])
        if pd[i] == pd[i-1]:
            zajecia[i] = zajecia[i-1]
        else:
            j = max(range(i), key = pd.__getitem__)
            zajecia[i] = zajecia[j] + [i]
    return zajecia[n]


print(f'Zadanie 2 - Algorytm dynamiczny: {activity_selector_pd(s, f)}') 
print(f'Zadanie 2 - Algorytm dynamiczny dla losowych 50 zajęć: {activity_selector_pd(s_test, f_test)}')

#zadanie 3
def recursive_activity_selector(s, f, k, n):
    m = k + 1
    while m <= n and s[m] < f[k]:
        m += 1
    if m <= n:
        return [k+1] + recursive_activity_selector(s, f, m, n)
    else:
        return [k+1]
    
def activity_selector(s, f):
    n = len(s)
    A = [1]
    j = 0
    for i in range(1, n):
        if s[i] >= f[j]:
            A.append(i+1)
            j = i
    return A


print(f'Zadanie 3 - Algorytm rekurencyjny: {recursive_activity_selector(s, f, 0, len(s)-1)}')
print(f'Zadanie 3 - Algorytm iteracyjny: {activity_selector(s, f)}')


print(f'Zadanie 3 - Algorytm rekurencyjny dla losowych 50 zajęć: {recursive_activity_selector(s_test, f_test, 0, len(s_test)-1)}')
print(f'Zadanie 3 - Algorytm iteracyjny dla losowych 50 zajęć: {activity_selector(s_test, f_test)}')

algorytmy = [activity_selector_pd, recursive_activity_selector, activity_selector]

print('Zadanie 3 - ')
for algorytm in algorytmy:
    if algorytm == recursive_activity_selector:
        start = time.time()
        algorytm(s_test, f_test, 0, len(s)-1)
        koniec = time.time()
    else:
        start = time.time()
        algorytm(s_test, f_test)
        koniec = time.time()
    print(f'Czas działania {algorytm.__name__}: {koniec-start}')
    
#zadanie 4
def dynamic_coin_changing(nominaly, sum):

    n = len(nominaly)
    pd = [[0]*(sum+1) for _ in range(n+1)]
    pd[0] = list(range(sum+1))

    for i in range(1, n+1):
        for j in range(0, sum+1):
            if nominaly[i-1] > j:
                pd[i][j] = pd[i-1][j]
            else:
                pd[i][j] = min(pd[i][j-nominaly[i-1]] + 1, pd[i-1][j])
    return pd[n][sum]

nominaly = [1, 5, 8, 10, 20, 50]
print(f'Zadanie 4 - Minimalna liczba monet za pomocą których możemy wydać wejściową sumę: {dynamic_coin_changing(nominaly, 100)}')


#zadanie 5
def coin_changing(nominaly, sum):
    n = len(nominaly)
    wynik = []
    for i in range(n-1, -1, -1):
        while sum >= nominaly[i]:
            sum -= nominaly[i]
            wynik.append(nominaly[i])
    return wynik

print(f'Zadanie 5 - Nominały za pomocą których możemy wydać wejściową sumę: {coin_changing(nominaly, 100)}')

nominaly_test = [1, 3, 4]
sum = 1
while True:
    if dynamic_coin_changing(nominaly_test, sum) == len(coin_changing(nominaly_test, sum)):
        sum += 1
    else:
        print("Zadanie 5 - \nDla sum =", sum)
        print("dynamic_coin_changing:", dynamic_coin_changing(nominaly_test, sum))
        print("greedy_coin_changing:", len(coin_changing(nominaly_test, sum)), coin_changing(nominaly_test, sum))
        print("Nominały dla których algorytm zachłanny nie znajduje optymalnego rozwiązania:", nominaly_test)
        break



