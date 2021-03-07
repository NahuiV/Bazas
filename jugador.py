import gamelib
import random
import graficos
class Jugador:
    def __init__(self,nombre,cartas):
        self.nombre=nombre
        self.cartas=[]
        self.imagen=''
        self.bazas=0
        self.puntos=0
        self.jugada=None
    def __str__(self):
        text=str(self.nombre)
        for a in self.cartas:
            text=text+','+str(a)
        return text
    def agregar_cartas(self,carta):
        self.cartas.append(carta)
    def nueva_mano(self):
        return 0
    def pedir_jugada(self):
        print(self.cartas)
        apuesta=gamelib.input("Elija la carta: ")
        self.cartas.pop(self.cartas.index(apuesta))
        self.jugada=apuesta