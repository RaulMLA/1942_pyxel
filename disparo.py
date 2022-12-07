import config

class Disparo:
    def __init__(self, x: int, y: int):
        '''Inicialización del disparo.'''
        self.x = x
        self.y = y
        self.sprite = (1, 3, 6, 16, 16)
    
    
    def move (self, direccion):
        '''Método que define el movimiento de un disparo.'''

        if direccion == 'down':
            self.y += 3
        else:
            self.y -=3
