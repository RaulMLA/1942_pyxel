from enemy import Enemy
import config
import random
import pyxel


class Bomber(Enemy):

    def __init__(self, x: int, y: int):
        '''Enemy bomber initialization.'''

        super().__init__(x, y)
        self.type = 'bomber'
        self.direction = random.choice(['down', 'downleft', 'downright'])	

        self.lives = config.ENEMIES3_LIVES
        self.speed = config.ENEMIES3_SPEED
        self.score = config.ENEMIES3_SCORE


    def move(self):
        '''Method that defines the movement of an enemy bomber.'''

        super().move()

        if self.direction in ['down', 'downleft', 'downright']:
            if self.y >= 150:
                self.direction = random.choice(['up', 'upleft', 'upright'])

    def check_colision(self, x: int, y: int, type: str) -> bool:
        '''Method that checks if it collides with the enemy.'''

        if type == 'shot':
            if int(x) in range (int(self.x) - 11, int(self.x) + 31) and int(y) in range (int(self.y), int(self.y) + 23):
                self.lives -= 1
                return True
        # type == 'plane':
        else:
            if int(x) in range (int(self.x) - 25, int(self.x) + 31) and int(y) in range (int(self.y), int(self.y) + 15):
                self.lives -= 1
                return True

        return False
