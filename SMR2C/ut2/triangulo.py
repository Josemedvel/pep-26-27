from turtle import *

lado = 60
angulo = 180 / 3
inicio = position()


for i in range(1,7):
    for _ in range(3): # triangulo
        forward(lado)
        left(180-angulo)
    forward(lado)
    left(angulo)
