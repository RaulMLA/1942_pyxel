import config

class Disparo:
    def __init__(self, x:int, y: int):
        self.x=x
        self.y =y
        self.sprite= (1, 3, 6, 16, 16)
    def move (self, direccion):
        if direccion =="down":
            self.y+=3
        else:
            self.y -=3
