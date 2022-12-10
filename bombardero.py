from enemigos import Enemigo
import config
import random
import pyxel


class Bombardero(Enemigo):

    def __init__(self, x: int, y: int):
        '''Inicialización del enemigo bombardero.'''

        super().__init__(x, y)
        self.tipo = 'bombardero'
        self.direction = random.choice(['down', 'downleft', 'downright'])	

        self.lives = config.ENEMIGOS3_LIVES
        self.speed = config.ENEMIGOS3_SPEED
        self.score = config.ENEMIGOS3_SCORE


    def move(self):
        '''Método que define el movimiento de un enemigo bombardero.'''

        super().move()

        if self.direction in ['down', 'downleft', 'downright']:
            if self.y >= 150:
                self.direction = random.choice(['up', 'upleft', 'upright'])

    def comprobar_colision(self, x: int, y: int, tipo: str) -> bool:
        '''Método que comprueba si se impacta con el enemigo.'''

        if tipo == 'disparo':
            if int(x) in range (int(self.x) - 11, int(self.x) + 31) and int(y) in range (int(self.y), int(self.y) + 23):
                self.lives -= 1
                return True
        # tipo == 'avion':
        else:
            if int(x) in range (int(self.x) - 25, int(self.x) + 31) and int(y) in range (int(self.y), int(self.y) + 15):
                self.lives -= 1
                return True

        return False
