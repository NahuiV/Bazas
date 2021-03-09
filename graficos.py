import gamelib

def dibujar_tablero():
    gamelib.draw_image('TABLERO.gif',0,0)

def dibujar_cartas(juego):
    for posicion,jugador in enumerate(juego.lista_jugadores):
        coordenadas=obtener_coordenadas(jugador.cartas,posicion)
        x,y,steps=coordenadas
        for carta in jugador.cartas:
            if posicion==0:
                gamelib.draw_image('cartas/'+carta+'.gif', x, y)
                x+=steps
            elif posicion==1 or posicion==3:
                gamelib.draw_image('cartas H\BACK H.gif', x, y)
                y+=steps
            elif posicion==2:
                gamelib.draw_image('cartas\BACK V.gif', x, y)
                x+=steps

def dibujar_carta_centro(juego):
    apuestas=juego.apuestas
    for n, jugador in enumerate(juego.lista_jugadores):
        if n == 0 :
            gamelib.draw_text(f'{jugador.nombre}', 400, 550)
            if apuestas!=None:
                gamelib.draw_text(f'{jugador.bazas}/{apuestas[jugador.nombre]}', 400, 570)
            if jugador.jugada != None:
                gamelib.draw_image('cartas/'+jugador.jugada+'.gif', 600, 360)
        elif n == 1:
            gamelib.draw_text(f'{jugador}', 245, 240)
            if apuestas!=None:
                gamelib.draw_text(f'{jugador.bazas}/{apuestas[jugador.nombre]}', 245, 260)
            if jugador.jugada != None:
                gamelib.draw_image('cartas H/'+jugador.jugada+'.gif', 500, 310)
        elif n == 2:
            gamelib.draw_text(f'{jugador}', 820, 170)
            if apuestas!=None:
                gamelib.draw_text(f'{jugador.bazas}/{apuestas[jugador.nombre]}', 820, 190) 
            if jugador.jugada != None:
                gamelib.draw_image('cartas/'+jugador.jugada+'.gif', 600, 260)
        elif n == 3 :
            gamelib.draw_text(f'{jugador}', 980, 500)
            if apuestas!=None:
                gamelib.draw_text(f'{jugador.bazas}/{apuestas[jugador.nombre]}', 980, 520)
            if jugador.jugada != None:
                gamelib.draw_image('cartas H/'+jugador.jugada+'.gif', 660, 320) 

def graficar_ganador(puntajes):
    for i,punto,nombre in enumerate(puntajes):
        if i==0:
            gamelib.draw_text(f'{nombre}-{punto}', 400, 550)
        elif i==1:
            gamelib.draw_text(f'{nombre}-{punto}', 400, 550)
        elif i==2:
            gamelib.draw_text(f'{nombre}-{punto}', 400, 550)
        elif i==3:
            gamelib.draw_text(f'{nombre}-{punto}', 400, 550)
    gamelib.wait()
        
def obtener_coordenadas(cartas,posicion):
    if posicion==0:
        return calcular_x_inicial(cartas),600,50
    elif posicion==1:
        return 30,calcular_y_inicial(cartas),20
    elif posicion==2:
        return calcular_x_inicial(cartas),30,30
    elif posicion==3:
        return 1100,calcular_y_inicial(cartas),20

def calcular_y_inicial(cartas):
    medio_Y=700/2
    py_y=30
    if not es_par(len(cartas)):
        medio_Y-=py_y/2
        y=medio_Y-((len(cartas)-1)*py_y)
    else:
        y=medio_Y-((len(cartas)/2)*py_y)
    return y

def calcular_x_inicial(cartas):
    medio_H=1230/2
    px_x=50
    if not es_par(len(cartas)):
        medio_H-=px_x/2
        x=medio_H-((len(cartas)-1)*px_x)
    else:
        x=medio_H-((len(cartas)/2)*px_x)
    return x
    
def es_par(numero):
    if numero % 2==0:
        return True
    return False
