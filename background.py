from island import Island


class Background:
    def __init__(self):
        ''' Inicialización del background.'''
        self.islas = []

        # Islas predefinidas.
        self.islas.append(Island('isla_grande_borde'))
        self.islas.append(Island('isla_pequena_1'))
        self.islas.append(Island('isla_pequena_2'))
        self.islas.append(Island('isla_pequena_3'))
        self.islas.append(Island('isla_grande'))


    def move(self):
        '''Movimiento del background.'''
        for island in self.islas:
            island.move()
