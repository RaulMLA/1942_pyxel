from enemigos import Enemigo
import config
import pyxel


class Superbombardero(Enemigo):

    def __init__(self, x: int, y: int):
        '''Inicialización del enemigo superbombardero.'''

        super().__init__(x, y)
        self.tipo = 'superbombardero'
        self.direction = 'up'

        self.lives = config.ENEMIGOS4_LIVES
        self.speed = config.ENEMIGOS4_SPEED
        self.score = config.ENEMIGOS4_SCORE


    def move(self):
        '''Método que define el movimiento de un enemigo superbombardero.'''

        super().move()

        if self.direction == 'up':
            if self.y <= 150:
                self.direction = None


    def comprobar_colision(self, x: int, y: int) -> bool:
        '''Método que comprueba si el disparo impacta en el enemigo.'''

        if int(x) in range (int(self.x) - 10, int(self.x) + 15) and int(y) in range (int(self.y), int(self.y) + 15):
            self.lives -= 1
            return True
        else:
            return False

