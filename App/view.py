"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    control = controller.newController()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_goalscorers(control,filename, memory, maptype, lf):
    """
    Carga los datos
    """
    goalscorers = controller.load_goalscorers(control,
                                 filename, memory, maptype, lf)
    
    return goalscorers

def load_results(control,filename, memory, maptype, lf):
    results = controller.load_results(control,
                                      filename, memory, maptype, lf)
    
    return results

def load_shootouts(control,filename, memory, maptype, lf):
    shootouts = controller.load_shootouts(control,
                                        filename,memory, maptype, lf)
    
    
    return shootouts

def printLoadDataAnswer(tiempo, memoria, bool): 
    """ 
    Imprime los datos de tiempo y memoria de la carga de datos 
    """ 
    if bool == True and memoria != 0.0: 
        print("Tiempo [ms]: ", round(tiempo,2), "||", 
        "Memoria [kB]: ", round(memoria,2)) 
    else: 
        print("Tiempo [ms]: ",round(tiempo,2))

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        inputs = input('Seleccione una opción para continuar\n')
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("¿Desea observar el uso de memoria en la carga de datos?, (True, False)")
            mem = input("Respuesta: \n")
            if mem == "True":
                memory = True
            else:
                memory = False
            print("Seleccione el tipo de mapa que desea usar: \n")
            print("1. Separate Chaining")
            print("2. Linear Probing")
            temp = input("Respuesta: \n")
            if int(temp) == 1:
                maptype = "CHAINING"
            else:
                maptype = "PROBING"
            lf = float(input("Ingrese el factor de carga deseado: \n"))
            results_file=input("Diga a cual csv de results quiere acceder: \n")
            results, time_r, memory_r=load_results(control,results_file, memory, maptype, lf)
            goal_file=input("Diga a cual csv de goalscorers quiere acceder: \n")
            goals, time_g, mem_g=load_goalscorers(control,goal_file, memory, maptype, lf)
            shootouts_file=input("Diga a cual csv de shootouts quiere acceder: \n")
            shootouts, time_s, memory_s=load_shootouts(control,shootouts_file, memory, maptype, lf)
            print("Cargando información de los archivos ....\n")
            print('Results: '+str(results))
            printLoadDataAnswer(time_r, memory_r, memory)
            print('Goalscorers: '+str(goals))
            printLoadDataAnswer(time_g, mem_g, memory)
            print('Shootouts: '+str(shootouts))
            printLoadDataAnswer(time_s, memory_s, memory)
            print("Tiempo total de carga: "+str(time_r+time_g+time_s))
            print("Memoria total de carga: "+str(memory_r+mem_g+memory_s))
            print("La información ha sido cargada correctamente\n")
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
