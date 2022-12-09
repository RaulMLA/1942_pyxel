from enemigos import Enemigo
import random
import pyxel


class EnemigoRojo(Enemigo):

    loops = random.randint(1, 3)
    next_loop = 70
    in_loop = False
    step_1 = False
    step_2 = False
    step_3 = False
    save_y = 0
    save_x = 0
    
    def move(self):
        
        if not self.in_loop:
            self.x += self.speed
            if self.x >= self.next_loop:
                self.in_loop = True
                self.save_y = self.y
                self.step_1 = True
        else:
            if self.step_1:
                self.y += self.speed 
                if self.save_y + 50 <= self.y:
                    self.save_x = self.x
                    self.step_1 = False
                    self.step_2 = True
            elif self.step_2:
                self.x -= self.speed
                if self.save_x - 50 >= self.x:
                    self.save_y = self.y
                    self.step_2 = False
                    self.step_3 = True
            elif self.step_3:
                self.y -= self.speed
                if self.save_y - 50 >= self.y:
                    self.save_x = self.x
                    self.step_3 = False
                    self.in_loop = False
                    self.next_loop += 70
