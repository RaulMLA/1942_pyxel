from enemigos import Enemigo
import config
import random
import pyxel


class EnemigoRegular(Enemigo):

    def __init__(self, x: int, y: int):
        '''Inicialización del enemigo regular.'''

        super().__init__(x, y)
        self.tipo = 'regular'
        self.direction = random.choice(['down', 'downleft', 'downright'])

        self.lives = config.ENEMIGOS1_LIVES
        self.speed = config.ENEMIGOS1_SPEED
        self.score = config.ENEMIGOS1_SCORE


    def move(self):
        '''Método que define el movimiento de un enemigo regular.'''

        super().move()

        if self.direction in ['down', 'downleft', 'downright']:
            if self.y >= 150:
                self.direction = 'up'


    def comprobar_colision(self, x: int, y: int, tipo: str) -> bool:
        '''Método que comprueba si se impacta con el enemigo.'''

        if tipo == 'disparo':
            if int(x) in range (int(self.x) - 11, int(self.x) + 15) and int(y) in range (int(self.y), int(self.y) + 14):
                self.lives -= 1
                return True
        # tipo == 'avion':
        else:
            if int(x) in range (int(self.x) - 25, int(self.x) + 15) and int(y) in range (int(self.y), int(self.y) + 14):
                self.lives -= 1
                return True

        return False
