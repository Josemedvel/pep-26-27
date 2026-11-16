from turtle import *

showturtle()
lado_o = 40
lado = lado_o
angulo = 120

for i in range(15):
    forward(lado) 
    left(angulo)
    lado += lado_o
    