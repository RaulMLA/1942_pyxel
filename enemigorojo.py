from enemigos import Enemigo


class EnemigoRojo(Enemigo):

    def move(self):
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

