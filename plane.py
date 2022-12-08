import config
from disparo import Disparo
import pyxel


class Plane:
    def __init__(self, x: int, y:int):
        '''Inicialización del avión.'''

        self.x = x
        self.y = y
        # Sprites para las animaciones del avión.
        self.sprites = [
            (0, 1, 1, 24, 16),
            (0, 27, 1, 24, 16),
            (0, 53, 1, 24, 16),
            (0, 79, 1, 24, 16)
        ]
        self.index = 0
        self.sprite = self.sprites[self.index]
        self.lives = config.PLAYER_LIVES
        self.speed = config.PLAYER_SPEED
        self.disparos = []
        self.loop = False


    def move(self, direction: str, size: int):
        '''Método que permite al avión moverse en las 4 direcciones.'''

        plane_x_size = self.sprite[3]
        plane_y_size = self.sprite[4]
        
        if direction.lower() == 'right' and self.x < size - plane_x_size:
            self.x += self.speed
        elif direction.lower() == 'left' and self.x > 0:
            self.x -= self.speed
        elif direction.lower() == 'up' and self.y > 0:
            self.y -= self.speed
        elif direction.lower() == 'down' and self.y < size - plane_y_size:
            self.y += self.speed


    def make_loop(self):
        '''Método que permite al avión hacer un loop para evitar ser abatido.'''
        self.loop = True
        #self.loop_animation()
        print('Activado')
        
            
    def animation(self):
        '''Método que anima el avión cambiando de sprite.'''

        self.index += 1

        if self.index >= (len(self.sprites)):
            self.index = 0

        self.sprite = self.sprites[self.index]

    def loop_animation(self):
        '''Método que anima el avión cuando hace un loop.'''

        self.index += 1

        if self.index >= (len(self.sprites)):
            self.index = 0

        self.sprite = self.sprites[self.index]
