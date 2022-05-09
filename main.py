from claseViajeroFrecuente import ViajeroFrecuente
from ManejadorDeViajeros import ListaViajeros
from claseMenu import Menu
if __name__ == '__main__':
    lista=ListaViajeros()
    lista.Inicializar()
    bandera = False
    while not bandera:
        print("\nMENU DE OPCIONES")
        print("0 Salir")
        print("1 ITEM 6.1: Determinar el/los viajero/s con mayor cantidad de millas acumuladas.")
        print("2 ITEM 6.2: Acumular millas usando la sobrecarga del operador binario suma(+)")
        print("3 ITEM 6.3: Canjear millas usando la sobrecarga del operador binario resta(-)")

        opcion = int(input('Ingrese una opcion:'))
        unmenu=Menu()
        unmenu.opcion(opcion,lista)
        bandera = int(opcion)== 0
