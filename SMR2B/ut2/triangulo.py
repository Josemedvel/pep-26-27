from turtle import *

showturtle()

lado = 100
angulo = 60
for j in range(6):
    for i in range(3): # triangulo
        forward(lado)
        left(180 - angulo)
    forward(lado)
    left(angulo)
