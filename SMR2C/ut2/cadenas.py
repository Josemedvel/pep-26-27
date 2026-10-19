palabra = "tomate"

print(palabra[2]) # m
print(palabra[-3]) # a
print(palabra[1:4]) # oma
print(palabra[::2]) # tmt
print(palabra[::-2]) # eao

# for in
for l in palabra:
    print(l, end="\t")
print()

# for con índices
for i in range(len(palabra)):
    print(palabra[i], end="\t")
print()

# for con dos variables (índice, valor)
for i, l in enumerate(palabra):
    print(i, l)
