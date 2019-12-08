# Napisz skrypt usuwający z wejściowego ciągu tekstowego
# (wybierz kilka plików z repozytorium: Tekstowego) następujące
# słowa : się, i, oraz, nigdy, dlaczego


input = open('tekst.txt', "r")
line = input.read()

zamiana = {'tekstowy.': ' ', 'Ma': 'uuu', ' nigdy ': ' ', ' dlaczego ': ' '}
for j, l in zamiana.items():
    line = line.replace(j, l)
with open('test2.txt', 'w') as input:
    input.write(line)