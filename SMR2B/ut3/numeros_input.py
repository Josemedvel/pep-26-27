import os


num_1 = input("Ingresa inicio:\t")
num_2 = input("Ingresa final:\t")
num_3 = input("Ingresa paso:\t")

try:
    num_1 = int(num_1)
    num_2 = int(num_2)
    num_3 = int(num_3)
except Exception as e:
    print("Error, no se puede transformar uno o más de los números:", e)
    os._exit(1)
    
for i in range(num_1, num_2 + 1, num_3):
    print(i)