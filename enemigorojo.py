from enemigos import Enemigo
import random
import config


class EnemigoRojo(Enemigo):

    def __init__(self, x: int, y: int):
        '''Inicialización del enemigo rojo.'''

        super().__init__(x, y)
        self.tipo = 'rojo'
        self.direction = 'right'

        self.loops = random.randint(1, 3)
        self.next_loop = 70
        self.in_loop = False
        self.save_y = 0
        self.save_x = 0

        self.lives = config.ENEMIGOS2_LIVES
        self.speed = config.ENEMIGOS2_SPEED
        self.score = config.ENEMIGOS2_SCORE
    

    def move(self):
        
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
