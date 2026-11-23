with open("hola.txt", "r", encoding="utf-8") as f:
    print(f.read())
with open("adios.txt", "w", encoding="utf-8") as f:
    f.write(input("Ingresa tu despedida:\t"))

    