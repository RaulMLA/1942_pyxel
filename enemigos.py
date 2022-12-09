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
            # Regular -> Dirección 'down' ([0:4])
            (0, 1, 42, 15, 14),
            (0, 17, 42, 15, 14),
            (0, 33, 42, 15, 14),
            (0, 49, 42, 15, 14),

            # Regular -> Dirección 'up' ([4:8])
            (0, 1, 57, 15, 14),
            (0, 17, 57, 15, 14),
            (0, 33, 57, 15, 14),
            (0, 49, 57, 15, 14),

            # Rojo -> Dirección 'down' ([8:12])
            (0, 1, 80, 15, 14),
            (0, 17, 80, 15, 14),
            (0, 33, 80, 15, 14),
            (0, 49, 80, 15, 14),

            # Rojo -> Dirección 'up' ([12:16])
            (0, 65, 80, 15, 14),
            (0, 81, 80, 15, 14),
            (0, 97, 80, 15, 14),
            (0, 113, 80, 15, 14),

            # Rojo -> Dirección 'right' ([16:20])
            (0, 65, 48, 14, 7),
            (0, 80, 48, 14, 7),
            (0, 61, 72, 14, 7),
            (0, 76, 72, 14, 7),

            # Rojo -> Dirección 'left' ([20:24])
            (0, 1, 72, 14, 7),
            (0, 16, 72, 14, 7),
            (0, 31, 72, 14, 7),
            (0, 46, 72, 14, 7),

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
            self.sprites = self.sprites_bank[12:16]
        elif self.tipo == 'rojo' and self.direction == 'down':
            self.sprites = self.sprites_bank[8:12]
        elif self.tipo == 'rojo' and self.direction == 'right':
            self.sprites = self.sprites_bank[16:20]
        elif self.tipo == 'rojo' and self.direction == 'left':
            self.sprites = self.sprites_bank[20:24]
        elif self.tipo == 'bombardero' and self.direction == 'up':
            pass
        elif self.tipo == 'bombardero' and self.direction == 'down':
            pass
        elif self.tipo == 'superbombardero':
            pass
        
        if self.index >= (len(self.sprites)):
            self.index = 0
            
        self.sprite = self.sprites[self.index]
