distancia_tortuga = 0
distancia_liebre = 0
i = 0

while True:
    distancia_tortuga = distancia_tortuga + 2
    print("Posición tortuga:" + str(distancia_tortuga))
    if i % 7 == 0:
        distancia_liebre = distancia_liebre + 15
    print("Posición liebre:" + str(distancia_liebre))
