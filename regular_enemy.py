from enemy import Enemy
import config
import random
import pyxel


class RegularEnemy(Enemy):

    def __init__(self, x: int, y: int):
        '''Regular enemy initialization.'''

        super().__init__(x, y)
        self.type = 'regular'
        self.direction = random.choice(['down', 'downleft', 'downright'])

        self.lives = config.ENEMIES1_LIVES
        self.speed = config.ENEMIES1_SPEED
        self.score = config.ENEMIES1_SCORE


    def move(self):
        '''Regular enemy movement method.'''

        super().move()

        if self.direction in ['down', 'downleft', 'downright']:
            if self.y >= 150:
                self.direction = 'up'


    def check_colision(self, x: int, y: int, type: str) -> bool:
        '''Method that checks if it collides with the enemy.'''

        if type == 'shot':
            if int(x) in range (int(self.x) - 11, int(self.x) + 15) and int(y) in range (int(self.y), int(self.y) + 14):
                self.lives -= 1
                return True
        # type == 'plane':
        else:
            if int(x) in range (int(self.x) - 25, int(self.x) + 15) and int(y) in range (int(self.y), int(self.y) + 14):
                self.lives -= 1
                return True

        return False
