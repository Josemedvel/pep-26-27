fin = False
contador = 0
suma_parcial = 0.0

while not fin:
    numero_str = input("Ingresa el numero:\t")
    try:
        numero = float(numero_str)
        contador += 1
        suma_parcial += numero
    except:
        if numero_str.strip().lower() == "fin":
            fin = True
if contador == 0:
    print("No se puede calcular la media sin números")
else:
    with open("resultado_media.txt", "w", encoding="utf-8") as f:
        f.write(f"{(suma_parcial / contador):.2f} \n")
