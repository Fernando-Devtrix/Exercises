def is_even():
    user_number = float(input("Introduce el número: "))

    if user_number % 2 == 0:
        print(f"{user_number} es par")
    else:
        print(f"{user_number} es impar")

    play_again()

def play_again():    
    start_again = input('''
¿Quieres ingresar un número de nuevo?
 Y = Yes
 N = No
 ''')

    if start_again == "Y" or start_again == "y":
        is_even()

    elif start_again == "N" or start_again == "n":
        print("Adiós")

is_even()
