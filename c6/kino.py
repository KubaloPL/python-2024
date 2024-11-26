# # Opis programu rezerwacji miejsc w kinie

# ## Zadania do wykonania:

# ### 1. Wyświetlanie aktualnego stanu rezerwacji miejsc
# - **Typ danych:** lista (`seats`)
# - **Opis:** Używamy listy `seats`, która przechowuje informacje o rezerwacjach miejsc. Jeśli miejsce jest wolne, w liście znajduje 
#   się wartość `None`. Jeśli miejsce jest zarezerwowane, w liście przechowywane jest imię osoby, która je zarezerwowała.
# - **Funkcja:** `print_seats(seats)` wyświetla aktualny stan wszystkich miejsc, informując, które z nich są wolne, 
# a które są zarezerwowane oraz przez kogo.
seats = [None]*10

def print_seats(seats: list):
    for i in range(len(seats)):
        if seats[i] == None:
            print(f"Miejsce {i+1} nie jest zarezerwowane przez nikogo.")
        else:
            print(f"Miejsce {i+1} jest zarezerowawane przez {seats[i]}")

# ### 2. Dodawanie nowej rezerwacji
# - **Typ danych:** lista (`seats`), ciąg znaków (imię), liczba całkowita (numer miejsca)
# - **Opis:** Użytkownik podaje swoje imię oraz numer miejsca, które chce zarezerwować. 
# Sprawdzamy, czy numer miejsca jest poprawny (czy mieści się w zakresie 1-10) 
# i czy miejsce jest wolne (czy wartość w liście `seats` jest `None`). 
# Jeśli warunki są spełnione, zapisujemy imię użytkownika w odpowiednim indeksie listy `seats`.
# - **Funkcja:** `add_reservation(seats)` realizuje te kroki.

def add_reservation(seats: list, name: str, seatpos: int):
    seats[seatpos] = name
    print(f"Dodano {name} do rezerwacji na miejscu {seatpos+1}")

# ### 3. Usuwanie istniejącej rezerwacji
# - **Typ danych:** lista (`seats`), liczba całkowita (numer miejsca)
# - **Opis:** Użytkownik podaje numer miejsca, które chce zwolnić. Sprawdzamy, czy numer miejsca jest poprawny
#  (czy mieści się w zakresie 1-10) i czy miejsce jest zarezerwowane (czy wartość w liście `seats` nie jest `None`). 
# Jeśli miejsce jest zarezerwowane, usuwamy rezerwację, ustawiając wartość `None` w odpowiednim indeksie listy `seats`.
# - **Funkcja:** `remove_reservation(seats)` realizuje te kroki.

def remove_reservation(seats: list, seatpos: int):
    seats[seatpos] = None
    print(f"Usunięto rezerwację na miejscu {seatpos}")

# ### 4. Modyfikacja istniejącej rezerwacji
# - **Typ danych:** lista (`seats`), liczba całkowita (numer miejsca), ciąg znaków (imię)
# - **Opis:** Użytkownik podaje numer miejsca, które chce zmodyfikować. Sprawdzamy, czy numer miejsca jest poprawny oraz czy miejsce
#  jest zarezerwowane. Następnie użytkownik podaje nowy numer miejsca, na które chce przenieść rezerwację. Sprawdzamy,
#  czy nowy numer miejsca jest poprawny i czy jest wolny. Jeśli warunki są spełnione, przenosimy rezerwację na nowe miejsce,
#  ustawiając odpowiednie wartości w liście `seats`.
# - **Funkcja:** `modify_reservation(seats)` realizuje te kroki.

def modify_reservation(seats: list, seatpos: int, name: str):
    seats[seatpos] = name
    print(f"Zmodyfikowano rezerwację na miejscu {seatpos+1}, zmieniono na {name}")

# ### 5. Wyjście z programu
# - **Opis:** Użytkownik może zakończyć działanie programu wybierając opcję "5". Funkcja `main()` odpowiada za główną pętlę programu,
#  która umożliwia wybór opcji przez użytkownika i realizację poszczególnych funkcji programu.



# ## Dodatkowe informacje
# - Program wykorzystuje pętlę `while` do utrzymywania działania, dopóki użytkownik nie zdecyduje się zakończyć programu.
# - Program działa na podstawie wprowadzonych danych użytkownika i wykonuje odpowiednie operacje na liście `seats`, która przechowuje 
# stan rezerwacji miejsc w kinie.

# ## Sprint 2 - Nowe możliwości w programie

