from enemigos import Enemigo
import random
import pyxel


class EnemigoRojo(Enemigo):

    def __init__(self, x: int, y: int):
        '''Inicialización del enemigo rojo.'''

        super().__init__(x, y)
        self.tipo = 'rojo'
        self.direction = 'right'

        self.loops = random.randint(1, 3)
        self.next_loop = 70
        self.in_loop = False
        self.step_1 = False
        self.step_2 = False
        self.step_3 = False
        self.save_y = 0
        self.save_x = 0
    
    def move(self):
        
        super().move()

        if not self.in_loop:
            if self.x >= self.next_loop:
                self.in_loop = True
                self.save_y = self.y
                self.step_1 = True
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
                    self.save_x = self.x
                    self.in_loop = False
                    self.next_loop += 70
                    self.direction = 'right'
