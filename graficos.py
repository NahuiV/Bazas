import gamelib
from jugador import Jugador
def dibujar_tablero():
    gamelib.draw_image('C:/Users/nahue/Desktop/Bazas/TABLERO.gif',0,0)

def dibujar_cartas(juego):
    jugadores=juego.lista_jugadores
    j1,j2=jugadores
    print(j1)
    for x in range(420, 813, 50):
        mano=j1.cartas
        for carta in mano:
            gamelib.draw_image('C:/Users/nahue/Desktop/Bazas/cartas/'+carta+'.gif', x, 600)
    
    for x2 in range(420, 813, 30):
        mano=j2.cartas
        for carta in mano:
            gamelib.draw_image('C:/Users/nahue/Desktop/Bazas/cartas/'+carta+'.gif', x2, 30)
def puntuaciones_partida():
    return 0
def ronda():
    return 0
