import random
import config

class Enemigo:
    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y
        # Sprites para las animaciones de los enemigos.
        self.sprites = [
            (0, 1, 42, 15, 14),
            (0, 17, 57, 15, 14),
        ]
        self.sprite = self.sprites[0]
        self.disparos = []
        self.lives = config.ENEMIGOS1_LIVES
        self.speed = config.ENEMIGOS1_SPEED
        self.a = True


    def move(self, direction: str, size: int):
        '''Método que define el movimiento de un enemigo.'''

        if direction == 'up':
            self.y -= self.speed
        
        elif direction == 'down':
            self.y += self.speed
