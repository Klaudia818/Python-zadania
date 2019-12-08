# Napisz skrypt obliczający wartość iloczynu dwóch wektorów:
# a = [1, 2, 12, 4], b = [2, 4, 2, 8], tzw. iloczyn skalarny wektorów

from functools import reduce

a = [1,2,12,4]
b = [2,4,2,8]
a_b = []
#print(a_b)
for i in range(len(a)):
    a_b.append(a[i] * b[i])
#print (a_b)
def suma(x,y):
    return x+y
print(reduce(suma, a_b))
