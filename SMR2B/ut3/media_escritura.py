suma = 0
contador = 0

fin = False

while not fin:
    num_cadena = input("Ingresa número:\t")
    try:
        numero = float(num_cadena)
        contador += 1
        suma += numero
    except:
        if num_cadena.strip() == "fin":
            fin = True
if contador != 0:
    print(suma/contador)
    with open("resultado_media.txt", "w", encoding="utf-8") as f:
        f.write(f"{(suma/contador):.2f}")
else:
    print("No hay numeros")
