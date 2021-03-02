import gamelib
from jugador import Jugador
def dibujar_tablero():
    gamelib.draw_image('C:/Users/nahue/Desktop/Bazas/TABLERO.gif',0,0)

def dibujar_cartas(juego):
    posiciones=((420,50,600),(420, 813, 30))
    for num,jugador in enumerate(juego.lista_jugadores):
        coordenadas=posiciones[num]
        x,steps,y=coordenadas
        for carta in jugador.cartas:
            gamelib.draw_image('C:/Users/nahue/Desktop/Bazas/cartas/'+carta+'.gif', x, y)
            x+=steps

def puntuaciones_partida():
    return 0
def ronda():
    return 0
