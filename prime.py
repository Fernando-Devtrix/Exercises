# def get_num():
#     user_num = input("Escribe un número: ") 

# def is_prime():
#     if user_num < 1:
#         return False
#     elif user_num == 2:
#         return True
#     else:
#         for num in range(2, user_num):

# primes = []

# for x in range(1, 101):
#     counter = 0 
#     for y in range(1, x+1):
#         if x % y == 0:
#             counter += 1
#     if counter <=2:
#         primes.append(x)

# print(primes)          

def is_prime():
    user_num = int(input("Escribe un número: ")) 
    if user_num > 0:
        for x in range(2, user_num):
            update = 2
            isPrime = True
            while isPrime and update < x:
                if x % update == 0:
                    isPrime = False
                else:
                    update += 1
            if isPrime:
                print(f"{x} es primo")
    else:
        print("Ingresa un numero positivo: ")
        is_prime()

# Call Function
is_prime()