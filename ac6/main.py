from manejador import ManejadorViajero
from viajero import Viajero
import os

if __name__=='__main__':
    lista = ManejadorViajero()
    lista.GenerarLista()
    lista.ListarViajeros()

    
    continuar = True

    while continuar:
        print("MENU".center(20,"-"))
        print("[1] Determinar el/los viajero/s con mayor cantidad de millas acumuladas. (Con sobrecarga de operadores)")
        print("[2] Acumular millas. (Con sobrecarga de operadores)")
        print("[3] Para canjear millas. (Con sobrecarga de operadores)")
        print("[0] Para SALIR del menu.")

        op = int( input("INGRESE OPCION POR TECLADO\n"))
        os.system("cls")
        if ( op == 1):
            print("".center(20,"-"))
            print("El viajero con mayor cantidad de millas acumuladas es:" )
            print(lista.MayorCantidad())
            print("".center(20,"-"))
        elif(op == 2):
            NroViaj= int(input("Ingrese nro de viajero del cual desea consultar\n"))
            Viajero= lista.buscar(NroViaj)
            millasAcum = int(input("Ingrese cantidad de millas a acumular\n"))
            Viajero = Viajero + millasAcum
            print("MILLAS ACUMULADAS:")
            print(Viajero)
            print("".center(20,"-"))

        elif(op == 3):
            NroViaj= int(input("Ingrese nro de viajero del cual desea consultar\n"))
            Viajero= lista.buscar(NroViaj)
            millasCanj = int(input("Ingrese cantidad de millas a canjear\n"))
            Viajero = Viajero - millasCanj
            print("MILLAS CANJEADAS:")
            print(Viajero)
            print("".center(20,"-"))
        elif(op == 0):
            continuar = not continuar