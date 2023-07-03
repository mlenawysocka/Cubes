import random

ciezka_liczba = random.randrange(1, 7)
print(ciezka_liczba)


def rzut_krzywa_kostka() -> int:
    los = random.randrange(0, 7)
    if los == 0:
        return ciezka_liczba
    return los


# ROZWIAZANIE ZA POMOCA TYLKO LISTY

wystapienia = []
wyniki = []
for i in range(0, 1000):
    wynik = rzut_krzywa_kostka()
    wyniki.append(wynik)
wyniki.sort()

for scianka in range(1, 7):
    ilosc_wyrzutow = wyniki.count(scianka)
    wystapienia.append(ilosc_wyrzutow)

najwiecej_wystapien = max(wystapienia)
najciezsze_oczko = wystapienia.index(najwiecej_wystapien) + 1

print(wyniki)
print(wystapienia)
print(najciezsze_oczko)

# ROZWIAZANIE DICTAMI

wyniki = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
}
for i in range(0, 1000):
    wynik = rzut_krzywa_kostka()
    wyniki[wynik] += 1

s = sorted(wyniki.items(), key=lambda x: x[1], reverse=True)
print(wyniki)
print(s[0][0])
