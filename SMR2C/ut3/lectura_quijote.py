# readline()
'''
with open("hola.txt", "r", encoding="utf-8") as f:
    line = f.readline()
    num_l = 1
    while line:
        print(f"{num_l}-{line}")
        line = f.readline()
        num_l += 1
'''
# readlines
'''
with open("el_quijote.txt", "r", encoding="utf-8") as f:
    lineas = f.readlines()
    print(lineas)
'''
# iteracion
with open("el_quijote.txt", "r", encoding="utf-8") as f, :
    contador = 0
    for l in f:
        if "espada" in l.lower():
            contador += 1
    print(contador)
    

    