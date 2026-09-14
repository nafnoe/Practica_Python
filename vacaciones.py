import os
import os.path
import pickle
import io

#Declaramos la estructura de datos
class Propiedad:
    def __init__(self):
        self.cod = 0
        self.tipo = " "
        self.zona =0
        self.dir= " "
        self.cantAmb = 0
        self.precio = 0.00 
        self.alquilado = [['D', 'D'] for i in range (3) ]

class Zona:
    def __init__(self):
        self.nro = 0
        self.nombre = " " 

def abrirArchivo():
    print()


def menu():
    print()

def cerrarArchivo():
    print()



#Inicio del programa principal
def programaPrincipal():
    abrirArchivo()
    menu()
    cerrarArchivo()








programaPrincipal()