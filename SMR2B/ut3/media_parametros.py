import os
import sys

if len(sys.argv) < 2:
    print("Faltan las notas")
    os._exit(1)
    
n = len(sys.argv) - 1
nota_acumulada = 0

for i in range(1, len(sys.argv)):
    nota = sys.argv[i]
    try:
        nota = float(nota)
        if nota < 0 or nota > 10:
            raise Exception("Las notas no pueden valer menos de 0 o más de 10")
        nota_acumulada += nota
    
    except ValueError:
        print("No se puede convertir una de las notas")
        os._exit(2)
    except Exception as e:
        print(e)
        os._exit(3)

print(nota_acumulada/n)

