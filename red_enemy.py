from enemy import Enemy
import random
import config


class RedEnemy(Enemy):

    def __init__(self, x: int, y: int):
        '''Red enemy initialization.'''

        super().__init__(x, y)
        self.type = 'red'
        self.direction = 'right'

        self.loops = random.randint(1, 3)
        self.next_loop = 70
        self.in_loop = False
        self.save_y = 0
        self.save_x = 0

        self.lives = config.ENEMIES2_LIVES
        self.speed = config.ENEMIES2_SPEED
        self.score = config.ENEMIES2_SCORE
    

    def move(self):
        '''Method that defines the movement of an enemy red.'''
        
        super().move()

        if not self.in_loop:
            if self.x >= self.next_loop and self.loops > 0:
                self.in_loop = True
                self.save_y = self.y
                self.direction = 'down'
        else:
            if self.direction == 'down':
                if self.save_y + 50 <= self.y:
                    self.save_x = self.x
                    self.direction = 'left'
            elif self.direction == 'left':
                if self.save_x - 50 >= self.x:
                    self.save_y = self.y
                    self.direction = 'up'
            elif self.direction == 'up':
                if self.save_y - 50 >= self.y:
                    self.loops -= 1
                    self.in_loop = False
                    self.next_loop += 70
                    self.direction = 'right'


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
