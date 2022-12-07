from enemigos import Enemigo


class EnemigoRegular(Enemigo):

    def move(self):
        self.indice_dir = 0
        self.contador_mov = 0
        if self.contador_mov < self.avance_movimiento[self.indice_dir]:
            self.contador_mov += 1
        else:
            self.contador_mov = 0
            if self.indice_dir < len(self.direccion_movimiento)-1:
                self.indice_dir += 1
            else:
                self.indice_dir = 0
        direccion = self.direccion_movimiento[self.indice_dir]
        if direccion == 'down':
            self.y += 1
        elif direccion == 'up':
            self.y -= 1
        elif direccion == 'left':
            self.x -= 1
        else:
            self.x += 1

