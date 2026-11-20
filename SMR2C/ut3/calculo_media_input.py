import os
# número de notas
n = input("Ingresa el número de exámenes:")
try:
    n = int(n)
    if n < 1:
        raise ValueError()
except ValueError:
    print("El valor de número de exámenes debe ser un entero positivo")
    os._exit(1)

nota_acc = 0

for i in range(n):
    nota = input(f"Ingresa la nota del examen {i}:")
    try:
        nota = float(nota)
        if nota < 0 or nota > 10:
            raise ValueError()
        nota_acc += nota
    except:
        print("La nota debe ser un número decimal entre 0 y 10")
        os._exit(2)

print(f"La nota media es de: {nota_acc / n}")
    
    
    
    
    
    
    