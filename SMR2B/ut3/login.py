import os

contra = ""
with open("password.txt", "r", encoding="utf-8") as f:
    contra = f.read().strip()

num_max_intentos = 3
intento = 1
while intento <= num_max_intentos:
    prueba_contra = input("Ingresa la contraseña:\t").strip()
    if prueba_contra == contra:
        print("Estas dentro")
        os._exit(0)
    else:
        print(f"Te quedan ({num_max_intentos - intento}) intentos")
        intento += 1
print("Cuenta bloqueada!")
os._exit(1)

