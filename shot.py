from config import *

class Shot:
    def __init__(self, x: int, y: int, type: str, direction: str):
        '''Shot initialization.'''
        self.x = x
        self.y = y

        # Sprites for shot animations.
        self.sprites = [
            (0, 1, 18, 11, 10),
            (0, 13, 18, 4, 4)
        ]
        self.sprite = self.sprites[0] if type == 'plane' else self.sprites[1]
        self.speed = ENEMIES_SHOTS if type == 'enemy' else PLAYER_SHOTS
        self.direction = direction


    def move (self):
        '''Method that defines the movement of a shot.'''

        # Lineal movements.
        if self.direction == 'down':
            self.y += self.speed
        elif self.direction == 'up':
            self.y -= self.speed
        elif self.direction == 'left':
            self.x -= self.speed
        elif self.direction == 'right':
            self.x += self.speed
        
        # Diagonal movements.
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
