from island import Island


class Background:
    def __init__(self):
        '''Background initialization.'''
        self.islands = []

        # Predifined islands.
        self.islands.append(Island('border_big_island'))
        self.islands.append(Island('small_island_1'))
        self.islands.append(Island('small_island_2'))
        self.islands.append(Island('small_island_3'))
        self.islands.append(Island('big_island'))


    def move(self):
        '''Background movement.'''
        for island in self.islands:
            island.move()
