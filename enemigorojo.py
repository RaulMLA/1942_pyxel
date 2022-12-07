from enemigos import Enemigo


class EnemigoRojo(Enemigo):

    loops = 3
    dir = 'right'
    count = 0

    def move(self):
        if self.a == True:
            self.sprite = self.sprites[0]
            self.y += self.speed
            #self.x -= 1
            if self.y == 0:
                self.a = False
        else:
            self.sprite = self.sprites[1]
            self.y -= self.speed
            #self.x -= 1

