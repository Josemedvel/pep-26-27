import os
import sys

parametros = sys.argv

if len(parametros) < 2:
    print("Es necesario poner como parámetros las notas de los exámenes")
    print("Ej. python calculo_media_sysargv.py 5 7.6 9")
    os._exit(1)

n = 0
notas_acc = 0

for nota in parametros[1:]:
    try:
        valor_nota = float(nota)
        if valor_nota < 0 or valor_nota > 10:
            raise Exception()
        notas_acc += valor_nota
        n += 1
    except ValueError as e:
        print("Hay una nota que no es válida")
        print("Tiene que ser un número decimal:", nota)
        os._exit(2)
    except Exception as e:
        print("Hay una nota que no es válida")
        print("El valor de una nota debe estar entre 0 y 10")
        os._exit(3)

print(f"La media de las notas es: {(notas_acc / n):.3f}")
    
    