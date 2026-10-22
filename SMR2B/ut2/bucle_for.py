for i in range(5): #[0,5)
    print(i, end="\t")
print()
for i in range(2, 7): # [2, 7)
    print(i, end="\t")
print()
'''for i in range(0, 101, 2): # [0,101) V x donde x % 2 == 0
    print(i, end="\t")
print()
'''
for i in range(10, -1, -1):
    print(i, end="\t")
print()

palabra = "Abuela"
cont_a = 0
# recorrido letra a letra
print("a" in palabra)
for l in palabra:
    if l.lower() == "a":
        cont_a = cont_a + 1
print(f"Hay un total de {cont_a} As")

# recorrido por índices de palabra
for i in range(len(palabra)):
    print(palabra[5 - i], end="\t")
print()
    
# recorrido con índices y valores
for idx, v in enumerate(palabra):
    print(idx, v)
    
for i in range(5):
    for j in range(3):
        print(i, j)
    
for i in range(11):
    for j in range(11):
        print(f"{j} x {i} = {i * j}", end="\t")
    print()
    
    