import pyxel


class Explosion:
    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        
        if tipo == 'avion':
            self.index = 1
        elif tipo == 'regular':
            self.index = 0
        elif tipo == 'rojo':
            self.index = 0
        elif tipo == 'bombardero':
            self.index = 1
        elif tipo == 'superbombardero':
            self.index = 2
        
        self.max = pyxel.frame_count + 7
        
        self.sprites = [
            # Regular, rojo.
            (0, 105, 18, 14, 12),
            # Avión, bombardero.
            (0, 216, 37, 31, 29),
            # Superbombardero.
            (0, 128, 94, 63, 48)
        ]
        self.sprite = self.sprites[self.index]
