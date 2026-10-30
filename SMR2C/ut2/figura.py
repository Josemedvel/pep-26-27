from turtle import *

n = 70

lado = 800 / n
angulo = 360 / n

for _ in range(n):
    forward(lado)
    left(angulo)
