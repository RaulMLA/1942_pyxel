import pyxel


class Explosion:
    def __init__(self, x, y, type):
        '''Explosion initialization.'''

        self.x = x
        self.y = y
        
        if type == 'plane':
            self.index = 1
        elif type == 'regular':
            self.index = 0
        elif type == 'red':
            self.index = 0
        elif type == 'bomber':
            self.index = 1
        elif type == 'superbomber':
            self.index = 2
        
        self.max = pyxel.frame_count + 7
        
        self.sprites = [
            # Regular, red.
            (0, 105, 18, 14, 12),
            # Plane, bomber.
            (0, 216, 37, 31, 29),
            # Superbomber.
            (0, 128, 94, 63, 48)
        ]
        
        self.sprite = self.sprites[self.index]
