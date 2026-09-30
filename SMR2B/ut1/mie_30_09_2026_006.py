a = 10.1
print(int(a))
#a = "10.1"
print(int(a))
a = False
print(int(a))
nota = 4.3

nota_redondeada = int(nota)
parte_decimal = nota - nota_redondeada
print(nota_redondeada)
print(parte_decimal)
if parte_decimal >= 0.5:
    nota_redondeada = nota_redondeada + 1
print(nota_redondeada)

texto = "numero :"+ str(3.14)
print(texto)

pi = "3.14"
print("pi", type(pi), "pi transformado", type(float(pi)), float(pi))
pi = "314e-2"
print("pi", type(pi), "pi transformado", type(float(pi)), float(pi))

sueldo_profesor = 9_000.54
print(sueldo_profesor)
texto_sueldo = str(sueldo_profesor)
print(texto_sueldo)
print(float("9_000.54"))
print(bool("Adios"))
print(bool(""))
print(bool(None))
print(bool(3))
print(bool(-3))
