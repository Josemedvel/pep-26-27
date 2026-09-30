print("hola")
a = 10
b = 15
c = a + b
print(c)
if c > 25:
    print("adios")
def imprimirA():
    a = 5
    print(a)
def modificarAGlobal():
    global a
    a = 30
imprimirA()
modificarAGlobal()
print(a)