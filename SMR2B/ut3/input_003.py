import os

num_1 = input("Ingresa un numero:")
num_2 = input("Ingresa otro numero:")

try:
    num_1 = int(num_1)
    num_2 = int(num_2)
    print(num_1 + num_2)
    os._exit(0)
except ValueError:
    print("Los números deben ser enteros")
    os._exit(1)

    