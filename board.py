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
        self.marcador_highscore = 0

        # Ventana y assets.
        pyxel.init(self.width, self.height, title = "1942")
        pyxel.load("assets/my_resource.pyxres")

        # Posición inicial de nuestro jugador.
        self.plane = Plane(self.width / 2, 200)

        # Metemos los distintos tipos de enemigos en una lista.
        self.enemigos = []

        # 20 aviones regulares.
        for i in range (0, 1):
            random_position = random.randint(0, self.width)
            self.enemigos.append(EnemigoRegular(random_position, 0))
        
        '''# 5 aviones rojos.
        random_position = random.randint(0, self.width)
        for i in range (0, 5):
            self.enemigos.append(EnemigoRojo(random_position, 100))
        
        # 2 bombarderos.
        for i in range (0, 2):
            self.enemigos.append(Bombardero(self.width / 2, 100))
        
        # 1 superbombardero.
        self.enemigos.append(Superbombardero(self.width / 2, 100))'''

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

        # Creación, movimiento y control de un disparo por parte del jugador.
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.plane.disparos.append(Disparo(self.plane.x + 9, self.plane.y))
        
        for i in range(len(self.plane.disparos)):
            self.plane.disparos[i].move('up')

        '''Los disparos enemigos son random y se disparan en un intervalo no controlado.
        Cada disparo tiene que tener un porcentaje distinto dependiendo del tipo
        de enemigo.'''

        for i in range (len(self.enemigos)):
            if random.randint(1, 100) < 4:
                self.enemigos[i].disparos.append(Disparo(self.enemigos[i].x + 4, self.enemigos[i].y))
            for d in range (len(self.enemigos[i].disparos)):
                self.enemigos[i].disparos[d].move('down')

        # Eliminamos los disparos del avión que salen de la pantalla.
        for i in range (len(self.plane.disparos)):
            try:
                if self.plane.disparos[i].y < -8:
                    self.plane.disparos.remove(self.plane.disparos[i])
            except:
                pass

        # Movimiento de los enemigos.
        for i in range (len(self.enemigos)):
            self.enemigos[i].move(self.height)

        # Colisión entre disparos y enemigos (usamos un try - except para evitar error de índice).
        for d in range (len(self.plane.disparos)):
            for i in range (len(self.enemigos)):
                try:
                    if (int(self.plane.disparos[d].x) in range (self.enemigos[i].x - 5, self.enemigos[i].x + 16) and (int(self.plane.disparos[d].y) in range (self.enemigos[i].y, self.enemigos[i].y + 16))):
                        self.enemigos.remove(self.enemigos[i])
                except:
                    pass
        
        # Colisión entre disparos y jugador.
        for d in range (len(self.enemigos)):
            print(self.enemigos[d].disparos)
            for i in range (len(self.enemigos[d].disparos)):
                try:
                    if (self.enemigos[d].disparos[i].x in range (int(self.plane.x) - 5, int(self.plane.x + 16))) and (self.enemigos[d].disparos[i].y in range (int(self.plane.y), int(self.plane.y) + 16)):
                        pyxel.quit()
                except:
                    pass


    def draw(self):
        '''Método que permite dibujar cada elemento en la ventana.'''

        # Color de fondo.
        pyxel.cls(5)
        
        # Dibujamos las islas.
        x = pyxel.frame_count % pyxel.width
        x = x + 1
        pyxel.blt(0, x, 1, 208, 0, 22, 56, colkey = 8)

        f = pyxel.frame_count % pyxel.width
        f = f + 2
        pyxel.blt(100, f, 1, 204, 101, 52, 14, colkey = 8)
        
        '''
        for u in range (0, 5):
            lista = []
            lista.append(u)
            for c in range (len(lista)):
                u = pyxel.frame_count % pyxel.width  + 2
                pyxel.blt(c, random.randint(20, 265), 1, 247, 40, 7, 6, colkey = 8)
        '''

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
