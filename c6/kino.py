# Program do rezerwacji miejsc w kinie
from typing import Optional


seats = [None]*10

def print_seats(seats: list) -> None:
    for i in range(len(seats)):
        if seats[i] == None:
            print(f"Miejsce {i+1} nie jest zarezerwowane przez nikogo.")
        else:
            print(f"Miejsce {i+1} jest zarezerowawane przez {seats[i]}")


def add_reservation(seats: list, name: str, seatpos: int) -> None:
    seats[seatpos] = name
    print(f"Dodano {name} do rezerwacji na miejscu {seatpos+1}")


def remove_reservation(seats: list, seatpos: int) -> None:
    seats[seatpos] = None
    print(f"Usunięto rezerwację na miejscu {seatpos+1}")


def modify_reservation(seats: list, seatpos: int, name: str) -> None:
    seats[seatpos] = name
    print(f"Zmodyfikowano rezerwację na miejscu {seatpos+1}, zmieniono na {name}")


def check_availability(seats: list, seatnums: list[int]) -> None:
    for i in seatnums:
        if seats[i] == None:
            print(f"Miejsce {i+1} Jest niezarezerwowane")
        else:
            print(f"Miejsce {i+1} Jest zarezerwowane przez {seats[i]}")


def add_multiple_reservations(seats: list, seatnums: list[int], name: str) -> None:
    for i in seatnums:
        seats[i] = name
        print(f"Dodano {name} do rezerwacji na miejscu {i+1}")


def cancel_all_reservations(seats: list, name: str) -> None:
    did_anything = False
    for i in range(len(seats)):
        if seats[i] == name:
            seats[i] = None
            print(f"Usunięto rezerwację dla {name} na miejscu {i+1}")
            did_anything = True
    if did_anything == False:
        print(f"BŁĄD: {name} Nie posiada żadnych rezerwacji")


def validate_seatpos(seatpos: str) -> tuple[bool, Optional[int], Optional[str]]:
    '''
        function takes in seatpos directly from input as a string
        Returns a tuple of:
        - bool (isValid)  whether the seatpos is valid or not
        - seatpos (int)  position of the 
        - error_message (string)  if it errors
    '''

    if not seatpos.isnumeric():
        return False, None, (f"BŁĄD: wpisano miejsce które nie jest liczbą ({seatpos})")
    seatpos = int(seatpos)
    seatpos -= 1 #account for counting tables from 0
    if not (seatpos >= 0 and seatpos < len(seats)): 
        return False, None, (f"BŁĄD: wpisano miejsce, które nie istnieje ({seatpos+1}), miejsca są dostępne od 1-{len(seats)}")
    return True, seatpos, None

    

def main():
        print("Opcja 1: Wyświetlanie miejsc")
        print("Opcja 2: Dodawanie rezerwacji")
        print("Opcja 3: Usuwanie rezerwacji")
        print("Opcja 4: Modyfikacja rezerwacji")
        print("Opcja 5: Sprawdzanie dostępności wielu miejsc")
        print("Opcja 6: Dodawanie rezerwacji na wielu miejscach")
        print("Opcja 7: Usuwanie wszystkich rezerwacji danej osoby")
        print("Opcja 8: Wyjście z programu")
        option = input("Wybierz opcje: ")


        if option == "1": #printing seats
            print_seats(seats)



        elif option == "2": #adding reservation
            seatpos = input("Podaj miejsce na którym chcesz dodać rezerwację: ")
            #SEATPOS VALIDATION
            is_valid, seatpos, error_message = validate_seatpos(seatpos)
            if is_valid == False:
                print(error_message)
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
            is_valid, seatpos, error_message = validate_seatpos(seatpos)
            if is_valid == False:
                print(error_message)
                return
            
            if (seats[seatpos] == None): 
                print(f"BŁĄD: wpisano miejsce, które nie jest zarezerwowane")
                return
            #END OF SEATPOS VALIDATION
            remove_reservation(seats, seatpos)



        elif option == "4": #modifying reservation
            seatpos = input("Podaj miejsce na którym chcesz zmodyfikować rezerwację: ")
            #SEATPOS VALIDATION
            is_valid, seatpos, error_message = validate_seatpos(seatpos)
            if is_valid == False:
                print(error_message)
                return
            
            if (seats[seatpos] == None): 
                print(f"BŁĄD: wpisano miejsce, które nie jest zarezerwowane")
                return
            #END OF SEATPOS VALIDATION
            name = input("Podaj nazwę osoby rezerwującej: ")
            modify_reservation(seats, seatpos, name)



        elif option == "5": #checking availability
            seatnums = input("Podaj numery miejsc oddzielone spacją aby sprawdzić ich dostępność: ")
            seatnums = seatnums.split(" ")
            #SEATPOS VALIDATION
            seatnums2 = []
            for seatpos in seatnums:
                is_valid, seatpos, error_message = validate_seatpos(seatpos)
                if is_valid == False:
                    print(error_message)
                    return
                seatnums2.append(seatpos)
            #END OF SEATPOS VALIDATION
            check_availability(seats, seatnums2)



        elif option == "6": #adding multiple reservations
            seatnums = input("Podaj numery miejsc oddzielone spacją na których chcesz dodać rezerwację: ")
            seatnums = seatnums.split(" ")
            #SEATPOS VALIDATION
            seatnums2 = []
            for seatpos in seatnums:
                is_valid, seatpos, error_message = validate_seatpos(seatpos)
                if is_valid == False:
                    print(error_message)
                    return
                
                if not (seats[seatpos] == None): 
                    print(f"BŁĄD: wpisano miejsce, które jest już zarezerwowane ({seatpos+1})")
                    return
                seatnums2.append(seatpos)
            #END OF SEATPOS VALIDATION
            name = input("Podaj nazwę osoby rezerwującej: ")
            add_multiple_reservations(seats, seatnums2, name)



        elif option == "7": #cancelling all reservations
            name = input("Podaj nazwę osoby której chcesz usunąć wszystkie rezerwację: ")
            cancel_all_reservations(seats, name)



        elif option == "8": #exiting the program
            return "end"
        


        else: #invalid option
            print("BŁĄD: Nie znaleziono takiej opcji")
        

        
while True:
    if main() == "end":
        break
    else:
        input("\nNaciśnij enter aby kontynuować...\n")
