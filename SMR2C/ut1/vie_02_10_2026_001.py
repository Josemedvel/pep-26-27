'''
a = 10
print(a)

def imprimeA():
    a = 5
    print(a)

def imprimeAGlobal():
    print(a)

imprimeA()
imprimeAGlobal()
print(a)

if a > 10:
    h = 10
'''
class Campeon:
    '''
    Representa un campeón del LoL
    '''
    def __init__(self, nombre, vida_inicial, df, dm, arm):
        '''
        Construye un campeón
        :param nombre: Nombre del campeón (str)
        :param vida_inicial: Puntos de vida con los que empieza la partida (int)
        :param df: Puntos de daño físico con los que empieza la partida (int)
        :return: Un objeto de tipo Campeon
        '''
        self.nombre = nombre
        self.vida_inicial = vida_inicial
        self.df = df
        self.dm = dm
        self.arm = arm
    def __str__(self):
        return f"Campeón {self.nombre}: \nVI:{self.vida_inicial}\nDaño físico:{self.df}"

def saludar(persona):
    '''
    Saluda a la persona "persona"
    :param persona: Persona a la que vamos a saludar (str)
    '''
    print("hola "+ str(persona))
print(__name__)

if __name__ == "__main__":
    saludar("Manuel")
