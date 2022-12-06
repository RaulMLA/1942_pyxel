import random
from enemigos import Enemigo
#from enemigocirc import EnemigoCircular
from plane import Plane
from disparo import Disparo
import pyxel


class Board:
    def __init__(self, w: int, h: int):
        '''Utilizamos esta clase para poner las medidas principales del tablero y a su vez
        importar nuestro banco de imagenes '''
        self.width = w
        self.height = h
        pyxel.init(self.width, self.height, title="1942")
        pyxel.load("assets/my_resource.pyxres")

        '''También ponemos la posicion inicial de nuestro jugador e introducimos la actualización del 
        programa ante el paso del tiempo y las posibles interacciones. Aparte de llamar a la función 
        dibujar para poder crear los gráficos'''
        self.plane = Plane(self.width / 2, 200)
        self.enemigo=Enemigo(self.width / 2, 0)
        '''self.enemigo = []
        for i in range (0,random.randint(3,7)):
            self.enemigo.append=Enemigo(self.width / 2, 0)'''
        #self.enemigocirc = EnemigoCircular(self.width / 2, 30)
###############################################################
        '''Valeee yo aquí para hacer una actualizacion y reiniciar haría un boolean, de tal manera que metemos una 
        variable inicializada anteriormente al run con un true y cuando nos den a nosotros se convierta en false 
        de este modo tiene que meterse en el bucle que hace run cada vez que nos dan '''
##################################################################
        pyxel.run(self.update, self.draw)

    def update(self):
        """ Para poder salir del programar y acabar el juego cuando el usuario quiera,
        utilizamos la tecla F1, de esta manera el jugador puede salir cuando quiera del programa"""
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()


        '''Movimiento de nuestro jugador principal y disparo'''

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.plane.move('right', self.width)
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.plane.move('left', self.width)
        if pyxel.btn(pyxel.KEY_UP):
            self.plane.move('up', self.width)
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.plane.move('down', self.width)
            '''Disparo del jugador controlado, creación del propio disparo y movimimiento del mismo'''
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.plane.disparo.append(Disparo(self.plane.x,self.plane.y))
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
        """ This is executed also each frame, here you should just draw
        things """
        pyxel.cls(12)
        x = pyxel.frame_count % pyxel.width
        x = x + 1
        pyxel.blt(0, x, 1, 208, 0, 22, 56, colkey=8)
        f = pyxel.frame_count % pyxel.width
        f = f + 2
        pyxel.blt(100, f, 1, 204, 101, 52, 14, colkey=8)
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
        pyxel.blt(self.plane.x, self.plane.y, *self.plane.sprite, colkey=8)

        pyxel.blt(self.enemigo.x, self.enemigo.y, *self.enemigo.sprite, colkey=8)


        #pyxel.blt(self.enemigocirc.x, self.enemigocirc.y, *self.enemigocirc.sprite, colkey=8)
        for i in range(len(self.enemigo.disparo)):
            pyxel.blt(self.enemigo.disparo[i].x, self.enemigo.disparo[i].y, *self.enemigo.disparo[i].sprite, colkey=8)


        for i in range(len(self.plane.disparo)):
            pyxel.blt(self.plane.disparo[i].x, self.plane.disparo[i].y, *self.plane.disparo[i].sprite, colkey=8)