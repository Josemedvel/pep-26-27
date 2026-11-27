with open("frases.txt", "a", encoding="utf-8") as f:
    frase = input("Ingresa algo para guardar:\t")
    while frase.strip().lower() != "fin":
        f.write(frase.strip() + "\n")
        frase = input("Ingresa algo para guardar:\t")
        
