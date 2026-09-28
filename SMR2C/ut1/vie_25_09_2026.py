edad = 16
if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 16:
    print("No eres mayor, pero puedes salir")
else:
    print("Eres menor de edad")
    
    
jugada_maquina = "papel"
jugada = "tijeras"

'''
## forma larga
if jugada_maquina == "tijeras" and jugada == "piedra":
    print("Gana humano")
elif jugada_maquina == "piedra" and jugada == "tijeras":
    print("Gana máquina")
elif jugada_maquina == "piedra" and jugada == "papel":
    print("Gana humano")
elif jugada_maquina == "papel" and jugada == "piedra":
    print("Gana máquina")
elif jugada_maquina == "piedra" and jugada == "piedra":
    print("Empate")

'''

## forma algo más corta
if jugada_maquina == jugada:
    print("Empate")
elif jugada == "piedra" and jugada_maquina == "tijeras":
    print("Ganas")
elif jugada == "tijeras" and jugada_maquina == "papel":
    print("Ganas")
elif jugada == "papel" and jugada_maquina == "piedra":
    print("Ganas")
else:
    print("Pierdes")

import random

numeros = {
    1: '''
        -----------
        |         |
        |         |
        |    o    |
        |         |
        |         |
        -----------
        ''',
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6:6,
}
print(numeros[random.randint(1,6)])
print(int(random.random()*6 + 5))
amigas = ["Ana", "Maria", "Jimena", "Marta", "Paula"]
print(random.choice(amigas))
print(random.choices(amigas, k=2))
print(random.randrange(0,101,3))

# bucles
i = 10
while i > 0:
    print(i)
    i -= 1


# pares hasta 100
i = 0
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1
    
while i <= 100:
    print(i)
    i += 2

# divisores de n
n = 64
div = 1
while div <= n:
    if n % div == 0:
        print(div)
    div += 1






