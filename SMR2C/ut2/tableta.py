from turtle import *

lado = 50
inicio = position()
print(inicio)

for l in range(1,5): # tableta
    for j in range(4): # línea
        for _ in range(4): # cuadrado
            forward(lado)
            left(90)
        forward(lado)
    teleport(inicio[0], -(lado) * l)
'''for l in range(1,5): # tableta
    for j in range(4): # línea
        print(l+j)
        if l+j % 2 == 0:
            begin_fill()
            for _ in range(4): # cuadrado
                forward(lado)
                left(90)
            end_fill()
        else:
            for _ in range(4): # cuadrado
                forward(lado)
                left(90)
        forward(lado)
    teleport(inicio[0], -(lado) * l)
    
'''
