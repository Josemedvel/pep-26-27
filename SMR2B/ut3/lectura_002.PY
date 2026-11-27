# lectura completa
'''
with open("el_quijote.txt", "r", encoding="utf-8") as f:
    print(f.read())
'''
# lectura de una línea
'''with open("el_quijote.txt", "r", encoding="utf-8") as f:
    linea = f.readline()
    num_l = 1
    while linea and num_l < 5:
        linea = f.readline()
        num_l += 1
    print(linea)
'''
# lectura de líneas
'''with open("el_quijote.txt", "r", encoding="utf-8") as f:
    print(f.readlines()[:20])
'''
# lectura iterativa
with open("el_quijote.txt", "r", encoding="utf-8") as f:
    num = 1
    for l in f:
        print(f"{num} - {l}")
        num += 1










