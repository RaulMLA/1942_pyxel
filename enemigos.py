import random
import config
class Enemigo:
    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y
        self.sprite = (1, 3, 6, 16, 16)
        self.disparo= []
        self.lives = config.ENEMIGOS1_LIVES
        self.speed = config.ENEMIGOS1_SPEED
        self.a=True


    def move(self, direction:int,size: int):
        '''
        if self.a==True:
            self.y += self.speed
            if self.y==random.randint(130,180):
                self.a=False
        else:
            self.y -= self.speed'''

        if direction.lower() :
            self.y -= self.speed
        
        elif direction.lower() == 'down' :
            self.y += self.speed






