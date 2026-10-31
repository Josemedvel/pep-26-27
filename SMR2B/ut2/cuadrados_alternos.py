from turtle import *

showturtle()
lado = 50
angulo = 90
begin_fill()
for j in range(4):
    if j % 2 == 0:
        for i in range(4): # cuadrado
            forward(lado)
            left(angulo)
    else:
        for i in range(4): # cuadrado
            forward(lado)
            right(angulo)
    forward(lado)
end_fill()