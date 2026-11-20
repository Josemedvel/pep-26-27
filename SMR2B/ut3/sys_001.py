import sys
import os


ERR_NUM_PARAMS = 1

print(sys.argv)
print(len(sys.argv))
if len(sys.argv) < 3:
    print("Faltan parámetros de ejecución.")
    print("Se esperan dos números enteros.")
    print("Ej. 4 5")
    os._exit(1)
    
num_1 = sys.argv[1]
num_2 = sys.argv[2]

try:
    num_1 = int(num_1)
    num_2 = int(num_2)
    print(num_1 + num_2)
    os._exit(0)
except Exception:
    print("El formato de los números debe ser entero")
    os._exit(2)

