# Objetivo
El objetivo del proyecto es implementar el videojuego 1942. El videojuego es un juego de disparos en el que el jugador controla un avión que debe destruir a los aviones enemigos y evitar que los misiles enemigos lo destruyan. El juego se desarrolla en un escenario de 2D, en el que el jugador se mueve en el eje horizontal y dispara en el eje vertical. El juego finaliza cuando el jugador es derrotado por los enemigos o cuando el jugador derrota a todos los enemigos.
<br><br>
El proyecto ha sido desarrollado mediante la librería Pyxel de Python, un motor de videojuegos retro creado por Takashi Kitao en 2018.
<br><br>
El videojuego mediante el desarrollo de clases que funcionan de manera cooperada mediante sus respectivos atributos y métodos.

# Contenidos
- [Descripción de clases, atributos y métodos](#descripción-de-clases-atributos-y-métodos)
  - [Board](#board)
  - [Enemigo](#enemigo)
  - [Plane](#plane)
  - [Disparo](#disparo)
  - [Fondo](#fondo)
  - [Isla](#isla)
  - [Explosión](#explosión)
- [Descripción de algoritmos utilizados](#descripción-de-algoritmos-utilizados)
    - [generar_enemigos](#generar_enemigos)
    - [stop_game](#stop_game)
    - [reset](#reset)
    - [comprobar_colision](#comprobar_colision)
- [Trabajo desarrollado](#trabajo-desarrollado)
    - [Funcionalidades incluidas](#funcionalidades-incluidas)
    - [Partes no implementadas](#partes-no-implementadas)
    - [Funcionalidades extra](#funcionalidades-extra)
- [Conclusiones](#conclusiones)

# Descripción de clases, atributos y métodos
Para el desarrollo del proyecto, se han utilizado clases para representar los diferentes objetos del juego. Algunos de ellos como podría ser el caso de los enemigos, cuentan con diferentes tipos que han sido derivados mediante herencia de clases, de modo que las clases hijas heredan toda la información de la clase padre y modifican las funcionalidades que difieren del mismo. En esta sección, se detallarán los puntos más importantes de cada una de las clases implementadas.
<br><br>
Destacar que, de manera general, los principales atributos de cada clase son las coordenadas (x, y) y el banco de sprites para los aspectos así como su aspecto en uso, sprite.

## Board
La clase Board es el núcleo principal del proyecto. Es la encargada de inicializar todo el contenido que va a ser observado por el usuario así como de actualizar las distintas funcionalidades y de dibujar en pantalla el contenido en cada actualización de frame. Respecto a los atributos, contamos con un avión (jugador), una lista de enemigos y otros como las dimensiones de la ventana (tablero) o las condiciones de inicio. Cuenta con los métodos update y draw, las cuales se encargan de actualizar y dibujar en cada frame. Además, cuenta con los métodos stop_game y generar_enemigos, los cuales serán explicados posteriormente. El método update cuenta con varios bucles que recorren las listas de enemigos y disparos y actualizan el estado del juego atendiendo a los principales requisitos. Recalcar aquí que hay bucles de enemigos que se podrían optimizar fusionándose en uno solo, pero se han considerado separados para facilitar la lectura y comprensión del código.

## Enemigo
La clase Enemigo representa cada enemigo generado durante el transcurso del juego. En nuestro caso, pueden ser de cuatro tipos: regular, rojo, bombardero y superbombardero, los cuales se representan con cuatro clases hijas que heredan los atributos y métodos de la clase padre. Dentro de la clase Enemigo contamos con el método move, el cuál permite al enemigo moverse dependiendo de su dirección. Además, contamos con los métodos animation y reset. El método animation se encarga de seleccionar el aspecto del enemigo dependiendo del tipo y dirección del mismo. Por otra parte, el método reset se encarga de devolver al enemigo a su estado inicial como se explicará posteriormente. Por último, hemos utilizado el ‘magic method’ de Python __repr__ para representar al enemigo con fines de depuración durante el desarrollo. Dentro de las clases hijas, además de modificaciones en la clase move del padre, contamos con un método llamado comprobar_colision el cuál será detallado en la sección de algoritmos implementados posteriormente. Los enemigos cuentan con atributos para controlar datos como su lista de disparos, vida, velocidad o puntuación que proporcionan.

## Plane
La clase Plane representa al jugador (avión) del juego. Es el encargado de disparar a los enemigos y puede moverse libremente usando las flechas del teclado además de hacer loops para evitar ser abatido. El método move permite al jugador moverse dependiendo de la dirección. El método make_loop permite al usuario hacer un loop para evitar ser abatido. El método animation permite realizar la animación de las hélices así como de los loops. Por último, el método comprobar_colision detecta colisiones con otros enemigos o disparos enemigos, pero será explicado con detalle posteriormente en la sección de algoritmos utilizados. El avión cuenta con atributos como su vida, velocidad, lista de disparos o loops restantes.

## Disparo
La clase Disparo representa un disparo por parte del jugador o del enemigo. Dependiendo del tipo, se utiliza un aspecto u otro y una dirección u otra atendiendo a las constantes del proyecto. Cuenta con el método move, el cuál mueve la bala por la pantalla dependiendo de su dirección y velocidad.

## Fondo
La clase Fondo representa el fondo del juego. Cuenta con el método move para mover el contenido (únicamente islas en nuestro caso) en cada frame del juego. Además, podemos observar el atributo islas, el cual es una lista que contiene todos los objetos de tipo Isla que veremos a continuación.

## Isla
La clase Isla representa una isla del fondo en el juego. Cuenta con el método move que permite a la isla desplazarse a una velocidad determinada. Además, el aspecto es distinto dependiendo del tipo de isla, por lo que se usa un atributo para determinar el mismo.

## Explosión
La clase Explosión es simple, simplemente se inicializa con sus coordenadas y un aspecto diferente dependiendo del tipo de explosión que se desee. Por ejemplo, la explosión de un bombardero será ampliamente mayor que la de un avión regular o rojo.

# Descripción de algoritmos utilizados
En el desarrollo del juego, se han implementado varios algoritmos en métodos como explicaremos a continuación. Se muestran los más relevantes, pero se han implementado más para satisfacer las necesidades de cada funcionalidad. Además de esto, el método update de la clase Board cuenta con los algoritmos necesarios para generar y eliminar enemigos, disparos y otros objetos como explosiones o islas que se generan durante el transcurso del mismo.

## generar_enemigos
Este método se encuentra en la clase Board y se encarga de generar los enemigos de manera automática y aleatoria siguiendo los patrones de formaciones y número mínimo de cada tipo de enemigos indicados en el enunciado. Esto es, se generan como mínimo 20 aviones regulares, 5 aviones rojos, 2 bombarderos y 1 superbombardero, aunque pueden generarse más.
Todos los enemigos se incluyen en una lista de enemigos inactivos (que posteriormente serán activados en intervalos de tiempo aleatorios). La generación de enemigos regulares se realiza en formaciones de 10 o 20, los enemigos rojos se generan en formaciones de 5 aviones y los bombarderos y superbombarderos se generan de manera individual.

## stop_game
Este método se encuentra en la clase Board y se encarga de parar el juego en caso de que un usuario pierda una vida. El método cambia las variables de control requeridas para mostrar la pantalla correspondiente y acto seguido elimina todo el contenido de la pantalla y lo guarda en listas para que al volver al juego se puedan volver a mostrar. Para ello, se ha utilizado el método reset que se explicará a continuación.

## reset
El método reset pertenece a la clase Enemigo y, por tanto, es común a todos los enemigos del juego. Se encarga de establecer las coordenadas que se establecieron por primera vez en la generación del mismo al inicio del juego, de forma que este enemigo pueda volver a aparecer. Además, se establece la dirección que seguirán, la cuál coincide con la que usaron en un primer instante.

## comprobar_colision
Este método se encuentra tanto en la clase Plane como en cada clase hija de Enemigo. Se encarga de comparar las coordenadas de un objeto para determinar si existe una colisión y si se tiene que realizar una acción u otra.
