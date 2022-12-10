import config
from disparo import Disparo
import pyxel


class Plane:
    def __init__(self, x: int, y:int):
        '''Inicialización del avión.'''

        self.x = x
        self.y = y
        # Sprites para las animaciones del avión.
        self.sprites_bank = [
            (0, 1, 1, 25, 16),
            (0, 27, 1, 25, 16),
            (0, 53, 1, 25, 16),
            (0, 79, 1, 25, 16),

            (0, 205, 71, 28, 17),
            (0, 172, 70, 30, 21),
            (0, 135, 68, 32, 25)
        ]
        self.sprites = []
        self.index = 0
        self.sprite = None
        self.lives = config.PLAYER_LIVES
        self.speed = config.PLAYER_SPEED
        self.disparos = []
        self.loops = config.PLAYER_LOOPS
        self.loop = False


    def move(self, direction: str, size: int):
        '''Método que permite al avión moverse en las 4 direcciones.'''

        plane_x_size = self.sprite[3]
        plane_y_size = self.sprite[4]
        
        if direction == 'right' and self.x < size - plane_x_size:
            self.x += self.speed
        elif direction == 'left' and self.x > 0:
            self.x -= self.speed
        elif direction == 'up' and self.y > 0:
            self.y -= self.speed
        elif direction == 'down' and self.y < size - plane_y_size:
            self.y += self.speed


    def make_loop(self):
        '''Método que permite al avión hacer un loop para evitar ser abatido.'''
        self.loop = True

            
    def animation(self):
        '''Método que anima el avión cambiando de sprite.'''

        if self.loop:
            self.sprites = self.sprites_bank[4:7]
            if pyxel.frame_count % 15 == 0:
                self.index += 1
        else:
            self.sprites = self.sprites_bank[0:4]
            self.index += 1

        if self.index >= (len(self.sprites)):
            self.index = 0

        self.sprite = self.sprites[self.index]


    def comprobar_colision(self, x: int, y: int) -> bool:
        '''Método que comprueba si se impacta con el avión.'''

        if int(x) in range (int(self.x) - 0, int(self.x) + 25) and int(y) in range (int(self.y), int(self.y) + 16):
            return True

        return False