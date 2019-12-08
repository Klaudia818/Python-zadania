# Zdefiniuj klasę reprezentującą liczby zespolone (wraz z funkc-
# jami na nich działającymi np. dodawanie, odejmowanie itd.)

import numpy

class ComplexNumber:   #klasa
    def __init__(self, re, im):     #  init - konstruktor klasy, sel - odnosze sie do samego siebie
        self.numberRe = re
        self.numberIm = im

    def __add__(self, other):
        return ComplexNumber(other.numberRe + self.numberRe, other.numberIm + self.numberIm)

    def __sub__(self, other):
        return ComplexNumber(self.numberRe - other.numberRe, self.numberIm - other.numberIm)

    def __str__(self):
        return str(self.numberRe) + "+" + str(self.numberIm) + "i"


x = ComplexNumber(2,4)
y = ComplexNumber(8,10)
print(x)
print(y)

print(x + y)
print(x - y)
