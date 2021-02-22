import gamelib
from jugador import Jugador
def dibujar_tablero():
    gamelib.draw_image('C:/Users/nahue/Desktop/Bazas/TABLERO.gif',0,0)
def dibujar_cartas(juego):
    x=0
    for jugador in juego[0]:
        mano=jugador.cartas
        for carta in mano:
            gamelib.draw_image('C:/Users/nahue/Desktop/Bazas/cartas/'+carta+'.gif',x,0)
            x=x+40
        break
def puntuaciones_partida():
    return 0
def ronda():
    return 0
    