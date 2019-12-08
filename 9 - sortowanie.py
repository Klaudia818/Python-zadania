# Napisz skrypt sortujący liczby malejąco. Wygeneruj losowo 50
# liczb - wykorzystąj standardową funkcje do losowania. Z wbudowanej
# funkcji sortującej korzystaj tylko w celu weryfikacji wyników


import random

liczby = []
for k in range(50):
    liczby.append(random.randint(1, 50))
print(liczby)

liczby_sort = liczby
liczby_sort.sort()
print(liczby_sort)

# def sortuj(liczby):
for i in range(len(liczby)):
    j = len(liczby) - 1
    while j>i:
        if liczby[j] < liczby[j-1]:
            tmp = liczby[j]
            liczby[j] = liczby[j - 1]
            liczby[j - 1] = tmp
        j -= 1

print(liczby)