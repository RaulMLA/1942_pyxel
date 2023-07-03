from config import *

class Shot:
    def __init__(self, x: int, y: int, tipo: str, direction: str):
        '''Inicialización del shot.'''
        self.x = x
        self.y = y

        # Sprites para las animaciones de los disparos.
        self.sprites = [
            (0, 1, 18, 11, 10),
            (0, 13, 18, 4, 4)
        ]
        self.sprite = self.sprites[0] if tipo == 'plane' else self.sprites[1]
        self.speed = ENEMIES_SHOTS if tipo == 'enemy' else PLAYER_SHOTS
        self.direction = direction


    def move (self):
        '''Método que define el movimiento de un shot.'''

        # Movimientos lineales.
        if self.direction == 'down':
            self.y += self.speed
        elif self.direction == 'up':
            self.y -= self.speed
        elif self.direction == 'left':
            self.x -= self.speed
        elif self.direction == 'right':
            self.x += self.speed
        
        # Movimientos diagonales.
        elif self.direction == 'upleft':
            self.x -= 0.6
            self.y -= self.speed
        elif self.direction == 'upright':
            self.x += 0.6
            self.y -= self.speed
        elif self.direction == 'downleft':
            self.x -= 0.6
            self.y += self.speed
        elif self.direction == 'downright':
            self.x += 0.6
            self.y += self.speed
