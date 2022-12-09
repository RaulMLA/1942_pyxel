import config


class Isla:
    def __init__(self, tipo: str):
        self.x = 0
        self.y = 0
        self.tipo = tipo

        self.sprites = [
            # Isla grande borde.
            (1, 1, 0, 105, 126),
            # Isla pequeña 1.
            (1, 1, 127, 10, 9),
            # Isla pequeña 2.
            (1, 12, 127, 12, 11),
            # Isla pequeña 3.
            (1, 25, 127, 15, 15),
            # Isla grande.
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
            self.y = -200
        
    def move(self):
        self.y += 1

        if self.y > config.BOARD_SIZE[1] + 10:
            if self.tipo == 'isla_grande_borde':
                self.x = 0
                self.y = -127
            elif self.tipo == 'isla_pequena_1':
                self.x = 160
                self.y = -10
            elif self.tipo == 'isla_pequena_2':
                self.x = 120
                self.y = -12
            elif self.tipo == 'isla_pequena_3':
                self.x = 210
                self.y = -16
            elif self.tipo == 'isla_grande':
                self.x = 130
                self.y = -91
