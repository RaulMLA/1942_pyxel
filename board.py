import random
from enemigos import Enemigo
from enemigocirc import EnemigoCircular
from plane import Plane
from disparo import Disparo
import pyxel


class Board:
    '''Clase que representa el tablero.'''

    def __init__(self, w: int, h: int):
        '''Método que inicializa el tablero con sus medidas y carga el banco de
        imágenes.'''

        self.width = w
        self.height = h
        pyxel.init(self.width, self.height, title = "1942")
        pyxel.load("assets/my_resource.pyxres")

        # Posición inicial de nuestro jugador.
        self.plane = Plane(self.width / 2, 200)

        # Posición inicial del enemigo.
        self.enemigo = Enemigo(self.width / 2, 0)

        '''self.enemigo = []
        for i in range (0, random.randint(3, 7)):
            self.enemigo.append = Enemigo(self.width / 2, 0)
            #self.enemigocirc = EnemigoCircular(self.width / 2, 30)'''

        pyxel.run(self.update, self.draw)


    def update(self):

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
            self.plane.disparo.append(Disparo(self.plane.x, self.plane.y))
        
        for i in range(len(self.plane.disparo)):
            self.plane.disparo[i].move('up')


        '''Disparo del enemigo random, al disparar en un intervalo no controlado'''
##########################
        '''Podriamos hacer distintos porcentajes de disparo según el tipo de enemigo pero esto 
        lo tenemos que mirar con más tiempo'''
##########################
        if random.randint(1,1000)<40:
            self.enemigo.disparo.append(Disparo(self.enemigo.x,self.enemigo.y))
        for i in range(len(self.enemigo.disparo)):
            self.enemigo.disparo[i].move("down")

##########################################################
            '''if self.plane.disparo[i].y<-8:
                del.self.plane.disparo[i]'''
#############################################################

        self.enemigo.move( "down",self.width)
        #self.enemigocirc.move()


    def draw(self):
        '''Método que permite dibujar cada elemento en la ventana.'''

        # Color de fondo.
        pyxel.cls(12)
        x = pyxel.frame_count % pyxel.width
        x = x + 1
        pyxel.blt(0, x, 1, 208, 0, 22, 56, colkey = 8)
        f = pyxel.frame_count % pyxel.width
        f = f + 2
        pyxel.blt(100, f, 1, 204, 101, 52, 14, colkey = 8)
        
        '''for u in range (0,5):
            lista=[]
            lista.append[u]
            for c in len(lista):
                u= pyxel.frame_count % pyxel.width  + 2
                pyxel.blt(a,random.randint(20,265),1,247,40,7,6,colkey=8)'''

        pyxel.text(90, 5, "H I G H   S C O R E", 7)
        pyxel.text(10, 5, "U P 1", 7)

        # We draw the plane taking the values from the plane object
        # Parameters are x, y, and a tuple containing the image bank,
        # the starting x and y and the size


        pyxel.blt(self.plane.x, self.plane.y, *self.plane.sprite, colkey = 8)

        pyxel.blt(self.enemigo.x, self.enemigo.y, *self.enemigo.sprite, colkey = 8)


        #pyxel.blt(self.enemigocirc.x, self.enemigocirc.y, *self.enemigocirc.sprite, colkey=8)
        for i in range(len(self.enemigo.disparo)):
            pyxel.blt(self.enemigo.disparo[i].x, self.enemigo.disparo[i].y, *self.enemigo.disparo[i].sprite, colkey = 8)


        for i in range(len(self.plane.disparo)):
            pyxel.blt(self.plane.disparo[i].x, self.plane.disparo[i].y, *self.plane.disparo[i].sprite, colkey = 8)
