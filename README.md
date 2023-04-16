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



