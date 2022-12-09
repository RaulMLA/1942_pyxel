from enemigos import Enemigo
import config
import pyxel


class EnemigoRegular(Enemigo):

    def __init__(self, x: int, y: int):
        '''Inicialización del enemigo regular.'''

        super().__init__(x, y)
        self.tipo = 'regular'
        self.direction = 'down'

        self.lives = config.ENEMIGOS1_LIVES
        self.speed = config.ENEMIGOS1_SPEED


    def move(self):
        '''Método que define el movimiento de un enemigo regular.'''

        super().move()

        if self.direction == 'down':
            if self.y >= 150:
                self.direction = 'up'
