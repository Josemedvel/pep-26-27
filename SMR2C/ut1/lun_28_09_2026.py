# ahora vamos a saludar print("asdfasf")
'''
ahora vamos a saludar
asdjflasdfa
asdfasdfasdf
asdfasdfasdf
asdfasdfasdf
'''
"""
ahora vamos a saludar
asdjflasdfa
asdfasdfasdf
asdfasdfasdf
asdfasdfasdf
"""
a = 5
print("Hola")

def imprimir_numero():
    global a
    a = 10
    print(a)
    
imprimir_numero()
print(a)
class Pelota:
    '''
    Clase Pelota, modela una pelota genérica
    '''
    def __init__(self, r, color):
        '''
        Método constructor:
        @param r: Radio de la pelota (en cm)
        @param color: Color de la pelota (en str hexadecimal, ej. "#CCC")
        '''
        self.r = r
        self.color = color
    
    def botar(self, veces):
        '''
        Método para hacer botar la pelota
        @param veces: número de veces que va a botar la pelota
        '''
        while veces > 0:
            print("Boing boing")
            veces -= 1
        
## conversiones
a = 10
a = float(a)
a += 0.5
print("Variable a: ", a, type(a))

b = int(a)
print("Variable b: ", b, type(b))

c = str(b)
print("Variable c: ", c, type(c))

parte_entera_a = int(a) # 10
resto = a - parte_entera_a # 0.5
acumulador = 0
if resto >= 0.5:
    acumulador = 1
d = parte_entera_a + acumulador # queremos que sea 11
print("Variable d: ", d, type(d))

import variables
print("principal",__name__)

