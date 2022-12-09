import random
from enemigos import Enemigo
from enemigoregular import EnemigoRegular
from enemigorojo import EnemigoRojo
from bombardero import Bombardero
from superbombardero import Superbombardero
from plane import Plane
from disparo import Disparo
import pyxel


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

        '''# 20 aviones regulares.
        for i in range (0, 20):
            random_position = random.randint(16, self.width - 16)
            self.enemigos_inactivos.append(EnemigoRegular(random_position, 0))'''
        
        '''# 5 aviones rojos.
        random_position = random.randint(80, self.height - 80)
        for i in range (0, 5):
            self.enemigos_inactivos.append(EnemigoRojo(0, random_position))'''
        
        '''# 2 bombarderos.
        for i in range (0, 1):
            random_position = random.randint(30, self.width - 30)
            self.enemigos_inactivos.append(Bombardero(random_position, 0))'''
        
        # 1 superbombardero.
        random_position = random.randint(70, self.width - 70)
        self.enemigos_inactivos.append(Superbombardero(random_position, self.height))

        # Música de fondo.
        pyxel.play(0, 1, 1, True)
        pyxel.play(0, 2, 1, True)
        pyxel.play(0, 3, 1, True)

        # Ejecutamos el juego.
        pyxel.run(self.update, self.draw)


    def update(self):
        '''Función que actualiza el estado del tablero.'''

        # Jugador sale del juego pulsando la tecla Q.
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

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

        # Creación de un disparo por parte del jugador.
        if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_S):
            self.plane.disparos.append(Disparo(self.plane.x + 7, self.plane.y, 'plane', 'up'))
        
        # Movimiento de los disparos del jugador.
        for i in range(len(self.plane.disparos)):
            self.plane.disparos[i].move()

        # Disparos y frecuencias dependiendo del tipo de enemigo.
        for i in range (len(self.enemigos)):
            # Enemigo regular.
            if self.enemigos[i].tipo == 'regular':
                if random.randint(1, 100) < 4 and self.enemigos[i].direction != 'up':
                    self.enemigos[i].disparos.append(Disparo(self.enemigos[i].x + 5, self.enemigos[i].y, 'enemigo', self.enemigos[i].direction))
            # Enemigo rojo.
            elif self.enemigos[i].tipo == 'rojo':
                if random.randint(1, 100) < 2:
                    self.enemigos[i].disparos.append(Disparo(self.enemigos[i].x + 10, self.enemigos[i].y, 'enemigo', self.enemigos[i].direction))
            # Enemigo bombardero.
            elif self.enemigos[i].tipo == 'bombardero':
                if random.randint(1, 100) < 3 and self.enemigos[i].direction not in ['up', 'upleft', 'upright']:
                    self.enemigos[i].disparos.append(Disparo(self.enemigos[i].x + 20, self.enemigos[i].y, 'enemigo', self.enemigos[i].direction))
            # Enemigo superbombardero.
            elif self.enemigos[i].tipo == 'superbombardero':
                if random.randint(1, 100) < 4 and self.enemigos[i].y < 200:
                    # Se generan en grupos de 3 con diferentes direcciones.
                    self.enemigos[i].disparos.append(Disparo(self.enemigos[i].x + 30, self.enemigos[i].y + 30, 'enemigo', 'downleft'))
                    self.enemigos[i].disparos.append(Disparo(self.enemigos[i].x + 30, self.enemigos[i].y + 30, 'enemigo', 'down'))
                    self.enemigos[i].disparos.append(Disparo(self.enemigos[i].x + 30, self.enemigos[i].y + 30, 'enemigo', 'downright'))
                
            for d in range (len(self.enemigos[i].disparos)):
                self.enemigos[i].disparos[d].move()

        # Eliminamos los disparos del avión que salen de la pantalla.
        for i in range (len(self.plane.disparos)):
            try:
                if self.plane.disparos[i].y < -8:
                    self.plane.disparos.remove(self.plane.disparos[i])
            except:
                pass
        
        # Eliminamos los disparos de los enemigos que salen de la pantalla.
        for i in range (len(self.enemigos)):
            for d in range (len(self.enemigos[i].disparos)):
                try:
                    if self.enemigos[i].disparos[d].y > self.height:
                        self.enemigos[i].disparos.remove(self.enemigos[i].disparos[d])
                except:
                    pass
        
        # Puesta en marcha de los enemigos.
        random_number = random.randint(15, 30)
        if pyxel.frame_count % random_number == 0 and len(self.enemigos_inactivos) > 0:
            enemigo = self.enemigos_inactivos.pop(0)
            self.enemigos.append(enemigo)

        # Movimiento de los enemigos.
        for i in range (len(self.enemigos)):
            self.enemigos[i].move()

        # Colisión entre disparos y enemigos (usamos un try - except para evitar error de índice en actualización de frames).
        for d in range (len(self.plane.disparos)):
            for i in range (len(self.enemigos)):
                try:
                    if self.enemigos[i].comprobar_colision(self.plane.disparos[d].x, self.plane.disparos[d].y):
                        if self.enemigos[i].lives <= 0:
                            # Efecto de sonido de destrucción de enemigo.
                            pyxel.play(1, 0)
                            self.marcador_1up += self.enemigos[i].score
                            self.enemigos.remove(self.enemigos[i])
                        self.plane.disparos.remove(self.plane.disparos[d])

                except: pass
        
        # Colisión entre disparos y jugador (usamos un try - except para evitar error de índice en actualización de frames).
        for d in range (len(self.enemigos)):
            for i in range (len(self.enemigos[d].disparos)):
                try:
                    if (int(self.enemigos[d].disparos[i].x) in range (int(self.plane.x - 5), int(self.plane.x + 24))) and (int(self.enemigos[d].disparos[i].y) in range (int(self.plane.y), int(self.plane.y + 16))) and not self.plane.loop:
                        self.enemigos[d].disparos.remove(self.enemigos[d].disparos[i])
                        if (self.plane.lives - 1) == 0:
                            pyxel.quit()
                        else:
                            self.plane.lives -= 1
                        # Efecto de sonido de colisión con enemigo.
                        pyxel.play(1, 0)
                except: pass
        
        # Colisión entre jugador y enemigos (usamos un try - except para evitar error de índice en actualización de frames).
        for i in range (len(self.enemigos)):
            try:
                if (int(self.plane.x) in range (self.enemigos[i].x - 5, self.enemigos[i].x + 16) and (int(self.plane.y) in range (self.enemigos[i].y, self.enemigos[i].y + 16))):
                    if self.plane.lives == 0:
                        pyxel.quit()
                    else:
                        self.plane.lives -= 1
            except: pass

        # Animación del avión.
        self.plane.animation()

        # Animación de los enemigos.
        for i in range (len(self.enemigos)):
            self.enemigos[i].animation()


    def draw(self):
        '''Método que permite dibujar cada elemento en la ventana.'''

        # Imagen de fondo.
        #pyxel.blt(0, 0, 2, 0, 0, 255, 255, colkey = 8)

        # Color de fondo.
        pyxel.cls(1)

        # Dibujamos las islas.
        x = pyxel.frame_count % pyxel.width
        x = x + 1
        pyxel.blt(0, x, 1, 1, 1, 105, 125, colkey = 8)

        f = pyxel.frame_count % pyxel.width
        f = f + 2
        pyxel.blt(200, f, 1, 25, 127, 15, 15, colkey = 8)

        # Dibujamos los marcadores de puntuación.
        pyxel.text(15, 5, "1 U P", 7)
        pyxel.text(90, 5, "H I G H  S C O R E", 10)
        pyxel.text(215, 5, "2 U P", 7)

        pyxel.text(15, 15, str(self.marcador_1up), 13)
        pyxel.text(90, 15, str(self.marcador_highscore), 13)

        # Dibujamos el avión.
        pyxel.blt(self.plane.x, self.plane.y, *self.plane.sprite, colkey = 8)

        # Dibujamos los enemigos.
        for i in range (len(self.enemigos)):
            pyxel.blt(self.enemigos[i].x, self.enemigos[i].y, *self.enemigos[i].sprite, colkey = 8)
        
        # Dibujamos los disparos de los enemigos.
        for i in range (len(self.enemigos)):
            for d in range(len(self.enemigos[i].disparos)):
                pyxel.blt(self.enemigos[i].disparos[d].x, self.enemigos[i].disparos[d].y, *self.enemigos[i].disparos[d].sprite, colkey = 8)

        # Dibujamos los disparos del avión.
        for i in range(len(self.plane.disparos)):
            pyxel.blt(self.plane.disparos[i].x, self.plane.disparos[i].y, *self.plane.disparos[i].sprite, colkey = 8)
