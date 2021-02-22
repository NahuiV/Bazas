class Pila:
    def __init__(self):
        self.mazo=[]
    def apilar(self,carta):
        self.mazo.append(carta)
    def desapilar(self):
        try:
            return self.mazo.pop()
        except IndexError:
            raise ValueError("La pila está vacía")
    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.mazo == []
    def cantidad_elementos(self):
        return len(self.mazo)