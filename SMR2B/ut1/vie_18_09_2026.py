#operadores relacionales
print(4 < 10)
print(5 >= 2)
print(3 == 3.0)
print(0.3 == 0.30000000004)
lista = [1,2,3]
print(2 not in lista)
print("Javier" in lista)
print("z" in "casa")

print("_" * 45)

# condicional if
edad = 18
if edad >= 18:
    print("eres mayor de edad")
elif edad >= 16:
    print("tienes permiso para salir")
else:
    print("eres menor de edad")

dia_semana = "Martes"

match dia_semana:
    case "Lunes" | "Martes" | "Miércoles" | "Jueves" | "Viernes":
        print("Laborable")
    case _:
        print("Festivo")


jugada = "piedra"
jugada_maquina = "papel"


        



