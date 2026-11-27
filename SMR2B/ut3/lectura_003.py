# escribir frases con espada
'''
with open("el_quijote.txt", "r", encoding="utf-8") as f,open("frases_espadas.txt", "w", encoding="utf-8") as fw:
    for l in f:
        if "espada" in l.lower():
            fw.write(l + "\n")
'''
# numero de veces que se dice espada y muerte en la misma frase
with open("el_quijote.txt", "r", encoding="utf-8") as f:
    cont = 0
    for l in f:
        if "espada" in l.lower() and "muerte" in l.lower():
            cont += 1
    print(cont)