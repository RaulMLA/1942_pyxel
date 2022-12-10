from isla import Isla


class Fondo:
    def __init__(self):
        ''' Inicialización del fondo.'''
        self.islas = []

        # Islas predefinidas.
        self.islas.append(Isla('isla_grande_borde'))
        self.islas.append(Isla('isla_pequena_1'))
        self.islas.append(Isla('isla_pequena_2'))
        self.islas.append(Isla('isla_pequena_3'))
        self.islas.append(Isla('isla_grande'))


    def move(self):
        '''Movimiento del fondo.'''
        for isla in self.islas:
            isla.move()
