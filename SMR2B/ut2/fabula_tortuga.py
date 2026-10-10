p_tortuga = 0
p_liebre = 0
num = 1
while True:
    p_tortuga = p_tortuga + 2
    if num % 7 == 0:
        p_liebre = p_liebre + 8
    print("Posicion tortuga: " + str(p_tortuga))
    print("Posicion liebre: " + str(p_liebre))
    num = num + 1