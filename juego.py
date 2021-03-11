import random
from tda import *
from jugador import Jugador
import gamelib
LARGO,ANCHO=1230,700
PIXELES_CARTA=50

class Juego:
    def __init__(self):
        self.lista_jugadores=[]
        self.mazo=Pila()
        self.cantidad_jugadores=0
        self.rondas=13
        self.ronda_actual=1
        self.manos_jugada=0
        self.suma_apuestas=0
        self.apuestas=None
        self.triunfo=None

    def mezclar_mazo(self):
        mazo_aux = []

        for _ in range(0,self.mazo.cantidad_elementos()):
            mazo_aux.append(self.mazo.desapilar())

        random.shuffle(mazo_aux) 
        
        for carta in mazo_aux:
            self.mazo.apilar(carta)

       

        self.manos_jugada=0
        self.apuestas=None
        self.triunfo=None
        for jugador in self.lista_jugadores:
            jugador.jugada=None

    def rotar_jugadores(self, n=-1):
        if len(self.lista_jugadores) == 0:
            self.lista_jugadores = self.lista_jugadores
        n = -n % len(self.lista_jugadores)
        self.lista_jugadores = self.lista_jugadores[n:] + self.lista_jugadores[:n]
    
    def inicializar_juego(self,cantidad_jugadores):
        palos = ('D', 'H', 'S', 'C')
        valores = ('2','3','4','5','6','7','8','9', 'J', 'Q', 'K', 'A')
        for palo in palos:
            for valor in valores:
                self.mazo.apilar((str(valor) + str(palo)))

        self.cantidad_jugadores=cantidad_jugadores
        for numero_jugador in range(1,cantidad_jugadores+1):
            while True:
                nombre_jugador=gamelib.input("Ingrese nombre del jugador numero "+str(numero_jugador))
                if ((nombre_jugador==None )or (len(nombre_jugador)==0)):
                    gamelib.say('Se necesita un nombre para poder continuar,porfavor vuelva a ingresar')
                else:
                    jugador=Jugador(nombre_jugador,0)
                    self.lista_jugadores.append(jugador)
                    break

    def repartir_cartas(self):
        for _ in range(0,self.ronda_actual):
            for jugador in self.lista_jugadores:
                jugador.agregar_cartas(self.mazo.desapilar())
        
        if self.ronda_actual==self.rondas-1:
            self.triunfo='AH'
        else:
            self.triunfo=self.mazo.desapilar()
        gamelib.say("Ronda "+ str(self.ronda_actual))

    def pedir_apuestas(self):
        apuestas={}
        suma_apuesta=0
        for contador,jugador in enumerate(self.lista_jugadores):
            while True:
                a=jugador.pedir_apuesta()
                a=self.validar_apuesta(jugador.nombre,a)
                #apuesta=gamelib.input('Cuantas bazas vas a obtener '+jugador.nombre)
                #apuesta=self.validar_apuesta(jugador.nombre,apuesta)
                if contador==self.cantidad_jugadores-1:
                    if suma_apuesta+int(a)==self.ronda_actual:
                        gamelib.say('La apuesta ingresada iguala el numero de ronda actual,ingrese un valor entre 0 y '+ str(self.ronda_actual)+'')
                    else:
                        apuestas[jugador.nombre]=int(a)
                        break
                else:
                    apuestas[jugador.nombre]=int(a)
                    suma_apuesta+=int(a)
                    break
            self.rotar_jugadores()
        self.apuestas=apuestas

    def contabilizar_puntos_ronda(self):
        for jugador in self.lista_jugadores:
            if jugador.apuesta==jugador.bazas:
                jugador.puntos+=10+(5*self.ronda_actual)
            jugador.bazas=0
        self.lista_jugadores=self.lista_jugadores[1:] + self.lista_jugadores[:1]
        for jugador in self.lista_jugadores:
            print(jugador.puntos)   
        self.ronda_actual+=1

    def determinar_ganador_ronda(self):
        valores = ('2','3','4','5','6','7','8','9', 'J', 'Q', 'K', 'A')
        indices_para_ordenar=[]
        cartas_palo_principal=[]
        cartas_palo_triunfo=[]
        cartas_distintas=[]
        cartas_ronda={}
        carta_principal_obtenida=False

        for jugador in self.lista_jugadores:
            cartas_ronda[jugador]=jugador.jugada
            if carta_principal_obtenida==False:
                carta_principal=cartas_ronda[jugador]
                cartas_palo_principal.append(carta_principal)
                carta_principal_obtenida=True
            
        for carta in cartas_ronda.values():
            if not carta==carta_principal:
                if carta[1]==carta_principal[1]:
                    cartas_palo_principal.append(carta)
                elif carta[1]==self.triunfo[1]:
                    cartas_palo_triunfo.append(carta)
                else:
                    cartas_distintas.append(carta)

        if len(cartas_palo_principal)==1 and len(cartas_palo_triunfo)==0:
            self.asignar_baza(cartas_ronda,carta_principal)
            
        elif len(cartas_palo_triunfo)>0:
            for carta in cartas_palo_triunfo:
                indices_para_ordenar.append(valores.index(carta[0]))
            indice=sorted(indices_para_ordenar)
            for carta in cartas_palo_triunfo:
                if carta[0]==valores[indice[0]]:
                    self.asignar_baza(cartas_ronda,carta)
                   
                    break
        else:
            for carta in cartas_palo_principal:
                indices_para_ordenar.append(valores.index(carta[0]))
            indice=sorted(indices_para_ordenar)
            for carta in cartas_palo_principal:
                if carta[0]==valores[indice[0]]:
                    self.asignar_baza(cartas_ronda,carta)
                    
                    break
        self.manos_jugada+=1

    def terminado(self):
        if self.ronda_actual==self.rondas:
            return True
        return False

    def asignar_baza(self,ronda,carta):
        for jugador in ronda:
            if ronda[jugador]==carta:
                jugador.bazas+=1
                break

    def ronda_terminada(self):
        if self.ronda_actual==self.manos_jugada:
            for jugador in self.lista_jugadores:
                for carta in jugador.cartas_usadas:
                    self.mazo.apilar(carta)
                jugador.cartas_usadas=[]
            self.mazo.apilar(self.triunfo)
            self.triunfo=None
            return True
        return False

    def validar_apuesta(self,jugador,apuesta):  
        while True:
            if apuesta==None or apuesta.isdigit()==False or (int(apuesta) > self.ronda_actual) or (0>int(apuesta)):
                gamelib.say('Opcion incorrecta, vuelva a ingresar ')
                apuesta=gamelib.input('Cuantas bazas vas a obtener '+jugador)
            else:
                break
        return int(apuesta)

