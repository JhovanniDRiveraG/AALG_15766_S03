#semana 4 Poo
#ejemplo class perro

import random #para saludo

class Perro:
    def __init__(self, nombre="",color="",edad=0): #self es para atributos
        self._nombre = nombre
        self._color = color
        self._edad = edad
        
        """ no funciona tener dos constructores
        def __init__(self):
        self.nombre = ""
        self.color = ""
        self.edad = ""
        
        def __init__(self, nombre, color, edad):
        self.nombre = nombre
        self.color = color
        self.edad = edad
        """
    
    def ladrar(self):
        print("guau")
    def saludo(self):
        return "pata" if random.randint(0,1) == 0 else "Cola"
    def __str__(self):
        return f"Perro: {self._nombre}, de color {self._color} y {self._edad} años"
    
p = Perro("Fido","Marron",5)
p.ladrar()
print(f"Me saludo con la {p.saludo()}")
print(p)

print()
q = Perro("Rambo")
print(q._nombre)