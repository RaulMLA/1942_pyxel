import random
from enemigos import Enemigo
from enemigoregular import EnemigoRegular
from enemigorojo import EnemigoRojo
from bombardero import Bombardero
from fondo import Fondo
from superbombardero import Superbombardero
from plane import Plane
from disparo import Disparo
import pyxel
import copy
from config import *


class Board:
    '''Clase que representa el tablero.'''

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

        # Metemos los distintos tipos de enemigos en una lista.
        self.enemigos = []
        self.enemigos_inactivos = []

        # Islas del fondo.
        self.fondo = Fondo()

        # Generamos los enemigos.
        self.generar_enemigos()

        # Variable de control para la generación de enemigos.
        self.random_number = random.randint(50, 100)

        # Variable de control para el bonus por eliminar enemigos rojos.
        self.bonus = False

        # Contador para comprobar el número de enemigos rojos destruidos para el bonus.
        self.red_counter = 0

        # Música de fondo.
        pyxel.play(0, 1, 1, True)
        pyxel.play(0, 2, 1, True)
        pyxel.play(0, 3, 1, True)

        # Condición de inicio del juego.
        self.start_condition = True

        # El jugador ha perdido una vida.
        self.loose_life = False

        # El jugador ha perdido la partida.
        self.loose = False

        # Ejecutamos el juego.
        pyxel.run(self.update, self.draw)


    def update(self):
        '''
        Función que actualiza el estado del tablero.
        (*) Hay bucles de enemigos que se podrían optimizar fusionándolos en uno solo,
        pero se han considerado separados para facilitar la lectura y comprensión del código.
        '''

        # Letra ENTER para empezar a jugar.
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.start_condition = True

        # Jugador sale del juego pulsando la tecla Q.
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

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

            # Puesta en marcha de los enemigos.
            if (pyxel.frame_count + 1) % self.random_number == 0 and len(self.enemigos_inactivos) > 0:
                enemigo = self.enemigos_inactivos.pop(0)
                # Los enemigos rojos se generan en grupos múltiplos de 5 y aparecen seguidos en el mismo intervalo de tiempo.
                if enemigo.tipo == 'rojo':
                    self.random_number = 10
                    if len(self.enemigos_inactivos) > 0:
                        if self.enemigos_inactivos[0].tipo != 'rojo':
                            self.random_number = random.randint(100, 300)
                # Los enemigos regulares se generan en grupos múltiplos de 10 y aparecen seguidos en el mismo intervalo de tiempo.
                elif enemigo.tipo == 'regular':
                    self.random_number = 20
                    if len(self.enemigos_inactivos) > 0:
                        if self.enemigos_inactivos[0].tipo != 'regular':
                            self.random_number = random.randint(100, 300)
                elif enemigo.tipo == 'bombardero':
                    self.random_number = 100
                    if len(self.enemigos_inactivos) > 0:
                        if self.enemigos_inactivos[0].tipo != 'bombardero':
                            self.random_number = random.randint(100, 300)    
                else:
                    self.random_number = random.randint(100, 300)
                
                # Ponemos en funcionamiento al enemigo.
                self.enemigos.append(enemigo)

            # Creación de un disparo por parte del jugador.
            if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_S):
                if self.bonus:
                    self.plane.disparos.append(Disparo(self.plane.x, self.plane.y, 'plane', 'up'))
                    self.plane.disparos.append(Disparo(self.plane.x + 15, self.plane.y, 'plane', 'up'))
                else:
                    self.plane.disparos.append(Disparo(self.plane.x + 7, self.plane.y, 'plane', 'up'))

            # Movimiento de los disparos del jugador.
            for i in range(len(self.plane.disparos)):
                self.plane.disparos[i].move()

            # Disparos y frecuencias dependiendo del tipo de enemigo.
            for enemigo in self.enemigos:
                # Enemigo regular.
                if enemigo.tipo == 'regular':
                    if random.randint(1, 100) < 4 and enemigo.direction != 'up':
                        enemigo.disparos.append(Disparo(enemigo.x + 5, enemigo.y, 'enemigo', enemigo.direction))
                # Enemigo rojo.
                elif enemigo.tipo == 'rojo':
                    if random.randint(1, 100) < 2:
                        enemigo.disparos.append(Disparo(enemigo.x + 10, enemigo.y, 'enemigo', enemigo.direction))
                # Enemigo bombardero.
                elif enemigo.tipo == 'bombardero':
                    if random.randint(1, 100) < 3 and enemigo.direction not in ['up', 'upleft', 'upright']:
                        enemigo.disparos.append(Disparo(enemigo.x + 20, enemigo.y, 'enemigo', enemigo.direction))
                # Enemigo superbombardero.
                elif enemigo.tipo == 'superbombardero':
                    if random.randint(1, 100) < 4 and enemigo.y < 200:
                        # Se generan en grupos de 3 con diferentes direcciones.
                        enemigo.disparos.append(Disparo(enemigo.x + 30, enemigo.y + 30, 'enemigo', 'downleft'))
                        enemigo.disparos.append(Disparo(enemigo.x + 30, enemigo.y + 30, 'enemigo', 'down'))
                        enemigo.disparos.append(Disparo(enemigo.x + 30, enemigo.y + 30, 'enemigo', 'downright'))
                    
                for disparo in enemigo.disparos:
                    disparo.move()

            # Si el jugador tiene bonus de tiro doble, se elimina pasado un tiempo.
            if pyxel.frame_count % 250 == 0 and self.bonus:
                    self.bonus = False

            # Eliminamos los disparos del avión que salen de la pantalla.
            for disparo in self.plane.disparos:
                if disparo.y < -8:
                    self.plane.disparos.remove(disparo)

            # Eliminamos los disparos de los enemigos que salen de la pantalla.
            for enemigo in self.enemigos:
                for disparo in enemigo.disparos:
                    if disparo.y > self.height or disparo.y < -8 or disparo.x < -8 or disparo.x > self.width:
                        enemigo.disparos.remove(disparo)
            
            # Eliminamos los enemigos que salen de la pantalla.
            for enemigo in self.enemigos:
                if enemigo.y > self.height or enemigo.y < -50 or enemigo.x < -50 or enemigo.x > self.width:
                    self.enemigos.remove(enemigo)
            
            # Movimiento de las islas del fondo.
            self.fondo.move()

            # Movimiento de los enemigos.
            for enemigo in self.enemigos:
                enemigo.move()

            # Colisión entre disparos y enemigos.
            for disparo in self.plane.disparos:
                for enemigo in self.enemigos:
                    if enemigo.comprobar_colision(disparo.x, disparo.y):
                        self.plane.disparos.remove(disparo)
                        if enemigo.lives <= 0:
                            # Comprobamos si es rojo y si se han destruido todos los rojos de una tanda para el bonus.
                            if enemigo.tipo == 'rojo':
                                self.red_counter += 1
                                if self.red_counter == 5:
                                    self.bonus = True
                                    self.plane.loops += 2
                                    self.red_counter = 0
                            elif enemigo.tipo != 'rojo' and self.red_counter > 0:
                                self.red_counter = 0
                            # Efecto de sonido de destrucción de enemigo.
                            pyxel.play(1, 5)
                            self.marcador_1up += enemigo.score
                            self.enemigos.remove(enemigo)
            
            # Colisión entre disparos y jugador.
            for enemigo in self.enemigos:
                for disparo in enemigo.disparos:
                    if (int(disparo.x) in range (int(self.plane.x - 5), int(self.plane.x + 24))) and (int(disparo.y) in range (int(self.plane.y), int(self.plane.y + 16))) and not self.plane.loop:
                        enemigo.disparos.remove(disparo)
                        # Efecto de sonido de disparo acertado a enemigo.
                        pyxel.play(1, 0)
                        self.stop_game()
            
            # Colisión entre jugador y enemigos.
            for enemigo in self.enemigos:
                if (int(self.plane.x) in range (int(enemigo.x) - 5, int(enemigo.x) + 16) and (int(self.plane.y) in range (int(enemigo.y) - 16, int(enemigo.y) + 16))):
                    # Efecto de sonido de colisión con enemigo.
                    pyxel.play(1, 4)
                    self.stop_game()
                        

            # Animación del avión.
            self.plane.animation()

            # Animación de los enemigos.
            for i in range (len(self.enemigos)):
                self.enemigos[i].animation()


    def draw(self):
        '''Método que permite dibujar cada elemento en la ventana.'''

        if self.start_condition:

            # Imagen de fondo.
            #pyxel.blt(0, 0, 2, 0, 0, 255, 255, colkey = 8)

            # Color de fondo.
            pyxel.cls(1)

            # Dibujamos las islas.
            for isla in self.fondo.islas:
                pyxel.blt(isla.x, isla.y, *isla.sprite, colkey = 8)

            # Dibujamos los marcadores de puntuación.
            pyxel.text(15, 5, "1 U P", 7)
            pyxel.text(90, 5, "H I G H  S C O R E", 10)
            pyxel.text(205, 5, "L I V E S", 14)

            pyxel.text(15, 15, str(self.marcador_1up), 13)
            pyxel.text(90, 15, str(self.marcador_highscore), 13)
            pyxel.text(205, 15, str(self.plane.lives), 13)

            # Dibujamos el avión.
            pyxel.blt(self.plane.x, self.plane.y, *self.plane.sprite, colkey = 8)

            # Dibujamos los enemigos.
            for enemigo in self.enemigos:
                pyxel.blt(enemigo.x, enemigo.y, *enemigo.sprite, 8)

            # Dibujamos los disparos de los enemigos.
            for enemigo in self.enemigos:
                for disparo in enemigo.disparos:
                    pyxel.blt(disparo.x, disparo.y, *disparo.sprite, 8)

            # Dibujamos los disparos del avión.
            for disparo in self.plane.disparos:
                pyxel.blt(disparo.x, disparo.y, *disparo.sprite, 8)

            # Animación final.
            if self.plane.lives == 0:
                self.loose = True
                # Imagen de fondo.
                #pyxel.blt(0, 0, 2, 0, 0, 255, 255, colkey = 8)

                # Color de fondo.
                pyxel.cls(1)

                pyxel.blt(40, 50, 0, 1, 209, 177, 45, colkey = 8)
                pyxel.text(95, 125, '--- GAME OVER ---', 7)
                pyxel.text(105, 152, 'HAS PERDIDO', 7)
                pyxel.blt(95, 188, 0, 1, 192, 64, 16, colkey = 8)

            if len(self.enemigos_inactivos) == 0 and len(self.enemigos) == 0 and not self.loose:
                # Imagen de fondo.
                #pyxel.blt(0, 0, 2, 0, 0, 255, 255, colkey = 8)

                # Color de fondo.
                pyxel.cls(1)

                pyxel.blt(40, 50, 0, 1, 209, 177, 45, colkey = 8)
                pyxel.text(93, 125, '--- GAME OVER ---', 7)
                pyxel.text(108, 152, 'HAS GANADO', 7)
                pyxel.text(99, 164, 'PUNTUACION: ' + str(self.marcador_1up), 7)
                pyxel.blt(95, 200, 0, 1, 192, 64, 16, colkey = 8)

        # Animación inicial.
        if self.loose_life:
            # Imagen de fondo.
            #pyxel.blt(0, 0, 2, 0, 0, 255, 255, colkey = 8)

            # Color de fondo.
            pyxel.cls(1)

            pyxel.blt(40, 50, 0, 1, 209, 177, 45, colkey = 8)
            pyxel.text(55, 140, '>> PULSA ENTER PARA EMPEZAR EL JUEGO', 7)
            pyxel.text(55, 152, '>> PULSA ESC O Q PARA QUITAR EL JUEGO', 7)
            pyxel.blt(95, 190, 0, 1, 192, 64, 16, colkey = 8)
        
        # Animación jugador pierde una vida.
        if not self.start_condition and self.plane.lives < PLAYER_LIVES:
            # Imagen de fondo.
            #pyxel.blt(0, 0, 2, 0, 0, 255, 255, colkey = 8)

            # Color de fondo.
            pyxel.cls(1)

            pyxel.blt(40, 50, 0, 1, 209, 177, 45, colkey = 8)
            pyxel.text(55, 128, 'HAS PERDIDO UNA VIDA', 7)
            pyxel.text(55, 140, '>> PULSA ENTER PARA CONTINUAR', 7)
            pyxel.text(55, 152, '>> PULSA ESC O Q PARA QUITAR EL JUEGO', 7)
            pyxel.blt(95, 190, 0, 1, 192, 64, 16, colkey = 8)


    def generar_enemigos(self):
        '''Método para generar los enemigos siguiendo una distribución aleatoria.'''

        count_enemigos_1 = 0    # Variable para asegurarnos de contar con el número mínimo de enemigos regulaares.
        count_enemigos_2 = 0    # Variable para asegurarnos de contar con el número mínimo de enemigos rojos.
        count_enemigos_3 = 0    # Variable para asegurarnos de contar con el número mínimo de enemigos bombarderos.
        count_enemigos_4 = 0    # Variable para asegurarnos de contar con el número mínimo de enemigos superbombarderos.

        while (count_enemigos_1 < ENEMIGOS1_MIN) or (count_enemigos_2 < ENEMIGOS2_MIN) or (count_enemigos_3 < ENEMIGOS3_MIN) or (count_enemigos_4 < ENEMIGOS4_MIN):
            # Generación de enemigos regulares (formaciones de 10 o 20).
            generar = random.randrange(0, 21, 10)
            count_enemigos_1 += generar
            while generar != 0:
                random_position = random.randint(16, self.width - 16)
                self.enemigos_inactivos.append(EnemigoRegular(random_position, 0))
                generar -= 1
            
            # Generación de enemigos rojos (formación de 5).
            generar = random.randrange(0, 6, 5)
            if generar != 0:
                random_position = random.randint(80, self.height - 80)
                enemigo_1 = EnemigoRojo(0, random_position)
                enemigo_2 = copy.deepcopy(enemigo_1)
                enemigo_3 = copy.deepcopy(enemigo_1)
                enemigo_4 = copy.deepcopy(enemigo_1)
                enemigo_5 = copy.deepcopy(enemigo_1)
                self.enemigos_inactivos.append(enemigo_1)
                self.enemigos_inactivos.append(enemigo_2)
                self.enemigos_inactivos.append(enemigo_3)
                self.enemigos_inactivos.append(enemigo_4)
                self.enemigos_inactivos.append(enemigo_5)
                count_enemigos_2 += generar

            # Generación de bombarderos (se generan de manera individual).
            generar = random.randint(0, 3)
            count_enemigos_3 += generar
            while generar != 0:
                random_position = random.randint(30, self.width - 30)
                self.enemigos_inactivos.append(Bombardero(random_position, 0))
                generar -= 1
            
            # Generación de superbombarderos (se generan de manera individual).
            generar = random.randint(0, 1)
            count_enemigos_4 += generar
            while generar != 0:
                random_position = random.randint(70, self.width - 70)
                self.enemigos_inactivos.append(Superbombardero(random_position, self.height))
                generar -= 1

        '''
        # Se muestra en pantalla cuantos enemigos de cada tipo se van a generar en el juego.
        print('ENEMIGOS QUE SE VAN A GENERAR')
        print('Enemigos regulares: ', count_enemigos_1)
        print('Enemigos rojos: ',  count_enemigos_2)
        print('Bombarderos: ', count_enemigos_3)
        print('Superbombarderos: ', count_enemigos_4)
        '''


    def stop_game(self):
        '''Método para detener el juego si el usuario pierde una vida.'''

        enemis = self.enemigos.copy()
        self.plane.disparos = []

        for enemigo in enemis:
            self.enemigos.remove(enemigo)
            enemigo.reset()
            self.enemigos_inactivos.append(enemigo)
        
        self.loose_life = True
        self.start_condition = False
        self.plane.lives -= 1
