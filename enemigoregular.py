from enemigos import Enemigo
import pyxel


class EnemigoRegular(Enemigo):

    def __init__(self, x: int, y: int):
        '''Inicialización del enemigo regular.'''

        super().__init__(x, y)
        self.tipo = 'regular'
        self.direction = 'down'


    def move(self):
        '''Método que define el movimiento de un enemigo regular.'''

        super().move()

        if self.direction == 'down':
            if self.y >= 150:
                self.direction = 'up'
