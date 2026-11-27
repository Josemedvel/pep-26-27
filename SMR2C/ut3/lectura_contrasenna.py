import os
password = ""
with open("password.txt", "r", encoding="utf-8") as f:
    password = f.read().strip()

intento = 1
max_intentos = 3

while intento <= max_intentos:
    prueba_contra = input("Ingresa la contraseña:\t").strip()
    if prueba_contra == password: # acierto
        print("Estás dentro")
        os._exit(0)
    intento += 1
    print(f"Has fallado, te quedan ({max_intentos + 1 - intento}) intentos")
print("Cuenta bloqueada")
os._exit(1)