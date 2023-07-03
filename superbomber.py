from enemy import Enemy
import config
import random


class Superbomber(Enemy):

    def __init__(self, x: int, y: int):
        '''Superbomber enemy initialization.'''

        super().__init__(x, y)
        self.type = 'superbomber'
        self.direction = 'up'

        self.lives = config.ENEMIES4_LIVES
        self.speed = config.ENEMIES4_SPEED
        self.score = config.ENEMIES4_SCORE

        self.loops = random.randint(1, 2)
        self.next_loop = 110
        self.in_loop = False
        self.save_y = 0
        self.save_x = 0


    def move(self):
        '''Method that defines the movement of a superbomber enemy.'''

        super().move()

        if not self.in_loop:
            if self.y <= self.next_loop and self.loops > 0:
                self.in_loop = True
                self.save_x = self.x
                self.direction = 'left'
        else:
            if self.direction == 'left':
                if self.save_x - 50 >= self.x:
                    self.save_y = self.y
                    self.direction = 'down'
            elif self.direction == 'down':
                if self.save_y + 20 <= self.y:
                    self.save_x = self.x
                    self.direction = 'right'
            elif self.direction == 'right':
                if self.save_x + 50 <= self.x:
                    self.loops -= 1
                    self.in_loop = False
                    self.next_loop -= 50
                    self.direction = 'up'


    def check_colision(self, x: int, y: int, type: str) -> bool:
        '''Method that checks if it collides with the enemy.'''

        if type == 'shot':
            if int(x) in range (int(self.x) - 11, int(self.x) + 60) and int(y) in range (int(self.y), int(self.y) + 10):
                self.lives -= 1
                return True
        # type == 'plane':
        else:
            if int(x) in range (int(self.x) - 25, int(self.x) + 60) and int(y) in range (int(self.y), int(self.y) + 20):
                self.lives -= 1
                return True

        return False

