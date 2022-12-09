import random
import config

class Enemigo:
    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y
        self.tipo = None
        self.direction = None

        # Sprites para las animaciones de los enemigos.
        self.sprites_bank = [
            (0, 1, 42, 15, 14),
            (0, 17, 42, 15, 14),
            (0, 33, 42, 15, 14),
            (0, 49, 42, 15, 14),

            (0, 1, 57, 15, 14),
            (0, 17, 57, 15, 14),
            (0, 33, 57, 15, 14),
            (0, 49, 57, 15, 14),

            (0, 1, 42, 15, 14),
            (0, 17, 42, 15, 14),
            (0, 33, 42, 15, 14),
            (0, 49, 42, 15, 14),

            (0, 17, 57, 15, 14),
            (0, 17, 57, 15, 14),
            (0, 17, 57, 15, 14),
            (0, 17, 57, 15, 14),

            (0, 1, 42, 15, 14),
            (0, 17, 42, 15, 14),
            (0, 33, 42, 15, 14),
            (0, 49, 42, 15, 14),

            (0, 17, 57, 15, 14),
            (0, 17, 57, 15, 14),
            (0, 17, 57, 15, 14),
            (0, 17, 57, 15, 14),

            (0, 1, 42, 15, 14),
            (0, 17, 42, 15, 14),
            (0, 33, 42, 15, 14),
            (0, 49, 42, 15, 14),

            (0, 17, 57, 15, 14),
            (0, 17, 57, 15, 14),
            (0, 17, 57, 15, 14),
            (0, 17, 57, 15, 14),

            (0, 1, 42, 15, 14),
            (0, 17, 42, 15, 14),
            (0, 33, 42, 15, 14),
            (0, 49, 42, 15, 14),

            (0, 17, 57, 15, 14),
            (0, 17, 57, 15, 14),
            (0, 17, 57, 15, 14),
            (0, 17, 57, 15, 14),

            (0, 1, 42, 15, 14),
            (0, 17, 42, 15, 14),
            (0, 33, 42, 15, 14),
            (0, 49, 42, 15, 14),

            (0, 17, 57, 15, 14),
            (0, 17, 57, 15, 14),
            (0, 17, 57, 15, 14),
            (0, 17, 57, 15, 14),

            (0, 1, 42, 15, 14),
            (0, 17, 42, 15, 14),
            (0, 33, 42, 15, 14),
            (0, 49, 42, 15, 14),

            (0, 17, 57, 15, 14),
            (0, 17, 57, 15, 14),
            (0, 17, 57, 15, 14),
            (0, 17, 57, 15, 14),

            (0, 1, 42, 15, 14),
            (0, 17, 42, 15, 14),
            (0, 33, 42, 15, 14),
            (0, 49, 42, 15, 14),

            (0, 17, 57, 15, 14),
            (0, 17, 57, 15, 14),
            (0, 17, 57, 15, 14),
            (0, 17, 57, 15, 14),

            (0, 1, 42, 15, 14),
            (0, 17, 42, 15, 14),
            (0, 33, 42, 15, 14),
            (0, 49, 42, 15, 14),

            (0, 17, 57, 15, 14),
            (0, 17, 57, 15, 14),
            (0, 17, 57, 15, 14),
            (0, 17, 57, 15, 14),

            (0, 1, 42, 15, 14),
        ]
        self.sprites = []
        self.index = 0
        self.sprite = None
        self.disparos = []
        self.lives = config.ENEMIGOS1_LIVES
        self.speed = config.ENEMIGOS1_SPEED
        

    def move(self):
        '''Método que define el movimiento de un enemigo.'''

        if self.direction == 'up':
            self.y -= self.speed
        elif self.direction == 'down':
            self.y += self.speed
        elif self.direction == 'right':
            self.x += self.speed
        elif self.direction == 'left':
            self.x -= self.speed


    def animation(self):
        '''Método que anima el enemigo regular cambiando de sprite.'''

        self.index += 1

        if self.tipo == 'regular' and self.direction == 'down':
            self.sprites = self.sprites_bank[0:4]
        elif self.tipo == 'regular' and self.direction == 'up':
            self.sprites = self.sprites_bank[4:8]
        elif self.tipo == 'rojo' and self.direction == 'up':
            pass
        elif self.tipo == 'rojo' and self.direction == 'down':
            pass
        elif self.tipo == 'rojo' and self.direction == 'right':
            pass
        elif self.tipo == 'rojo' and self.direction == 'left':
            pass
        elif self.tipo == 'bombardero' and self.direction == 'up':
            pass
        elif self.tipo == 'bombardero' and self.direction == 'down':
            pass
        elif self.tipo == 'superbombardero':
            pass
        
        if self.index >= (len(self.sprites)):
            self.index = 0
            
        self.sprite = self.sprites[self.index]
