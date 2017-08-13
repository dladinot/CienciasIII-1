from pila import*

pPeliculas = Pila()
pBusquedas = Pila()

class Peliculas:

    def __init__(self, nombre, ano, actor, genero):
        self.nombre = nombre
        self.ano = ano
        self.actor = actor
        self.genero = genero
    def getGenero(self):
        return self.genero
    def getNombre(self):
        return self.nombre
    def getAno(self):
        return self.ano
    def getActor(self):
        return self.actor    
    
class BusquedaPeliculas:   

    def initPeliculas(self):
        global pPeliculas        
        p0 = Peliculas("Love exposure", "2008", "Takahiro Nishijima", "Comedia")
        p1 = Peliculas("Spiderman HomeComing", "2017", "Tom Holland", "Accion")
        p2 = Peliculas("WonderWoman", "2017", "Gal Gadot", "Accion")
        p3 = Peliculas("Gifted", "2017", "Chris Evans", "Drama")
        p4 = Peliculas("El Conjuro", "2013", "Vera Farmiga", "Terror")
        p5 = Peliculas("Ghost In The Shell", "2017", "Scarlett Johansson", "Accion")
        p6 = Peliculas("Doctor Strange", "2016", "Benedict Cumberbath", "Accion")
        p7 = Peliculas("Die Hard", "1989", "Bruce Willis", "Accion")
        p8 = Peliculas("La Pelota de Letras", "2004", "Andres Lopez", "Comedia")
        p9 = Peliculas("Ring", "1998", "Nanako Matsushima", "Terror")
        allP = [p0,p1,p2,p3,p4,p5,p6,p7,p8,p9]
        for x in range(0, 10):
            pPeliculas.apilar(allP[x])            
        
    def busquedas(self):
        global pBusquedas
        pEncontradas = 0
        print("Buscador de Peliculas con Pilas."+"\n")
        print("Ingrese el Genero:")
        genero = input() #Python 2.x raw_input(), 3.x input()        
        while (pPeliculas.es_vacia() == False):            
            aux = pPeliculas.desapilar()
            if aux.getGenero() == genero:
                pBusquedas.apilar(aux)
                pEncontradas+=1         

        while (pBusquedas.es_vacia() == False):
            pelicula = pBusquedas.desapilar()
            print ("=========================================")
            print ("Nombre: " + pelicula.getNombre() +"\n")
            print ("Ano: " + pelicula.getAno() +"\n")
            print ("Actor: " + pelicula.getActor() +"\n")
        if(pEncontradas == 0):
            print("No se encuentran peliculas de este genero." +"\n")
            
        print("Desea realizar otra busqueda y/n")
        ans = input()        
        if ans == "y":
            self.initPeliculas()
            self.busquedas()
        else:
            exit

class Main:
    obj = BusquedaPeliculas()    
    obj.initPeliculas()
    obj.busquedas()
