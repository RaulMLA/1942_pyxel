from enemigos import Enemigo
import random


class EnemigoRegular(Enemigo):

    def move(self, size: int):

        if self.a == True:
            self.sprite = self.sprites[0]
            self.y += self.speed
            #self.x -= 1
            if self.y == 150:
                self.a = False
        else:
            self.sprite = self.sprites[1]
            self.y -= self.speed
            #self.x -= 1
