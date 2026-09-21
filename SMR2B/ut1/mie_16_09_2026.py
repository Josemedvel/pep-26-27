# variables
a = 5
b = a
b = 10

a = "adios"
print("hola mundo")
print(b)
print(a)
# tipos de datos
num_int = 40
cadena = "hola"
verdadero = True
decimal = 314E-2
print(decimal)
print("verdadero",type([]))

#constantes
HORA_SALIDA = "21:25"
HORA_SALIDA = 3
print(HORA_SALIDA)

# operadores aritméticos
#suma
suma = 4 + 7
#resta
resta = 10 - 6
#mult
mult = 3 * 2
#div
div = 31 / 3
print(div)
#div_ent
div_ent = 31 // 3
#pot
pot = 2**(0.5)
print(pot)
#modulo
mod = 17 % 5
print(mod)

num_s = 8541
horas = 8541 // 3600
minutos = (num_s - (horas * 3600)) // 60
segundos = num_s - horas * 3600 - minutos * 60
print(horas, minutos, segundos)

a = "hola"
b = 4
c = True
print(a, b, c)
print(a + " " + str(b) + " " + str(c))
print(f"{a} {b} {c}")

# reloj impreso con formato
print("%02.f : %02.f : %02.f" % (float(horas), float(minutos), float(segundos)))

#print(True == (len("True") < 10))



