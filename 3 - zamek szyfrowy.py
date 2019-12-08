# Napisz skrypt realizujący funkcję zamka szyfrowego. Prosi
# o podanie kodu i następnie sprawdza czy jest on zgodny z
# wcześniej wprowadzonym kodem


kod = input("Podaj kod: ")
print(kod)


while 1 :
    kod_1 = input("Zgaduj kod zamka szyfrowego ")
    if kod == kod_1 :
        print("Brawo! Podano prwidlowy kod.")
        break
    else :
        print("Spróbuj jeszcze raz!")
