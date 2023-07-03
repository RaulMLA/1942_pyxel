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
        '''Inicialización del tablero con sus medidas y carga del banco de imágenes.'''

        # Dimensiones del tablero.
        self.width = w
        self.height = h

        # Marcadores de puntuación.
        self.marcador_1up = 0
        self.marcador_highscore = 40000

        # Ventana y assets.
        pyxel.init(self.width, self.height, title = "1942")
        pyxel.load("assets/my_resource.pyxres")

        # Posición inicial de nuestro jugador.
        self.plane = Plane(self.width / 2, 200)

        # Metemos los distintos tipos de enemies en una lista.
        self.enemies = []
        self.enemigos_inactivos = []

        # Islas del background.
        self.background = Background()

        # Generamos los enemies.
        self.generar_enemigos()

        # Explosiones de los enemies.
        self.explosiones = []

        # Variable de control para la generación de enemies.
        self.random_number = random.randint(50, 100)

        # Variable de control para el bonus por eliminar enemies rojos.
        self.bonus = False

        # Contador para comprobar el número de enemies rojos destruidos para el bonus.
        self.red_counter = 0

        # Música de background.
        pyxel.play(0, 1, 1, True)
        pyxel.play(0, 2, 1, True)
        pyxel.play(0, 3, 1, True)

        # Condición de inicio del juego.
        self.start_condition = False

        # El jugador ha perdido una vida.
        self.loose_life = False

        # El jugador ha perdido la partida.
        self.loose = False

        # Ejecutamos el juego.
        pyxel.run(self.update, self.draw)


    def update(self):
        '''
        Método que actualiza el estado del tablero.
        (*) Hay bucles de enemies que se podrían optimizar fusionándolos en uno solo,
        pero se han considerado separados para facilitar la lectura y comprensión del código.
        '''

        # Letra ENTER para empezar a jugar.
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.start_condition = True

        # Jugador sale del juego pulsando la tecla Q.
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        # Control de explosiones.
        for explosion in self.explosiones:
            if explosion.max < pyxel.frame_count:
                self.explosiones.remove(explosion)
        
        if self.start_condition:
            # Reestablecemos la configuración si el usuario ha perdido una vida.
            if self.loose_life:
                self.random_number = random.randint(50, 100)
                self.plane.x = self.width / 2
                self.plane.y = 200
                self.loose_life = False

            # Movimiento del jugador (derecha e izquierda).
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.plane.move('right', self.width)
            elif pyxel.btn(pyxel.KEY_LEFT):
                self.plane.move('left', self.width)
            
            # Movimiento del jugador (arriba y abajo).
            if pyxel.btn(pyxel.KEY_UP):
                self.plane.move('up', self.width)
            elif pyxel.btn(pyxel.KEY_DOWN):
                self.plane.move('down', self.width)

            # Movimiento loop del jugador para evitar ser abatido.
            if pyxel.btn(pyxel.KEY_Z):
                if self.plane.loops > 0:
                    self.plane.make_loop()
                
            # Tiempo máximo que dura un loop.
            if self.plane.make_loop:
                if pyxel.frame_count % 45 == 0:
                    if self.plane.loop:
                        self.plane.loops -= 1
                        self.plane.loop = False    

            # Puesta en marcha de los enemies.
            if (pyxel.frame_count + 1) % self.random_number == 0 and len(self.enemigos_inactivos) > 0:
                enemy = self.enemigos_inactivos.pop(0)
                # Los enemies rojos se generan en grupos múltiplos de 5 y aparecen seguidos en el mismo intervalo de tiempo.
                if enemy.type == 'red':
                    self.random_number = 10
                    if len(self.enemigos_inactivos) > 0:
                        if self.enemigos_inactivos[0].type != 'red':
                            self.random_number = random.randint(100, 300)
                # Los enemies regulares se generan en grupos múltiplos de 10 y aparecen seguidos en el mismo intervalo de tiempo.
                elif enemy.type == 'regular':
                    self.random_number = 20
                    if len(self.enemigos_inactivos) > 0:
                        if self.enemigos_inactivos[0].type != 'regular':
                            self.random_number = random.randint(100, 300)
                elif enemy.type == 'bomber':
                    self.random_number = 100
                    if len(self.enemigos_inactivos) > 0:
                        if self.enemigos_inactivos[0].type != 'bomber':
                            self.random_number = random.randint(100, 300)    
                else:
                    self.random_number = random.randint(100, 300)
                
                # Ponemos en funcionamiento al enemy.
                self.enemies.append(enemy)

            # Creación de un shot por parte del jugador.
            if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_S):
                if self.bonus:
                    self.plane.shots.append(Shot(self.plane.x, self.plane.y, 'plane', 'up'))
                    self.plane.shots.append(Shot(self.plane.x + 15, self.plane.y, 'plane', 'up'))
                else:
                    self.plane.shots.append(Shot(self.plane.x + 7, self.plane.y, 'plane', 'up'))
                # Sonido de shot.
                pyxel.play(1, 6)

            # Movimiento de los shots del jugador.
            for i in range(len(self.plane.shots)):
                self.plane.shots[i].move()

            # Disparos y frecuencias dependiendo del type de enemy.
            for enemy in self.enemies:
                # enemy regular.
                if enemy.type == 'regular':
                    if random.randint(1, 100) < 4 and enemy.direction != 'up':
                        enemy.shots.append(Shot(enemy.x + 5, enemy.y, 'enemy', enemy.direction))
                # enemy red.
                elif enemy.type == 'red':
                    if random.randint(1, 100) < 2:
                        enemy.shots.append(Shot(enemy.x + 10, enemy.y, 'enemy', enemy.direction))
                # enemy bomber.
                elif enemy.type == 'bomber':
                    if random.randint(1, 100) < 3 and enemy.direction not in ['up', 'upleft', 'upright']:
                        enemy.shots.append(Shot(enemy.x + 20, enemy.y, 'enemy', enemy.direction))
                # enemy superbomber.
                elif enemy.type == 'superbomber':
                    if random.randint(1, 100) < 4 and enemy.y < 200:
                        # Se generan en grupos de 3 con diferentes direcciones.
                        enemy.shots.append(Shot(enemy.x + 30, enemy.y + 30, 'enemy', 'downleft'))
                        enemy.shots.append(Shot(enemy.x + 30, enemy.y + 30, 'enemy', 'down'))
                        enemy.shots.append(Shot(enemy.x + 30, enemy.y + 30, 'enemy', 'downright'))
            
                for shot in enemy.shots:
                    shot.move()

            # Si el jugador tiene bonus de tiro doble, se elimina pasado un tiempo.
            if pyxel.frame_count % 250 == 0 and self.bonus:
                    self.bonus = False

            # Eliminamos los shots del avión que salen de la pantalla.
            for shot in self.plane.shots:
                if shot.y < -8:
                    self.plane.shots.remove(shot)

            # Eliminamos los shots de los enemies que salen de la pantalla.
            for enemy in self.enemies:
                for shot in enemy.shots:
                    if shot.y > self.height or shot.y < -8 or shot.x < -8 or shot.x > self.width:
                        enemy.shots.remove(shot)
            
            # Eliminamos los enemies que salen de la pantalla.
            for enemy in self.enemies:
                if enemy.y > self.height or enemy.y < -50 or enemy.x < -50 or enemy.x > self.width:
                    self.enemies.remove(enemy)
            
            # Movimiento de las islands del background.
            self.background.move()

            # Movimiento de los enemies.
            for enemy in self.enemies:
                enemy.move()

            # Colisión entre shots y enemies.
            for shot in self.plane.shots:
                for enemy in self.enemies:
                    if enemy.check_colision(shot.x, shot.y, 'shot'):
                        self.plane.shots.remove(shot)
                        if enemy.lives <= 0:
                            # Comprobamos si es red y si se han destruido todos los rojos de una tanda para el bonus.
                            if enemy.type == 'red':
                                self.red_counter += 1
                                if self.red_counter == 5:
                                    self.bonus = True
                                    self.plane.loops += 2
                                    self.red_counter = 0
                            elif enemy.type != 'red' and self.red_counter > 0:
                                self.red_counter = 0
                            # Efecto de sonido de destrucción de enemy.
                            pyxel.play(1, 5)
                            self.marcador_1up += enemy.score
                            self.enemies.remove(enemy)
                            self.explosiones.append(Explosion(enemy.x, enemy.y, enemy.type))
            
            # Colisión entre shots y jugador.
            for enemy in self.enemies:
                for shot in enemy.shots:
                    if self.plane.check_colision(shot.x, shot.y) and not self.plane.loop:
                        enemy.shots.remove(shot)
                        self.explosiones.append(Explosion(self.plane.x, self.plane.y, 'plane'))
                        # Efecto de sonido de shot acertado a enemy.
                        pyxel.play(1, 0)
                        self.stop_game()
            
            # Colisión entre jugador y enemies.
            for enemy in self.enemies:
                if enemy.check_colision(self.plane.x, self.plane.y, 'plane') and not self.plane.loop:
                    self.explosiones.append(Explosion(self.plane.x, self.plane.y, 'plane'))
                    # Efecto de sonido de colisión con enemy.
                    pyxel.play(1, 4)
                    self.stop_game()

            # Animación del avión.
            self.plane.animation()

            # Animación de los enemies.
            for i in range (len(self.enemies)):
                self.enemies[i].animation()
    

    def draw(self):
        '''Método que permite dibujar cada elemento en la ventana.'''

        if self.start_condition:

            # Imagen de background.
            #pyxel.blt(0, 0, 2, 0, 0, 255, 255, colkey = 8)

            # Color de background.
            pyxel.cls(1)

            # Dibujamos las islands.
            for island in self.background.islands:
                pyxel.blt(island.x, island.y, *island.sprite, colkey = 8)

            # Dibujamos los marcadores de puntuación.
            pyxel.text(15, 5, "1 U P", 7)
            pyxel.text(60, 5, "H I G H  S C O R E", 10)
            pyxel.text(155, 5, "L O O P S", 11)
            pyxel.text(210, 5, "L I V E S", 14)

            pyxel.text(15, 15, str(self.marcador_1up), 13)
            pyxel.text(60, 15, str(self.marcador_highscore), 13)
            pyxel.text(155, 15, str(self.plane.loops), 13)
            pyxel.text(210, 15, str(self.plane.lives), 13)

            # Dibujamos el avión.
            pyxel.blt(self.plane.x, self.plane.y, *self.plane.sprite, colkey = 8)

            # Dibujamos los enemies.
            for enemy in self.enemies:
                pyxel.blt(enemy.x, enemy.y, *enemy.sprite, 8)

            # Dibujamos los shots de los enemies.
            for enemy in self.enemies:
                for shot in enemy.shots:
                    pyxel.blt(shot.x, shot.y, *shot.sprite, 8)

            # Dibujamos los shots del avión.
            for shot in self.plane.shots:
                pyxel.blt(shot.x, shot.y, *shot.sprite, 8)

            # Animación final.
            if self.plane.lives == 0:
                self.loose = True
                # Imagen de background.
                #pyxel.blt(0, 0, 2, 0, 0, 255, 255, colkey = 8)

                # Color de background.
                pyxel.cls(1)

                pyxel.blt(40, 50, 0, 1, 209, 177, 45, colkey = 8)
                pyxel.text(95, 125, '--- GAME OVER ---', 7)
                pyxel.text(105, 152, 'YOU LOOSE', 7)
                pyxel.blt(95, 188, 0, 1, 192, 64, 16, colkey = 8)

            if len(self.enemigos_inactivos) == 0 and len(self.enemies) == 0 and not self.loose:
                # Imagen de background.
                #pyxel.blt(0, 0, 2, 0, 0, 255, 255, colkey = 8)

                # Color de background.
                pyxel.cls(1)

                pyxel.blt(40, 50, 0, 1, 209, 177, 45, colkey = 8)
                pyxel.text(93, 125, '--- GAME OVER ---', 7)
                pyxel.text(108, 152, 'YOU WIN', 7)
                pyxel.text(99, 164, 'SCORE: ' + str(self.marcador_1up), 7)
                pyxel.blt(95, 200, 0, 1, 192, 64, 16, colkey = 8)
        
        # Dibujamos las explosiones.
        for explosion in self.explosiones:
            pyxel.blt(explosion.x, explosion.y, *explosion.sprite, 8)

        # Animación inicial.
        if not self.start_condition and not self.loose and not self.loose_life:
            # Imagen de background.
            #pyxel.blt(0, 0, 2, 0, 0, 255, 255, colkey = 8)

            # Color de background.
            pyxel.cls(1)

            pyxel.blt(40, 50, 0, 1, 209, 177, 45, colkey = 8)
            pyxel.text(55, 140, '>> PRESS ENTER TO START THE GAME', 7)
            pyxel.text(55, 152, '>> PRESS ESC OR Q TO QUIT THE GAME', 7)
            pyxel.blt(95, 190, 0, 1, 192, 64, 16, colkey = 8)
        
        # Animación cuando el jugador pierde una vida.
        if self.loose_life:
            # Imagen de background.
            #pyxel.blt(0, 0, 2, 0, 0, 255, 255, colkey = 8)

            # Color de background.
            #pyxel.cls(1)

            pyxel.blt(40, 50, 0, 1, 209, 177, 45, colkey = 8)
            pyxel.text(55, 128, 'YOU HAVE LOST A LIFE', 7)
            pyxel.text(55, 140, '>> PRESS ENTER TO CONTINUE', 7)
            pyxel.text(55, 152, '>> PRESS ESC OR Q TO QUIT THE GAME', 7)
            pyxel.blt(95, 190, 0, 1, 192, 64, 16, colkey = 8)


    def generar_enemigos(self):
        '''Método para generar los enemies siguiendo una distribución aleatoria.'''

        count_enemigos_1 = 0    # Variable para asegurarnos de contar con el número mínimo de enemies regulaares.
        count_enemigos_2 = 0    # Variable para asegurarnos de contar con el número mínimo de enemies rojos.
        count_enemigos_3 = 0    # Variable para asegurarnos de contar con el número mínimo de enemies bombarderos.
        count_enemigos_4 = 0    # Variable para asegurarnos de contar con el número mínimo de enemies superbombarderos.

        
        while (count_enemigos_1 < ENEMIES1_MIN) or (count_enemigos_2 < ENEMIES2_MIN) or (count_enemigos_3 < ENEMIES3_MIN) or (count_enemigos_4 < ENEMIES4_MIN):
            # Generación de enemies regulares (formaciones de 10 o 20).
            generar = random.randrange(0, 21, 10)
            count_enemigos_1 += generar
            while generar != 0:
                random_position = random.randint(16, self.width - 16)
                self.enemigos_inactivos.append(RegularEnemy(random_position, -15))
                generar -= 1
            
            # Generación de enemies rojos (formación de 5).
            generar = random.randrange(0, 6, 5)
            if generar != 0:
                counter = 5
                random_position = random.randint(80, self.height - 80)
                enemigo_1 = RedEnemy(-15, random_position)
                
                while counter > 0:
                    enemy = copy.deepcopy(enemigo_1)
                    self.enemigos_inactivos.append(enemy)
                    counter -= 1

                count_enemigos_2 += generar

            # Generación de bombarderos (se generan de manera individual).
            generar = random.randint(0, 3)
            count_enemigos_3 += generar
            while generar != 0:
                random_position = random.randint(30, self.width - 30)
                self.enemigos_inactivos.append(Bomber(random_position, -24))
                generar -= 1
            
            # Generación de superbombarderos (se generan de manera individual).
            generar = random.randint(0, 1)
            count_enemigos_4 += generar
            while generar != 0:
                random_position = random.randint(70, self.width - 70)
                self.enemigos_inactivos.append(Superbomber(random_position, self.height + 1))
                generar -= 1

        '''
        # Se muestra en pantalla cuantos enemies de cada type se van a generar en el juego.
        print('enemies QUE SE VAN A GENERAR')
        print('enemies regulares: ', count_enemigos_1)
        print('enemies rojos: ',  count_enemigos_2)
        print('Bombarderos: ', count_enemigos_3)
        print('Superbombarderos: ', count_enemigos_4)
        '''


    def stop_game(self):
        '''Método para detener el juego si el usuario pierde una vida.'''

        self.loose_life = True
        self.start_condition = False
        self.plane.lives -= 1

        copia_enemigos = self.enemies.copy()
        self.plane.shots = []

        for enemy in copia_enemigos:
            self.enemies.remove(enemy)
            enemy.reset()
            self.enemigos_inactivos.append(enemy)
        