# ### 6. Sprawdzenie dostępności wielu miejsc
# - **Typ danych:** lista (`seats`), lista liczb całkowitych (numery miejsc)
# - **Opis:** Użytkownik może sprawdzić, czy wybrane miejsca są dostępne. Podaje listę numerów miejsc, a program sprawdza i informuje,
#  które z nich są wolne, a które są zarezerwowane.
# - **Funkcja:** `check_availability(seats)` realizuje te kroki.

def check_availability(seats: list, seatnums: list[int]):
    for i in seatnums:
        if not (i >= 1 and i <= 10): continue
        if seats[i] == None:
            print(f"Miejsce {i} Jest niezarezerwowane")
        else:
            print(f"Miejsce {i} Jest zarezerwowane przez {seats[i]}")



def main():
        print("Opcja 1: Wyświetlanie miejsc")
        print("Opcja 2: Dodawanie rezerwacji")
        print("Opcja 3: Usuwanie rezerwacji")
        print("Opcja 4: Modyfikacja rezerwacji")
        print("Opcja 5: Wyjście z programu")
        option = input("Wybierz opcje: ")


        if option == "1": #printing seats
            print_seats(seats)



        elif option == "2": #adding reservation
            seatpos = input("Podaj miejsce na którym chcesz dodać rezerwację: ")
            #SEATPOS VALIDATION
            if not seatpos.isnumeric():
                print(f"BŁĄD: wpisano miejsce które nie jest liczbą")
                return
            seatpos = int(seatpos)
            seatpos -= 1 #account for counting tables from 0
            if not (seatpos >= 0 and seatpos < len(seats)): 
                print(f"BŁĄD: wpisano miejsce, które nie istnieje, miejsca są dostępne od 1-{len(seats)}")
                return 
            if not (seats[seatpos] == None): 
                print(f"BŁĄD: wpisano miejsce, które jest już zarezerwowane")
                return
            #END OF SEATPOS VALIDATION
            
            name = input("Podaj nazwę osoby rezerwującej: ")
            add_reservation(seats,name, seatpos)



        elif option == "3": #removing reservation
            seatpos = input("Podaj miejsce na którym chcesz usunąć rezerwację: ")
            #SEATPOS VALIDATION
            if not seatpos.isnumeric():
                print(f"BŁĄD: wpisano miejsce które nie jest liczbą")
                return
            seatpos = int(seatpos)
            seatpos -= 1 #account for counting tables from 0
            if not (seatpos >= 0 and seatpos < len(seats)): 
                print(f"BŁĄD: wpisano miejsce, które nie istnieje, miejsca są dostępne od 1-{len(seats)}")
                return 
            if (seats[seatpos] == None): 
                print(f"BŁĄD: wpisano miejsce, które nie jest zarezerwowane")
                return
            #END OF SEATPOS VALIDATION
            remove_reservation(seats, seatpos)



        elif option == "4": #modifying reservation
            seatpos = input("Podaj miejsce na którym chcesz zmodyfikować rezerwację: ")
            #SEATPOS VALIDATION
            if not seatpos.isnumeric():
                print(f"BŁĄD: wpisano miejsce które nie jest liczbą")
                return
            seatpos = int(seatpos)
            seatpos -= 1 #account for counting tables from 0
            if not (seatpos >= 0 and seatpos < len(seats)): 
                print(f"BŁĄD: wpisano miejsce, które nie istnieje, miejsca są dostępne od 1-{len(seats)}")
                return 
            if (seats[seatpos] == None): 
                print(f"BŁĄD: wpisano miejsce, które nie jest zarezerwowane")
                return
            #END OF SEATPOS VALIDATION
            name = input("Podaj nazwę osoby rezerwującej: ")
            modify_reservation(seats, seatpos, name)


        elif option == "5":
            return "end"

while True:
    if main() == "end":
        break
    else:
        input("\nNaciśnij enter aby kontynuować...\n")
# ### 7. Rezerwacja wielu miejsc naraz
# - **Typ danych:** lista (`seats`), ciąg znaków (imię), lista liczb całkowitych (numery miejsc)
# - **Opis:** Użytkownik może dokonać rezerwacji wielu miejsc jednocześnie. Podaje swoje imię oraz listę numerów miejsc do rezerwacji. Program sprawdza, czy wszystkie podane miejsca są wolne, a jeśli tak, dokonuje rezerwacji.
# - **Funkcja:** `add_multiple_reservations(seats)` realizuje te kroki.




# ### 8. Anulowanie wszystkich rezerwacji
# - **Typ danych:** lista (`seats`), ciąg znaków (imię)
# - **Opis:** Użytkownik może anulować wszystkie swoje rezerwacje. Podaje swoje imię, a program usuwa wszystkie miejsca zarezerwowane na to imię.
# - **Funkcja:** `cancel_all_reservations(seats)` realizuje te kroki.

