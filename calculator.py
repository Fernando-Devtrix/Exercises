def init():
    print('''

                                         Bienvenido a calculadora los Raptors

''')

def calculate():    
    user_number = input('''
Introduce el número de según la operación que deseas realizar:
 1 ) Suma
 2 ) Resta
 3 ) Multiplicación
 4 ) Division
''')

    options = ["1", "2", "3", "4"]

    if not user_number:
        print("Introduce un número")
      
     # Addition
    elif user_number == "1":
        number_1 = str(input("Escribe el primer número: "))
        number_2 = str(input("Escribe el segundo número: "))
        if not number_1 or not number_2:
            print("Campos incompletos")
        else:
            result_addition = int(number_1) + int(number_2)
            print(result_addition)

     # Substraction
    elif user_number == "2":
        number_1 = str(input("Escribe el primer número: "))
        number_2 = str(input("Escribe el segundo número: "))
        if not number_1 or not number_2:
            print("Campos incompletos")
        else:    
            result_substraction = int(number_1) - int(number_2)
            print(f"El resultado de la resta es {result_substraction}")

     # Multiplication
    elif user_number == "3":
        number_1 = str(input("Escribe el primer número: "))
        number_2 = str(input("Escribe el segundo número: "))
        if not number_1 or not number_2:
            print("Campos incompletos")
        else:    
            result_multiplication = int(number_1) * int(number_2)
            print(f"El resultado de la multiplication es {result_multiplication}")

     # Division
    elif user_number == "4":
        number_1 = str(input("Escribe el primer número: "))
        number_2 = str(input("Escribe el segundo número: "))
        if number_2 == "0":
            print("Número es dividido entre 0")
        elif not number_1 or not number_2:
            print("Campos incompletos")
        else:
            result_division = int(number_1) / int(number_2)
            print(f"El resultado de la multiplication es {result_division}")

    elif user_number != options:
        print("Tu opción esta fuera del rango, revisa porfavor")

    play_again()



def play_again():    
    start_again = input('''
¿Quieres hacer una operación de nuevo?
 Y = Yes
 N u otra tecla = No
 ''')

    if start_again == "Y" or start_again == "y":
        calculate()

    elif start_again == "N" or start_again == "n":
        print("Adiós")


   

 # Call functions
init()
calculate()

