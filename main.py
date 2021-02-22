from jugador import Jugador
import gamelib
import graficos
from juego import Juego
def verificar_opciones(opcion):
    if opcion<2 or opcion>4:
        return False
    return True
def mostrar_ganador(juego):
    return 0
def mostrar_estado_juego(juego):
    return 0
def main():
    bazas=Juego()
    gamelib.resize(1235, 720)
    graficos.dibujar_tablero()
    cantidad_jugadores=gamelib.input('Ingrese la cantidad de jugadores, puede ser entre 2 o 4: ')
    bazas.inicializar_juego(int(cantidad_jugadores))
    while not bazas.terminado():
        mostrar_estado_juego(bazas)
        bazas.mezclar_mazo()
        bazas.repartir_cartas()
        bazas.pedir_apuestas()
        while not bazas.ronda_terminada():
            mostrar_estado_juego(bazas)
            for jugador in bazas.lista_jugadores:
                jugador.pedir_jugada()
            bazas.determinar_ganador_ronda()
        bazas.contabilizar_puntos_ronda()
    mostrar_ganador(bazas)
gamelib.init(main)