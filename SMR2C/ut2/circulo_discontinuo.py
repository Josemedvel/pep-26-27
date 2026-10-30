from turtle import *

n = 140

lado = 800 / n
angulo = 360 / n

for i in range(n):
    if (i // 10) % 2 == 0:
        color("white")
    else:
        color("black")
    forward(lado)
    left(angulo)