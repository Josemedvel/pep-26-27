import sys
import os

args = sys.argv
argc = len(args)

if argc != 4:
    print("Número erróneo de parámetros, se espera {inicio, final, paso}")
    os._exit(-1)
    
inicio = args[1]
final = args[2]
paso = args[3]

try:
    inicio = int(inicio)
    final = int(final)
    paso = int(paso)
except Exception as e:
    print("El formato de los parámetros debe ser entero", e)
    os._exit(-2)

for i in range(inicio, final+1, paso):
    print(i)
    