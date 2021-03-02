import gamelib
from jugador import Jugador
def dibujar_tablero():
    gamelib.draw_image('C:/Users/nahue/Desktop/Bazas/TABLERO.gif',0,0)

def dibujar_cartas(juego):
    posiciones=((420,50,600),(30,20,200),(420, 30, 30),(1100,20,200))
    for num,jugador in enumerate(juego.lista_jugadores):
        coordenadas=posiciones[num]
        x,steps,y=coordenadas
        for carta in jugador.cartas:
            if num==0:
                gamelib.draw_image('C:/Users/nahue/Desktop/Bazas/cartas/'+carta+'.gif', x, y)
                x+=steps
            elif num==1 or num==3:
                gamelib.draw_image('C:/Users/nahue/Desktop/Bazas/cartas H/BACK H.gif', x, y)
                y+=steps
            elif num==2:
                gamelib.draw_image('C:/Users/nahue/Desktop/Bazas/cartas/BACK V.gif', x, y)
                x+=steps
            
def puntuaciones_partida():
    return 0
def ronda():
    return 0
