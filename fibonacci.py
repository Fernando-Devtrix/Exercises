# a, b = 0, 1

# while b < 10:
#     print(b)
#     a, b = b, a+b

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n-1) + fibonacci(n-2)

for x in range(1,11):
    print(x, ":", fibonacci(x))