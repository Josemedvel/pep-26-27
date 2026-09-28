jugada = "piedra"
jugada_maq = "papel"

if jugada == jugada_maq: # empate
    print("Empate")
elif jugada == "piedra" and jugada_maq == "tijeras":
    print("Gano")
elif jugada == "papel" and jugada_maq == "piedra":
    print("Gano")
elif jugada == "tijeras" and jugada_maq == "papel":
    print("Gano")
else:
    print("Pierdo")