import random
import config

class Enemy:
    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y
        self.type = None
        self.direction = None

        # Positions that were assigned to the enemy when the game started.
        self.start_x = x
        self.start_y = y

        # Sprites for enemy animations.
        self.sprites_bank = [
            # Regular -> Direction 'down' ([0:4])
            (0, 1, 42, 15, 14),
            (0, 17, 42, 15, 14),
            (0, 33, 42, 15, 14),
            (0, 49, 42, 15, 14),

            # Regular -> Direction 'up' ([4:8])
            (0, 1, 57, 15, 14),
            (0, 17, 57, 15, 14),
            (0, 33, 57, 15, 14),
            (0, 49, 57, 15, 14),

            # red -> Direction 'down' ([8:12])
            (0, 1, 80, 15, 14),
            (0, 17, 80, 15, 14),
            (0, 33, 80, 15, 14),
            (0, 49, 80, 15, 14),

            # red -> Direction 'up' ([12:16])
            (0, 65, 80, 15, 14),
            (0, 81, 80, 15, 14),
            (0, 97, 80, 15, 14),
            (0, 113, 80, 15, 14),

            # red -> Direction 'right' ([16:20])
            (0, 65, 48, 14, 7),
            (0, 80, 48, 14, 7),
            (0, 61, 72, 14, 7),
            (0, 76, 72, 14, 7),

            # red -> Direction 'left' ([20:24])
            (0, 1, 72, 14, 7),
            (0, 16, 72, 14, 7),
            (0, 31, 72, 14, 7),
            (0, 46, 72, 14, 7),

            # bomber -> Direction 'down' ([24:28])
            (0, 1, 119, 31, 23),
            (0, 33, 119, 31, 23),
            (0, 65, 119, 31, 23),
            (0, 97, 119, 31, 23),

            # bomber -> Direction 'up' ([28:32])
            (0, 1, 95, 31, 23),
            (0, 33, 95, 31, 23),
            (0, 65, 95, 31, 23),
            (0, 97, 95, 31, 23),

            # superbomber (full) -> Direction 'up' ([32:34])
            (0, 0, 143, 63, 48),
            (0, 64, 143, 63, 48),

            # superbomber (half) -> Direction 'up' ([34:36])
            (0, 128, 143, 63, 48),
            (0, 192, 143, 63, 48),

            # superbomber (destroyed) -> Direction 'up' ([36:37])
            (0, 128, 94, 63, 48),
        ]
        self.sprites = []
        self.index = 0
        self.sprite = None
        self.shots = []
        

    def move(self):
        '''Method that defines the movement of an enemy.'''

        # Lineal movements.
        if self.direction == 'up':
            self.y -= self.speed
        elif self.direction == 'down':
            self.y += self.speed
        elif self.direction == 'right':
            self.x += self.speed
        elif self.direction == 'left':
            self.x -= self.speed

        # Diagonal movements.
        elif self.direction == 'upleft':
            self.x -= 0.4
            self.y -= self.speed
        elif self.direction == 'upright':
            self.x += 0.4
            self.y -= self.speed
        elif self.direction == 'downleft':
            self.x -= 0.4
            self.y += self.speed
        elif self.direction == 'downright':
            self.x += 0.4
            self.y += self.speed



    def animation(self):
        '''Method that animates the regular enemy by changing the sprite.'''

        self.index += 1

        if self.type == 'regular' and self.direction in ['down', 'downleft', 'downright']:
            self.sprites = self.sprites_bank[0:4]
        elif self.type == 'regular' and self.direction == 'up':
            self.sprites = self.sprites_bank[4:8]
        elif self.type == 'red' and self.direction == 'up':
            self.sprites = self.sprites_bank[12:16]
        elif self.type == 'red' and self.direction == 'down':
            self.sprites = self.sprites_bank[8:12]
        elif self.type == 'red' and self.direction == 'right':
            self.sprites = self.sprites_bank[16:20]
        elif self.type == 'red' and self.direction == 'left':
            self.sprites = self.sprites_bank[20:24]
        elif self.type == 'bomber' and self.direction in ['up', 'upleft', 'upright']:
            self.sprites = self.sprites_bank[28:32]
        elif self.type == 'bomber' and self.direction in ['down', 'downleft', 'downright']:
            self.sprites = self.sprites_bank[24:28]
        elif self.type == 'superbomber':
            if self.lives > config.ENEMIES4_LIVES / 2:
                self.sprites = self.sprites_bank[32:34]
            else:
                self.sprites = self.sprites_bank[34:36]
        
        if self.index >= (len(self.sprites)):
            self.index = 0
            
        self.sprite = self.sprites[self.index]


    def reset(self):
        '''Method that resets the enemy position to the initial one.'''
        self.x = self.start_x
        self.y = self.start_y
        self.shots = []

        if self.type == 'red':
            self.direction = 'right'
        elif self.type == 'bomber':
            self.direction = random.choice(['down', 'downleft', 'downright'])
        elif self.type == 'superbomber':
            self.direction = 'up'
        elif self.type == 'regular':
            self.direction = random.choice(['down', 'downleft', 'downright'])

    def __repr__(self) -> str:
        '''Enemy representation for debug purposes.'''
        return f'enemy({self.type}, {self.x}, {self.y}, {self.direction})'
