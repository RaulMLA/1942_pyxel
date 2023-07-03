import pyxel


class Explosion:
    def __init__(self, x, y, tipo):
        '''Inicializa la explosión.'''

        self.x = x
        self.y = y
        
        if tipo == 'avion':
            self.index = 1
        elif tipo == 'regular':
            self.index = 0
        elif tipo == 'red':
            self.index = 0
        elif tipo == 'bomber':
            self.index = 1
        elif tipo == 'superbomber':
            self.index = 2
        
        self.max = pyxel.frame_count + 7
        
        self.sprites = [
            # Regular, red.
            (0, 105, 18, 14, 12),
            # Avión, bomber.
            (0, 216, 37, 31, 29),
            # superbomber.
            (0, 128, 94, 63, 48)
        ]
        
        self.sprite = self.sprites[self.index]
