import gamelib
import random
class Jugador:
    def __init__(self,nombre,cartas):
        self.nombre=nombre
        self.cartas=[]
        self.imagen=''
        self.puntos=0
        self.jugada=None
    def __str__(self):
        text=str(self.nombre)
        for a  in self.cartas:
            text=text+','+str(a)
        return text
    def agregar_cartas(self,carta):
        self.cartas.append(carta)
    def nueva_mano(self):
        return 0
    def pedir_jugada(self):
        self.jugada=self.cartas[random.shuffle(len(self.cartas))]