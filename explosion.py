import pyxel


class Explosion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.frame = pyxel.frame_count
        self.sprites = [
            # Avión, regular, rojo.
            (0, 105, 18, 14, 12),
            # Bombardero.
            (0, 216, 37, 31, 21),
            # Superbombardero.
            (0, 128, 94, 63, 48)
        ]
        self.index = 0
        self.sprite = self.sprites[self.index]
        self.done = False


    def update(self):
        self.frame = (self.frame + 1) % 8
        if self.frame == 7:
            self.done = True

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
