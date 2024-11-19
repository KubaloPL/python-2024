import math

def suma(x,y):
    return x+y

print(suma(2,5))

def pole_kola(r: float) -> float:
    """
    Funkcja licząca pole koła
    """
    print(type(r))
    return math.pi * r**2

print(f"Pole koła wynosi: {pole_kola(5)}")

def witaj(imie:str, powitanie:str = "Cześć") -> str:
    return(f"{powitanie}, {imie} jesteś na PW")

print(witaj(powitanie="Hej", imie="Kuba"))

def silnia(n:int) -> int:
    if n == 0:
        return 1
    return n * silnia(n-1)

print(silnia(5))

def pi()->float:
    return 3.14

print(pi())


def suma_wielu(*args)->int:
    return sum(args)

print(suma_wielu(3,4,6,7,3,2,5))


# funkcja filtrująca liczby parzyste (in: lista) wy: lista

def filtruj_parzyste(liczby:list[int]) -> list[int]:
    return [num for num in liczby if num % 2 == 0]

print(filtruj_parzyste([53,52,54,55,56]))