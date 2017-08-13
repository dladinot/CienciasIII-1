from cola import *
import random

cParqueaderos = Cola()

class Estudiantes:
     def __init__(self, nombre, codigo, placa):
         self.nombre = nombre
         self.codigo = codigo
         self.placa = placa
     def getNombre(self):    
         return self.nombre
     def getCodigo(self):
         return self.codigo
     def getPlaca(self):
         return self.placa

class AsignacionParqueaderos:
    global cParqueaderos
    
    def initEstudiantes(self):
        e0 = Estudiantes("Samuel Martinez", "20162025105", "CF790C")
        e1 = Estudiantes("Eduardo Romero", "20162020117", "AB123C")
        e2 = Estudiantes("Andres Diaz", "20112015089", "AS243D")
        e3 = Estudiantes("Bruno Lopez", "20122025114", "CB754B")
        e4 = Estudiantes("Felipe Rojas", "20141020007", "XC813D")
        e5 = Estudiantes("Camila Fernandez", "20132020117", "RT325A")
        e6 = Estudiantes("Diego Ramirez", "20171025113", "DS29A")
        e7 = Estudiantes("Orlando Duran", "20162007001", "HY765T")
        e8 = Estudiantes("Camilo Sanchez", "20112020056", "CB123F")
        e9 = Estudiantes("Angela Ortiz", "20151020067", "AF098A")

        allE = [e0,e1,e2,e3,e4,e5,e6,e7,e8,e9]
        for x in range(0, 10):
            cParqueaderos.encolar(allE[x]) 
           
    def getNumParqueaderos(self):
        return random.randint(1, 7)
    
    def asignacionParqueaderos(self):
        numParqueaderos = self.getNumParqueaderos()
        print("El numero de cupos de parqueaderos es: " + str(numParqueaderos))
        print("Los estudiantes beneficiados con parqueadero son:"+"\n")
        for x in range(0, numParqueaderos):
            aux = cParqueaderos.desencolar()
            print (str(x+1) +" =========================================")
            print ("Nombre: " + aux.getNombre() +"\n")
            print ("Codigo: " + aux.getCodigo() +"\n")
            print ("Placa: " + aux.getPlaca() +"\n")

        print("\n"+"Los estudiantes sin parqueadero son:"+"\n")
        while(cParqueaderos.es_vacia() == False):
            aux = cParqueaderos.desencolar()
            print ("||||||||||||||||||||||||||||||||||||||||||")
            print ("Nombre: " + aux.getNombre() +"\n")
            print ("Codigo: " + aux.getCodigo() +"\n")
            print ("Placa: " + aux.getPlaca() +"\n")
            
class Main:
    obj = AsignacionParqueaderos()
    obj.initEstudiantes()
    obj.asignacionParqueaderos()
        
        


        
    
    
