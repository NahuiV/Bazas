import random
from tda import *
from jugador import *
import gamelib
class Juego:
    def __init__(self):
        self.lista_jugadores=[]
        self.mazo=[]
        self.cantidad_jugadores=0
        self.rondas=12
        self.ronda_actual=0
        self.apuestas=None
        self.triunfo=''
    def mezclar_mazo(self):
        for _ in range(0,4):
            random.shuffle(self.mazo)
        mazo_nuevo=Pila()
        for carta in self.mazo:
            mazo_nuevo.apilar(carta)
        self.mazo=mazo_nuevo
    def crear_mazo(self):
        palos=('D','H','S','C')
        valor=(2,3,4,5,6,7,8,9,'J','Q','K','A')
        for palo in palos:
            for numero in valor:
                self.mazo.append(str(numero)+str(palo))
    def inicializar_juego(self,cantidad_jugadores):
        self.cantidad_jugadores=cantidad_jugadores
        for numero_jugador in range(1,cantidad_jugadores+1):
            nombre_jugador=gamelib.input("Ingrese nombre del jugador numero "+str(numero_jugador))
            jugador=Jugador(nombre_jugador,0)
            self.lista_jugadores.append(jugador)
    def repartir_cartas(self):
        for _ in range(0,self.ronda_actual):
            for jugador in self.lista_jugadores:
                jugador.agregar_cartas(self.mazo.desapilar())
    def pedir_apuestas(self):
        apuestas={}
        suma_bazas=0    
        for jugador in self.lista_jugadores:
            apuesta=gamelib.input('Cuantas bazas vas a obtener '+jugador.nombre)
            if jugador==self.lista_jugadores[-1]:
                while True:
                    if(suma_bazas+int(apuesta))!=self.ronda_actual:
                        break
                    print('Ingrese un numero entre 0 y'+str(self.ronda_actual))
                    apuesta=gamelib.input('Cuantas bazas vas a obtener '+jugador.nombre)
            apuestas[jugador.nombre]=apuesta
            suma_bazas=+int(apuesta)
            self.apuestas=apuestas
    def contabilizar_puntos_ronda(self):
        return 0
    def devolver_cartas(self):
        return 0
    def determinar_ganador_ronda(self):
        valor=(2,3,4,5,6,7,8,9,'J','Q','K','A')
        indice=[]
        cartas_que_si=[]
        ronda=[]
        for jugador in self.lista_jugadores:
            ronda.append(jugador.jugada)
        carta_principal=ronda[0]
        for carta in ronda:
            if not carta==carta_principal:
                if carta[1]==carta_principal[1] or carta[1]==self.triunfo[1]:
                    cartas_que_si.append(carta)
        for carta in cartas_que_si:
            
                

        
    def terminado(self):
        if self.ronda_actual==self.rondas:
            return True
        return False
    def ronda_terminada(self):
        return 0
    def pedir_jugada(self):
        return 0
    