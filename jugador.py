import gamelib
import random
import graficos
LARGO,ANCHO=1230,700
PIXELES_CARTA=50
class Jugador:
    def __init__(self,nombre,cartas):
        self.nombre=nombre
        self.cartas=[]
        self.cartas_usadas=[]
        self.imagen=''
        self.bazas=0
        self.puntos=0
        self.jugada=None
        self.apuesta=0

    def agregar_cartas(self,carta):
        self.cartas.append(carta)
    
    def validar_apuesta(self,apuesta,ronda_actual):  
        while True:
            if apuesta==None or apuesta.isdigit()==False or (int(apuesta) > ronda_actual) or (0>int(apuesta)):
                gamelib.say('Opcion incorrecta, vuelva a ingresar ')
                apuesta=gamelib.input('Cuantas bazas vas a obtener '+self.nombre)
            else:
                break
        return int(apuesta)
    
    def pedir_apuesta(self,indice,suma_apuesta,bazas):
        apuesta=gamelib.input('Cuantas bazas vas a obtener '+self.nombre)
        apuesta=self.validar_apuesta(apuesta,bazas.ronda_actual)
        if indice==bazas.cantidad_jugadores-1:
            if bazas.suma_apuestas+int(apuesta)==bazas.ronda_actual:
                gamelib.say('La apuesta ingresada iguala el numero de ronda actual,ingrese un valor entre 0 y '+ str(self.ronda_actual)+'')
            else:
                self.apuesta=apuesta
        else:
            self.apuesta=apuesta
            bazas.suma_apuestas+=int(apuesta)
               
    def buscar_carta(self, ev_x, x1, x2):
        contador=0
        while not x1==x2:
            if ev_x >= x1 and ev_x<x1+PIXELES_CARTA:
                return contador
            x1+=PIXELES_CARTA
            contador+=1
            
    def pedir_jugada(self):
        if (len(self.cartas) % 2) == 0:
            coord_x1 = (LARGO/2 - (len(self.cartas)/ 2) * PIXELES_CARTA)
            coord_x2 = (LARGO/2 + (len(self.cartas)/ 2) * PIXELES_CARTA)
        else:
            coord_x1 = LARGO/2 - (PIXELES_CARTA/ 2) - (((len(self.cartas)-1) / 2)*PIXELES_CARTA)
            coord_x2 = LARGO/2 + (PIXELES_CARTA/ 2) + (((len(self.cartas)-1) / 2)*PIXELES_CARTA)
            
        while gamelib.is_alive():
            ev = gamelib.wait()
            if ev.type == gamelib.EventType.ButtonPress:
                x, y = ev.x, ev.y
                if  y >600  and ( x < coord_x2 and x > coord_x1):
                    break
        
        carta = self.buscar_carta(x, coord_x1, coord_x2)
        self.jugada = self.cartas.pop(carta)
        self.cartas_usadas.append(self.jugada)
        