import os

num = input("Introduce el numero:")
try:
    val_int = int(num)
except Exception as e:
    print("El numero no es válido:", e)
    os._exit(-1)