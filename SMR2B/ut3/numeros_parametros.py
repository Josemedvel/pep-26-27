import os
import sys

print(sys.argv)

if len(sys.argv) < 4:
    print("Faltan parámetros")
    os._exit(1)

try:
    inicio = int(sys.argv[1])
    final = int(sys.argv[2])
    paso = int(sys.argv[3])
except ValueError as e:
    print("No se ha podido convertir un número:\t", e)
    os._exit(2)

for i in range(inicio, final + 1, paso):
    print(i)

