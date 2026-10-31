from turtle import *

showturtle()
lado = 50
angulo = 90
inicio = position()

for x in range(1,4): # tableta
    for j in range(5): # linea
        for i in range(4): # cuadrado
            forward(lado)
            left(angulo)
        forward(lado)
    teleport(0, inicio[1]-lado*x)
