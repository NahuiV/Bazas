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

    def agregar_cartas(self,carta):
        self.cartas.append(carta)
    
    def __str__(self):
        t=self.nombre
        return t
    
    def buscar_carta(self, ev_x, x1, x2):
        contador_i = 0
        while not x1 < ev_x < x1+PIXELES_CARTA and ev_x < x2:
            x1 += PIXELES_CARTA
            contador_i += 1
        return contador_i
    
    def pedir_jugada(self):
        if (len(self.cartas) % 2) == 0:
            coord_x1 = LARGO/2 - (len(self.cartas)/ 2) * PIXELES_CARTA
            coord_x2 = LARGO/2 + (len(self.cartas)/ 2) * PIXELES_CARTA
        else:
            coord_x1 = LARGO/2 - (PIXELES_CARTA/ 2) - (((len(self.cartas)-1) / 2)*PIXELES_CARTA)
            coord_x2 = LARGO/2 + (PIXELES_CARTA/ 2) + (((len(self.cartas)-1) / 2)*PIXELES_CARTA)
            
        while gamelib.is_alive():
            ev = gamelib.wait()
            if ev.type == gamelib.EventType.ButtonPress:
                x, y = ev.x, ev.y
                if  y >600  and coord_x1 < x < coord_x2:
                    break
        
        carta = self.buscar_carta(x, coord_x1, coord_x2)
        self.jugada = self.cartas.pop(carta)
        self.cartas_usadas.append(self.jugada)
        