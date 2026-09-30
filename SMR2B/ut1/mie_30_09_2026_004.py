class Pelota:
    '''
    Representa una pelota de un radio 'r' y un color 'color'
    '''
    def __init__(self, r, color):
        '''
        Constructor de Pelota
        :param r: radio de la pelota (en cm)
        :param color: color externo de la pelota (en tupla RGB)
        '''
        self.r = r
        self.color = color
        
    def botar(self, n):
        '''
        Bota la pelota n veces
        :param n: número de veces que bota
        '''
        for i in range(n):
            print("Boiiing Boiiing")
            
    def __str__(self):
        return f"Pelota de {self.r} cm de radio y color {self.color}"
p = Pelota(15, (255,0,0))
print(p)
