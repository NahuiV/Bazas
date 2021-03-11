import jugador
import gamelib
import graficos
from juego import Juego

def pedir_opcion():
    while True:
        opcion=gamelib.input('Ingrese la cantidad de jugadores, puede ser entre 2 o 4: ')
        if ((opcion==None) or (opcion.isdigit()==False) or (int(opcion)<2 or int(opcion)>4)):
            gamelib.say('Opcion invalida, vuelva a ingresar')
        else:
            break
    return int(opcion)

def mostrar_ganador(juego):
    jugadores=juego.lista_jugadores
    puntajes=[]
    for jugador in jugadores:
        puntajes.append((jugador.puntos,jugador.nombre))
    puntajes.sort(key=lambda x: x[0])
    graficos.graficar_ganador(puntajes)

def mostrar_estado_juego(juego):
    graficos.dibujar_tablero()
    graficos.dibujar_cartas(juego)
    graficos.dibujar_carta_centro(juego)
    
def main():
    bazas=Juego()
    gamelib.resize(1230, 700)
    graficos.dibujar_tablero()
    bazas.inicializar_juego(pedir_opcion())
    while not bazas.terminado():
        bazas.mezclar_mazo()
        bazas.repartir_cartas()
        mostrar_estado_juego(bazas)
        bazas.suma_apuestas=0
        for indice,jugador in enumerate(bazas.lista_jugadores):
            jugador.pedir_apuesta(indice,bazas.suma_apuestas,bazas)
            bazas.rotar_jugadores()
            mostrar_estado_juego(bazas)
        #bazas.pedir_apuestas()
        while not bazas.ronda_terminada():
            mostrar_estado_juego(bazas)
            for jugador in bazas.lista_jugadores:
                jugador.pedir_jugada()
                bazas.rotar_jugadores()
                mostrar_estado_juego(bazas)
            bazas.determinar_ganador_ronda()
        bazas.contabilizar_puntos_ronda()
    mostrar_ganador(bazas)
gamelib.init(main)