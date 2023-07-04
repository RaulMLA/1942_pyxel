import random
from enemy import Enemy
from regular_enemy import RegularEnemy
from red_enemy import RedEnemy
from bomber import Bomber
from explosion import Explosion
from background import Background
from superbomber import Superbomber
from plane import Plane
from shot import Shot
import pyxel
import copy
from config import *


class Board:
    '''Board class that represents the board.'''

    def __init__(self, w: int, h: int):
        '''Board initialization with its measures and loading of the image bank.'''

        # Board dimensions.
        self.width = w
        self.height = h

        # Punctuation markers.
        self.marker_1up = 0
        self.marker_highscore = 40000

        # Window and assets.
        pyxel.init(self.width, self.height, title = "1942")
        pyxel.load("assets/my_resource.pyxres")

        # Initial position of our player.
        self.plane = Plane(self.width / 2, 200)

        # Append de enemies in a list.
        self.enemies = []
        self.inactive_enemies = []

        # Background islands.
        self.background = Background()

        # Enemies generation.
        self.generate_enemigos()

        # Enemies explosions.
        self.explosions = []

        # Control variable for the generation of enemies.
        self.random_number = random.randint(50, 100)

        # Control variable for the bonus for destroying red enemies.
        self.bonus = False

        # Counter to check the number of red enemies destroyed for the bonus.
        self.red_counter = 0

        # Background music.
        pyxel.play(0, 1, 1, True)
        pyxel.play(0, 2, 1, True)
        pyxel.play(0, 3, 1, True)

        # Initial condition of the game.
        self.start_condition = False

        # Player has lost a life.
        self.loose_life = False

        # Player has lost the game.
        self.loose = False

        # We run the game.
        pyxel.run(self.update, self.draw)


    def update(self):
        '''
        Method that updates the state of the board.
        (*) There are enemy loops that could be optimized by merging them into one,
        but they have been considered separate to facilitate reading and understanding of the code.
        '''

        # ENTER key to start playing.
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.start_condition = True

        # Q key to quit the game.
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # Explosions control.
        for explosion in self.explosions:
            if explosion.max < pyxel.frame_count:
                self.explosions.remove(explosion)
        
        if self.start_condition:
            # Configurations are restored if the user has lost a life.
            if self.loose_life:
                self.random_number = random.randint(50, 100)
                self.plane.x = self.width / 2
                self.plane.y = 200
                self.loose_life = False

            # Player movement (right and left).
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.plane.move('right', self.width)
            elif pyxel.btn(pyxel.KEY_LEFT):
                self.plane.move('left', self.width)
            
            # Player movement (up and down).
            if pyxel.btn(pyxel.KEY_UP):
                self.plane.move('up', self.width)
            elif pyxel.btn(pyxel.KEY_DOWN):
                self.plane.move('down', self.width)

            # Player loop movement to avoid being shot down.
            if pyxel.btn(pyxel.KEY_Z):
                if self.plane.loops > 0:
                    self.plane.make_loop()
                
            # Maximum time a loop lasts.
            if self.plane.make_loop:
                if pyxel.frame_count % 45 == 0:
                    if self.plane.loop:
                        self.plane.loops -= 1
                        self.plane.loop = False    

            # Enemies are activated.
            if (pyxel.frame_count + 1) % self.random_number == 0 and len(self.inactive_enemies) > 0:
                enemy = self.inactive_enemies.pop(0)
                # Red enemies are generated in groups of 5 and appear in the same interval of time.
                if enemy.type == 'red':
                    self.random_number = 10
                    if len(self.inactive_enemies) > 0:
                        if self.inactive_enemies[0].type != 'red':
                            self.random_number = random.randint(100, 300)
                # Regular enemies are generated in groups of 10 and appear in the same interval of time.
                elif enemy.type == 'regular':
                    self.random_number = 20
                    if len(self.inactive_enemies) > 0:
                        if self.inactive_enemies[0].type != 'regular':
                            self.random_number = random.randint(100, 300)
                elif enemy.type == 'bomber':
                    self.random_number = 100
                    if len(self.inactive_enemies) > 0:
                        if self.inactive_enemies[0].type != 'bomber':
                            self.random_number = random.randint(100, 300)    
                else:
                    self.random_number = random.randint(100, 300)
                
                # Enemy is activated.
                self.enemies.append(enemy)

            # Shot creation by the player.
            if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_S):
                if self.bonus:
                    self.plane.shots.append(Shot(self.plane.x, self.plane.y, 'plane', 'up'))
                    self.plane.shots.append(Shot(self.plane.x + 15, self.plane.y, 'plane', 'up'))
                else:
                    self.plane.shots.append(Shot(self.plane.x + 7, self.plane.y, 'plane', 'up'))
                # Shot sound.
                pyxel.play(1, 6)

            # Player shot movement.
            for i in range(len(self.plane.shots)):
                self.plane.shots[i].move()

            # Shot movement and frequency depending on the type of enemy.
            for enemy in self.enemies:
                # Regular enenmies.
                if enemy.type == 'regular':
                    if random.randint(1, 100) < 4 and enemy.direction != 'up':
                        enemy.shots.append(Shot(enemy.x + 5, enemy.y, 'enemy', enemy.direction))
                # Red enemies.
                elif enemy.type == 'red':
                    if random.randint(1, 100) < 2:
                        enemy.shots.append(Shot(enemy.x + 10, enemy.y, 'enemy', enemy.direction))
                # Bomber enemies.
                elif enemy.type == 'bomber':
                    if random.randint(1, 100) < 3 and enemy.direction not in ['up', 'upleft', 'upright']:
                        enemy.shots.append(Shot(enemy.x + 20, enemy.y, 'enemy', enemy.direction))
                # Superbomber enemies.
                elif enemy.type == 'superbomber':
                    if random.randint(1, 100) < 4 and enemy.y < 200:
                        # Generate in groups of 3 with different directions.
                        enemy.shots.append(Shot(enemy.x + 30, enemy.y + 30, 'enemy', 'downleft'))
                        enemy.shots.append(Shot(enemy.x + 30, enemy.y + 30, 'enemy', 'down'))
                        enemy.shots.append(Shot(enemy.x + 30, enemy.y + 30, 'enemy', 'downright'))
            
                for shot in enemy.shots:
                    shot.move()

            # If the player has double shot bonus, it is removed after a while.
            if pyxel.frame_count % 250 == 0 and self.bonus:
                    self.bonus = False

            # Plane shots are removed when they leave the screen.
            for shot in self.plane.shots:
                if shot.y < -8:
                    self.plane.shots.remove(shot)

            # Enemy shots are removed when they leave the screen.
            for enemy in self.enemies:
                for shot in enemy.shots:
                    if shot.y > self.height or shot.y < -8 or shot.x < -8 or shot.x > self.width:
                        enemy.shots.remove(shot)
            
            # Enemy is removed when it leaves the screen.
            for enemy in self.enemies:
                if enemy.y > self.height or enemy.y < -50 or enemy.x < -50 or enemy.x > self.width:
                    self.enemies.remove(enemy)
            
            # Background islands movement.
            self.background.move()

            # Enemies movement.
            for enemy in self.enemies:
                enemy.move()

            # Colision between shots and enemies.
            for shot in self.plane.shots:
                for enemy in self.enemies:
                    if enemy.check_colision(shot.x, shot.y, 'shot'):
                        self.plane.shots.remove(shot)
                        if enemy.lives <= 0:
                            # We check if it is red and if all the reds of a batch have been destroyed for the bonus.
                            if enemy.type == 'red':
                                self.red_counter += 1
                                if self.red_counter == 5:
                                    self.bonus = True
                                    self.plane.loops += 2
                                    self.red_counter = 0
                            elif enemy.type != 'red' and self.red_counter > 0:
                                self.red_counter = 0
                            # Explosion sound.
                            pyxel.play(1, 5)
                            self.marker_1up += enemy.score
                            self.enemies.remove(enemy)
                            self.explosions.append(Explosion(enemy.x, enemy.y, enemy.type))
            
            # Colision between shots and player.
            for enemy in self.enemies:
                for shot in enemy.shots:
                    if self.plane.check_colision(shot.x, shot.y) and not self.plane.loop:
                        enemy.shots.remove(shot)
                        self.explosions.append(Explosion(self.plane.x, self.plane.y, 'plane'))
                        # Sound effect of shot hit enemy.
                        pyxel.play(1, 0)
                        self.stop_game()
            
            # Colision between player and enemies.
            for enemy in self.enemies:
                if enemy.check_colision(self.plane.x, self.plane.y, 'plane') and not self.plane.loop:
                    self.explosions.append(Explosion(self.plane.x, self.plane.y, 'plane'))
                    # Enemy collision sound effect.
                    pyxel.play(1, 4)
                    self.stop_game()

            # Plane animation.
            self.plane.animation()

            # Enemies animation.
            for i in range (len(self.enemies)):
                self.enemies[i].animation()
    

    def draw(self):
        '''Method that allows to draw each element in the window.'''

        if self.start_condition:

            # Background image.
            #pyxel.blt(0, 0, 2, 0, 0, 255, 255, colkey = 8)

            # Background color.
            pyxel.cls(1)

            # Islands are drawn.
            for island in self.background.islands:
                pyxel.blt(island.x, island.y, *island.sprite, colkey = 8)

            # Punctuation markers are drawn.
            pyxel.text(15, 5, "1 U P", 7)
            pyxel.text(60, 5, "H I G H  S C O R E", 10)
            pyxel.text(155, 5, "L O O P S", 11)
            pyxel.text(210, 5, "L I V E S", 14)

            pyxel.text(15, 15, str(self.marker_1up), 13)
            pyxel.text(60, 15, str(self.marker_highscore), 13)
            pyxel.text(155, 15, str(self.plane.loops), 13)
            pyxel.text(210, 15, str(self.plane.lives), 13)

            # Plane is drawn.
            pyxel.blt(self.plane.x, self.plane.y, *self.plane.sprite, colkey = 8)

            # Enemies are drawn.
            for enemy in self.enemies:
                pyxel.blt(enemy.x, enemy.y, *enemy.sprite, 8)

            # Enemy shots are drawn.
            for enemy in self.enemies:
                for shot in enemy.shots:
                    pyxel.blt(shot.x, shot.y, *shot.sprite, 8)

            # Plane shots are drawn.
            for shot in self.plane.shots:
                pyxel.blt(shot.x, shot.y, *shot.sprite, 8)

            # Final animation.
            if self.plane.lives == 0:
                self.loose = True
                # Background image.
                #pyxel.blt(0, 0, 2, 0, 0, 255, 255, colkey = 8)

                # Background color.
                pyxel.cls(1)

                pyxel.blt(40, 50, 0, 1, 209, 177, 45, colkey = 8)
                pyxel.text(95, 125, '--- GAME OVER ---', 7)
                pyxel.text(105, 152, 'YOU LOOSE', 7)
                pyxel.blt(95, 188, 0, 1, 192, 64, 16, colkey = 8)

            if len(self.inactive_enemies) == 0 and len(self.enemies) == 0 and not self.loose:
                # Background image.
                #pyxel.blt(0, 0, 2, 0, 0, 255, 255, colkey = 8)

                # Background color.
                pyxel.cls(1)

                pyxel.blt(40, 50, 0, 1, 209, 177, 45, colkey = 8)
                pyxel.text(93, 125, '--- GAME OVER ---', 7)
                pyxel.text(108, 152, 'YOU WIN', 7)
                pyxel.text(99, 164, 'SCORE: ' + str(self.marker_1up), 7)
                pyxel.blt(95, 200, 0, 1, 192, 64, 16, colkey = 8)
        
        # Explosions are drawn.
        for explosion in self.explosions:
            pyxel.blt(explosion.x, explosion.y, *explosion.sprite, 8)

        # Initial animation.
        if not self.start_condition and not self.loose and not self.loose_life:
            # Background image.
            #pyxel.blt(0, 0, 2, 0, 0, 255, 255, colkey = 8)

            # Background color.
            pyxel.cls(1)

            pyxel.blt(40, 50, 0, 1, 209, 177, 45, colkey = 8)
            pyxel.text(55, 140, '>> PRESS ENTER TO START THE GAME', 7)
            pyxel.text(55, 152, '>> PRESS ESC OR Q TO QUIT THE GAME', 7)
            pyxel.blt(95, 190, 0, 1, 192, 64, 16, colkey = 8)
        
        # Animations when the player loses a life.
        if self.loose_life:
            # Background image.
            #pyxel.blt(0, 0, 2, 0, 0, 255, 255, colkey = 8)

            # Background color.
            #pyxel.cls(1)

            pyxel.blt(40, 50, 0, 1, 209, 177, 45, colkey = 8)
            pyxel.text(55, 128, 'YOU HAVE LOST A LIFE', 7)
            pyxel.text(55, 140, '>> PRESS ENTER TO CONTINUE', 7)
            pyxel.text(55, 152, '>> PRESS ESC OR Q TO QUIT THE GAME', 7)
            pyxel.blt(95, 190, 0, 1, 192, 64, 16, colkey = 8)


    def generate_enemigos(self):
        '''Method for generating enemies following a random distribution.'''

        enemy_1_count = 0    # Variable to ensure that we have the minimum number of regular enemies.
        enemy_2_count = 0    # Variable to ensure that we have the minimum number of red enemies.
        enemy_3_count = 0    # Variable to ensure that we have the minimum number of bomber enemies.
        enemy_4_count = 0    # Variable to ensure that we have the minimum number of superbomber enemies.

        
        while (enemy_1_count < ENEMIES1_MIN) or (enemy_2_count < ENEMIES2_MIN) or (enemy_3_count < ENEMIES3_MIN) or (enemy_4_count < ENEMIES4_MIN):
            # Regular enemies are generated (formations of 10 or 20).
            generate = random.randrange(0, 21, 10)
            enemy_1_count += generate
            while generate != 0:
                random_position = random.randint(16, self.width - 16)
                self.inactive_enemies.append(RegularEnemy(random_position, -15))
                generate -= 1
            
            # Red enemies are generated (formations of 5).
            generate = random.randrange(0, 6, 5)
            if generate != 0:
                counter = 5
                random_position = random.randint(80, self.height - 80)
                enemigo_1 = RedEnemy(-15, random_position)
                
                while counter > 0:
                    enemy = copy.deepcopy(enemigo_1)
                    self.inactive_enemies.append(enemy)
                    counter -= 1

                enemy_2_count += generate

            # Bombers are generated (individual).
            generate = random.randint(0, 3)
            enemy_3_count += generate
            while generate != 0:
                random_position = random.randint(30, self.width - 30)
                self.inactive_enemies.append(Bomber(random_position, -24))
                generate -= 1
            
            # Superbombers are generated (individual).
            generate = random.randint(0, 1)
            enemy_4_count += generate
            while generate != 0:
                random_position = random.randint(70, self.width - 70)
                self.inactive_enemies.append(Superbomber(random_position, self.height + 1))
                generate -= 1

        '''
        # Test for enemies generation.
        print('enemies THAT WILL BE GENERATED')
        print('Regular enemies: ', enemy_1_count)
        print('Red enemies: ',  enemy_2_count)
        print('Bombers: ', enemy_3_count)
        print('Superbombers: ', enemy_4_count)
        '''


    def stop_game(self):
        '''Method to stop the game if the user loses a life.'''

        self.loose_life = True
        self.start_condition = False
        self.plane.lives -= 1

        enemies_copy = self.enemies.copy()
        self.plane.shots = []

        for enemy in enemies_copy:
            self.enemies.remove(enemy)
            enemy.reset()
            self.inactive_enemies.append(enemy)
        