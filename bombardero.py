from enemigos import Enemigo
import config
import pyxel


class Bombardero(Enemigo):

    def __init__(self, x: int, y: int):
        '''Inicialización del enemigo bombardero.'''

        super().__init__(x, y)
        self.tipo = 'bombardero'
        self.direction = 'down'

        self.lives = config.ENEMIGOS3_LIVES
        self.speed = config.ENEMIGOS3_SPEED


    def move(self):
        '''Método que define el movimiento de un enemigo bombardero.'''

        super().move()

        if self.direction == 'down':
            if self.y >= 150:
                self.direction = 'up'

