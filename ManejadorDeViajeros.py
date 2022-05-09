import csv
from claseViajeroFrecuente import ViajeroFrecuente
class ListaViajeros:

    def __init__(self):
        self.__lista=[]


    def AgregarViajero(self,viajero):
        self.__lista.append(viajero)

    def Inicializar (self):
        archivo=open("ViajerosFrecuentes.csv")
        reader= csv.reader(archivo,delimiter=";")
        bandera= True
        for fila in reader:
            if bandera:
                bandera= not bandera
            else:
                numero= fila[0]
                dni= fila[1]
                nom= fila[2]
                ape= fila[3]
                millas= fila[4]
                unViajero=ViajeroFrecuente(numero,dni,nom,ape,millas)
                self.AgregarViajero(unViajero)
        archivo.close()

    def __str__(self):
        s=""
        for viajero in self.__lista:
            s += str(viajero)+'\n'
        return s

    def buscarViajero(self,num):
        i=0
        unViajero=self.__lista[i]
        unNum=unViajero.getNumero()
        while((num!=unNum)and(int(i)<9)):
            i+=1
            unViajero=self.__lista[i]
            unNum=unViajero.getNumero()
        if i<11:
            print("Se encontro el viajero")
            print(unViajero)
            return i




    def consultarMillas(self,i):
        print("La cantidad de millas son "+str(self.__lista[i].getMillas()))

    def acumularMilla(self,i):
        m= input("Ingrese la cantidad de millas a acumular >> ")
        unViajero=self.__lista[i]
        unViajero.acumularMillas(m)



    def comparar(self):
        mayor=0
        indice=0
        for i in range(len(self.__lista)):
            if (self.__lista[i].getMillas()>=mayor):
                mayor=self.__lista[i].getMillas()
                indice=i

        for j in range(len(self.__lista)):
            if j!=indice:
                if self.__lista[j].getMillas()==mayor:
                    self.__lista[j].mostrarDatos()

        self.__lista[indice].mostrarDatos()





    def acumularMillas(self,i):
        millas=input("Ingrese la cantidad de millas")
        unViajero=self.__lista[i]
        unViajero+millas
        print("Se sumaron las millas {}".format(unViajero.getMillas()))

    def canjearMillas(self,i):
        millas=input("Ingrese la cantidad de millas")
        unViajero=self.__lista[i]
        unViajero-millas
        print("Se canjearon las millas {}".format(unViajero.getMillas()))





