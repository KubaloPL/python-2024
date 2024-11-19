# Zadanie 1:
# Napisz program, który wyświetli liczby od 1 do 50. Dla liczb podzielnych przez 3 zamiast liczby wyświetl "Fizz", dla liczb podzielnych przez 5 wyświetl "Buzz", a dla liczb podzielnych jednocześnie przez 3 i 5 wyświetl "FizzBuzz".
# for i in range(1,51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     if i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)



# Zadanie 2:
# Napisz program, który dla liczby n podanej przez użytkownika (n ≥ 1) wygeneruje tabliczkę mnożenia o rozmiarze n x n.

# n = input("Podaj liczbe n dla ktorej chcesz wygenerowac tabliczke mnozenia: ")
# n = int(n)
# if n >= 1:
#     for i in range(1,n+1):
#         rows = []
#         for j in range(1,n+1):
#             rows.append(i*j)
#         print(rows)
# else:
#     print("Błąd: n musi byc wieksze lub rowne 1")

# Zadanie 3:

# Poproś użytkownika o wprowadzenie listy liczb całkowitych dodatnich oddzielonych spacjami. Następnie wyświetl wykres słupkowy z gwiazdek reprezentujący te liczby.

# nums = input("Podaj liste liczb calkowitych oddzielonych spacjami: ")
# nums = nums.split(" ")
# print("Wykres:")
# for num in nums:
#     graph = ""
#     num = int(num)
#     for i in range(num):
#         graph += "*"
#     print(graph)

# Zadanie 4:

# Napisz program, który znajdzie i wyświetli wszystkie liczby Armstronga w zakresie od 100 do 999.

# for i in range(100,1000):
#     digits = str(i)
#     armstrongSum = 0
#     for j in range(len(digits)):
#         digit = int(digits[j])
#         armstrongSum += pow(digit,3)
#     if armstrongSum == i:
#         print(armstrongSum)

# Pętle while

# **Suma cyfr liczby**
#    - Napisz program, który poprosi użytkownika o wprowadzenie liczby całkowitej. Oblicz i wyświetl sumę cyfr tej liczby, używając pętli `while`.

# n = input("wprowadz liczbe calkowita ")
# total = 0
# while len(n) > 0:
#     if n[0].isdigit() == True:
#         total += int(n[0])
#     n = n[1:]

# print(f"suma cyfr tej liczby: {total}")



# **Suma liczb dodatnich**
#  Poproś użytkownika o podawanie liczb całkowitych. Dodawaj podane liczby, dopóki użytkownik nie wpisze liczby ujemnej. Gdy to zrobi, wyświetl sumę wszystkich liczb dodatnich.

# n = "1"
# numbers = []
# total = 0
# while n.isdigit() == True:
#     n = input("wprowadź liczby dodatnie, gdy wpiszesz liczbę ujemną program wypisze sumę: ")
#     if int(n) > 0:
#         numbers.append(int(n))
#     else:
#         break

# for num in numbers:
#     total += num

# print(f"suma cyfr tej liczby: {total}")