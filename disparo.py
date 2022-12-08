from config import *

class Disparo:
    def __init__(self, x: int, y: int):
        '''Inicialización del disparo.'''
        self.x = x
        self.y = y
        # Sprites para las animaciones de los disparos.
        self.sprites = [
            (0, 1, 18, 11, 10)
        ]
        self.sprite = self.sprites[0]
    
    def move (self, direccion):
        '''Método que define el movimiento de un disparo.'''

        if direccion == 'down':
            self.y += DISPARO_SPEED
        elif direccion == 'up':
            self.y -= DISPARO_SPEED
        elif direccion == 'left':
            self.x -= DISPARO_SPEED
        elif direccion == 'right':
            self.x += DISPARO_SPEED
