from config import *


class Island:
    def __init__(self, tipo: str):
        '''Inicialización de la island.'''
        self.x = 0
        self.y = 0
        self.tipo = tipo

        self.sprites = [
            # island grande borde.
            (1, 1, 0, 105, 126),
            # island pequeña 1.
            (1, 1, 127, 10, 9),
            # island pequeña 2.
            (1, 12, 127, 12, 11),
            # island pequeña 3.
            (1, 25, 127, 15, 15),
            # island grande.
            (1, 107, 1, 114, 90)
        ]

        if self.tipo == 'isla_grande_borde':
            self.sprite = self.sprites[0]
            self.x = 0
            self.y = -127
        elif self.tipo == 'isla_pequena_1':
            self.sprite = self.sprites[1]
            self.x = 160
            self.y = -10
        elif self.tipo == 'isla_pequena_2':
            self.sprite = self.sprites[2]
            self.x = 120
            self.y = -40
        elif self.tipo == 'isla_pequena_3':
            self.sprite = self.sprites[3]
            self.x = 210
            self.y = -30
        elif self.tipo == 'isla_grande':
            self.sprite = self.sprites[4]
            self.x = 130
            self.y = -250
        
    def move(self):
        '''Movimiento de la island.'''''
        self.y += 1

        if self.y > BOARD_SIZE[1] + 10:
            if self.tipo == 'isla_grande_borde':
                self.x = 0
                self.y = -127
            elif self.tipo == 'isla_pequena_1':
                self.x = 160
                self.y = -10
            elif self.tipo == 'isla_pequena_2':
                self.x = 120
                self.y = -40
            elif self.tipo == 'isla_pequena_3':
                self.x = 210
                self.y = -30
            elif self.tipo == 'isla_grande':
                self.x = 130
                self.y = -250
