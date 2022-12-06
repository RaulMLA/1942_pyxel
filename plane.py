import config
from disparo import Disparo
class Plane:
    def __init__(self, x: int, y:int):
        self.x = x
        self.y = y
        self.sprite = (0, 0, 0, 16, 16)
        self.lives = config.PLAYER_LIVES
        self.speed = config.PLAYER_SPEED
        self.disparo= []
    def move(self, direction: str, size: int):
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
