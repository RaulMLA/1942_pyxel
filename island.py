from config import *


class Island:
    def __init__(self, type: str):
        '''Island initialization.'''
        self.x = 0
        self.y = 0
        self.type = type

        self.sprites = [
            # Big island border.
            (1, 1, 0, 105, 126),
            # Small island 1.
            (1, 1, 127, 10, 9),
            # Small island 2.
            (1, 12, 127, 12, 11),
            # Small island 3.
            (1, 25, 127, 15, 15),
            # Big island.
            (1, 107, 1, 114, 90)
        ]

        if self.type == 'border_big_island':
            self.sprite = self.sprites[0]
            self.x = 0
            self.y = -127
        elif self.type == 'small_island_1':
            self.sprite = self.sprites[1]
            self.x = 160
            self.y = -10
        elif self.type == 'small_island_2':
            self.sprite = self.sprites[2]
            self.x = 120
            self.y = -40
        elif self.type == 'small_island_3':
            self.sprite = self.sprites[3]
            self.x = 210
            self.y = -30
        elif self.type == 'big_island':
            self.sprite = self.sprites[4]
            self.x = 130
            self.y = -250
        
    def move(self):
        '''Island movement.'''
        self.y += 1

        if self.y > BOARD_SIZE[1] + 10:
            if self.type == 'border_big_island':
                self.x = 0
                self.y = -127
            elif self.type == 'small_island_1':
                self.x = 160
                self.y = -10
            elif self.type == 'small_island_2':
                self.x = 120
                self.y = -40
            elif self.type == 'small_island_3':
                self.x = 210
                self.y = -30
            elif self.type == 'big_island':
                self.x = 130
                self.y = -250
