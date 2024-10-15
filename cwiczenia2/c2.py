# import math

# print("hi")

# #zad 1 napisz program ktory przypisze do zmiennych lizbe calkowita i tekst a nastepnie wypisze te dane na ekran
# print("zad1")
# liczba = 10
# tekst = "hi"

# print("liczba: ", liczba,"tekst: ", tekst)

# #zad2 zadeklaruj zmienna z liczba zmiennoprzecinkowa i tekstem a nastepnie wpisz oba elementy w jednym ciagu znakow
# print("zad2")
# float_liczba = 0.4935
# tekst = "assdafsad"

# print("float: ", float_liczba, "tekst: ", tekst)

# #zad3 wypisz na ekranie sume dwoch liczb oraz komunikat z wynikiem w formie "suma liczb 5 i 10 wynosi 15"
# print("zad3")
# print("suma liczb",5,"i ",10,"wynosi",5+10)


#zad4 wczytaj od uzytkownika dwie liczby i oblicz ich iloczyn, roznice i iloraz

print("zad4: wczytaj od uzytkownika dwie liczby i oblicz ich iloczyn, roznice i iloraz")
num1 = input("Wpisz liczbę 1: ")
if not num1.isnumeric():
    print("ERROR: Wpisana wartość nie jest liczbą")
    exit()
num2 = input("Wpisz liczbę 2: ")
if not num2.isnumeric():
    print("ERROR: Wpisana wartość nie jest liczbą")
    exit()

num1 = float(num1)
num2 = float(num2)

print("Iloczyn: "f"{num1}*{num2} = {num1*num2}")
print("Roznica: "f"{num1}-{num2} = {num1-num2}")
if num2 == 0:
    print("ERROR: Nie można dzielić przez zero")
    exit()
print("Iloraz: "f"{num1}/{num2} = {num1/num2}")

# #zad5 wczytaj ciag znakow ktory reprezentuje liczbe zmiennoprzecinkowa, przekonwertuj go i oblicz pierwiastek kwadratowy z tej liczby

# print("zad5")
# float_liczba = float(input("wpisz float ktory chcesz zpierwiastkowac: "))
# print("pierwiastek kwadratowy z",float_liczba,"wynosi",math.sqrt(float_liczba))
# #zad6 napisz program ktory wczyta od uzytkownika tekst a nastepnie wypisze dlugosc tego tekstu
# print("zad6")

# tekst = input("podaj tekst ktorego dlugosc chcesz policzyc: ")
# print("dlugosc tekstu wynosi: ",len(tekst))

# # Zadanie 7:  Wczytaj od użytkownika słowo oraz literę, a następnie znajdź pozycję tej litery w podanym słowie. Jeśli litery nie ma, poinformuj o tym użytkownika.
# print("zad7")
# slowo = input("wpisz slowo: ")
# litera = input("wpisz litere: ")
# if (litera in slowo):
#     print("znaleziono litere w slowie na pozycji: ", slowo.rfind(litera),"(liczone od zera)")
# else:
#     print("nie znaleziono litery w slowie")

# Zadanie 8: Wczytaj od użytkownika zdanie oraz literę, anastępnie policz, ile razy dana litera występuje w zdaniu.
# print("Zadanie 8: Wczytaj od użytkownika zdanie oraz literę, a następnie policz, ile razy dana litera występuje w zdaniu.")
# zdanie = input("wpisz zdanie: ")
# litera = input("wpisz litere: ")
# if (litera in zdanie):
#     print(f"litera {litera} wystepuje {zdanie.count(litera)} razy w zdaniu")
# else:
#     print("nie znaleziono litery w zdaniu")

# # Zadanie 9: Wczytaj od użytkownika zdanie i zamień w nim wszystkie spacje na myślniki. Wypisz wynik na ekranie.

# print("Zadanie 9: Wczytaj od użytkownika zdanie i zamień w nim wszystkie spacje na myślniki. Wypisz wynik na ekranie.")
# zdanie = input("wpisz zdanie: ")
# zdanie = zdanie.replace(" ","-")
# print(zdanie)