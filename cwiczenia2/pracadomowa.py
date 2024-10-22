import re

# Zadanie 1: Przetwarzanie tekstu i analizy statystyczne
# Napisz program, który:
#     Pobiera od użytkownika wieloliniowy tekst.
#     Wypisuje liczbę słów, zdań (przyjmując, że zdania kończą się kropką), oraz średnią długość słowa (w znakach).
#     Sprawdza, czy podane słowo występuje w tekście. Jeśli tak, wypisuje liczbę jego wystąpień oraz pozycje (indeksy) w tekście.
# Podaj tekst: "Python jest fajny. Uczymy się Pythona."
# Podaj szukane słowo: "Python"

# tekst = input("""wpisz tekst: """)
tekst = "Python jest fajny. Uczymy się Pythona. XD."
szukane_slowo = "Python"
tekst.strip()
zdania = tekst.split(".")
slowa = tekst.split(" ")

srednia_dlugosc = 0
for slowo in slowa:
    srednia_dlugosc += len(slowo)

srednia_dlugosc = srednia_dlugosc / len(slowa)

print(f"liczba zdan: {len(zdania)-1}")

print(f"liczba slow: {len(slowa)}")

print(f"srednia dlugosc slow: {srednia_dlugosc}")
znalezione_slowo = tekst.count(szukane_slowo)

if znalezione_slowo:
    indeksy = [m.start() for m in re.finditer(szukane_slowo, tekst)]
    print(f"slowo {szukane_slowo} wystepuje w tekscie: {znalezione_slowo} razy na indeksach: {indeksy}")
else:
    print(f"slowo {szukane_slowo} nie wystepuje w tekscie")