# Napisz skrypt obliczający pierwiastki równania kwadratowego
# w postaci : y = ax2+bx+c. Wejściem skryptu są wartości: a, b, c


print('Obliczanie pierwiastkow rownania kwadratowego:');
a = float(input('Podaj a:'));
b = float(input('Podaj b:'));
c = float(input('Podaj c:'));
delta = (b*b)-4*a*c;

if delta < 0 :
    print("Rownanie nie ma rozwiazania ");
elif delta ==0 :
    print("Delta rowna 0, rozwiazanie to:  ");
    x_0 = -b / (2 * a);
    print(x_0);
else :
    print("Rownania wynosza: ");
    x_1 = (-b - delta) / (2 * a);
    x_2 = (-b + delta) / (2 * a);
    print(x_1, x_2);