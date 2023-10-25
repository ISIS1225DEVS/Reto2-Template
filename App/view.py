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
import tabulate as tb
from tabulate import tabulate
import traceback
import pandas as pd

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
    numero = input("Ingrese el número de partidos: ")
    nombre = input("Ingrese el nombre del equipo: ")
    condicion= input("Ingrese la condición del equipo: ")
    lista_p3_u3,lista,tiempo=controller.req_1(control,numero,nombre,condicion)
    x= len(lista)
    print("------REQ 1 INPUTS------")
    print("Número de partidos: "+numero)
    print("Nombre del equipo: "+nombre)
    print("Condición del equipo: "+condicion)
    print(f"    Only {x} matches found, selecting all... ")
    print("------REQ 1 RESULTS------")
    print("Total matches found: " + str(len(lista)))
    print(f"Selecting {numero} matches...")
    if len(lista) > 6:
        print("Results struct has more than 6 records...\n")
    else:
        print("Results struct has less than 6 records...\n")
    print("Tiempo de ejecución: "+str(tiempo))
    print(tb.tabulate(lista_p3_u3['elements'], headers='keys', tablefmt='fancy_grid'))
    


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    numero_de_goles = input("Ingrese el número de goles: ")
    nombre = input("Ingrese el nombre del jugador: ")
    lista,tiempo=controller.req_2(control,numero_de_goles,nombre)
    xd= len(lista)
    print("------REQ 2 INPUTS------")
    print("TOP N Goals: "+numero_de_goles)
    print("Player Name: "+nombre)
    print(f"    Only {xd} goals found, selecting all... ")
    print("------REQ 2 RESULTS------")
    print("Total matches found: " + str(len(lista)))
    print(f"Selecting {xd} matches...")
    if len(lista) > 6:
        print("Results struct has more than 6 records...\n")
    else:
        print("Results struct has less than 6 records...\n")
    print("Tiempo de ejecución: "+str(tiempo))
    print(tb.tabulate(lista['elements'], headers="keys", tablefmt='fancy_grid'))


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    equipo= input("Ingrese el nombre del equipo: ")
    fecha_i = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
    fecha_f = input("Ingrese la fecha final (YYYY-MM-DD): ")
    
    lista,tiempo=controller.req_3(control,equipo,fecha_i,fecha_f)
    xd= len(lista)
    print("------REQ 2 INPUTS------")
    print("Team name: "+equipo)
    print("Start date: "+fecha_i)
    print("End date: "+fecha_f)
    print(f"    Only {xd} goals found, selecting all... ")
    print("------REQ 2 RESULTS------")
    if len(lista) > 6:
        print("Results struct has more than 6 records...\n")
    else:
        print("Results struct has less than 6 records...\n")
    print("Tiempo de ejecución: "+str(tiempo))
    print(tb.tabulate(lista['elements'], headers='keys', tablefmt='fancy_grid'))


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
    total_jugadores, total_anotaciones, total_torneos, total_penal, total_autogoles, anotaciones_del_jugador = controller.req_5(control)

    print("Total de jugadores con anotaciones registradas:", total_jugadores)
    print("Total de anotaciones obtenidas por el jugador:", total_anotaciones)
    print("Total de torneos en que anotó el jugador:", total_torneos)
    print("Total de anotaciones obtenidas desde el punto penal:", total_penal)
    print("Total de autogoles cometidos:", total_autogoles)

    print("\nListado de anotaciones del jugador:")
    print(tb.tabulate(anotaciones_del_jugador, headers='keys', tablefmt='fancy_grid'))




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
    nombre_torneo = input("Ingrese el nombre del torneo: ")
    puntaje = int(input("Ingrese el puntaje de los jugadores: "))
    
    resultado = controller.req_7(control, nombre_torneo, puntaje)

    if resultado:
        total_torneos, total_anotadores, total_partidos, total_goles, total_penales, total_autogoles, lista_anotadores = resultado

        print("Resultados del Requerimiento 7:")
        print("Total de Torneos Disponibles para Consultar:", total_torneos)
        print("Total de Anotadores que Participaron en el Torneo:", total_anotadores)
        print("Total de Partidos en el Torneo:", total_partidos)
        print("Total de Goles Anotados durante los Partidos del Torneo:", total_goles)
        print("Total de Goles por Penal en el Torneo:", total_penales)
        print("Total de Autogoles en el Torneo:", total_autogoles)

        print("\nLista de Anotadores Ordenada por Criterio de Estadísticas:")
        for i, jugador in enumerate(lista_anotadores):
            print(f"\nJugador {i + 1}:")
            print("Nombre del Anotador:", jugador['Nombre del Anotador'])
            print("Puntaje del Jugador como Anotador:", jugador['Puntaje del Jugador'])
            print("Total de Goles Anotados:", jugador['Total de Goles Anotados'])
            print("Total de Goles por Penal Anotados:", jugador['Total de Goles por Penal Anotados'])
            print("Total de Autogoles Anotados:", jugador['Total de Autogoles Anotados'])
            print("Tiempo Promedio para Anotar en Minutos:", jugador['Tiempo Promedio para Anotar en Minutos'])
            print("Total de Torneos en que Anotó el Jugador:", jugador['Total de Torneos en que Anotó el Jugador'])
            print("Total de Anotaciones en Victorias:", jugador['Total de Anotaciones en Victorias'])
            print("Total de Anotaciones en Empates:", jugador['Total de Anotaciones en Empates'])
            print("Total de Anotaciones en Derrotas:", jugador['Total de Anotaciones en Derrotas'])
            print("Último Gol Anotado por el Jugador:")
            print("Fecha del Encuentro:", jugador['Último Gol Anotado']['Fecha del Encuentro'])
            print("Nombres de los Equipos Local y Visitante:", jugador['Último Gol Anotado']['Nombres de los Equipos Local y Visitante'])
            print("Puntaje de los Equipos Local y Visitante:", jugador['Último Gol Anotado']['Puntaje de los Equipos Local y Visitante'])
            print("Minuto en que Anotó el Gol:", jugador['Último Gol Anotado']['Minuto en que Anotó el Gol'])
            print("Detalles Técnicos del Gol:", jugador['Último Gol Anotado']['Detalles Técnicos del Gol'])
            print("-" * 50)
        print("Fin de la Lista de Anotadores")
    else:
        print("No se encontraron resultados para el Requerimiento 7.")


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
            results_file = input("ponga el nombre del archivo results EJ: results-utf8-small.csv")
            results, time_r, memory_r=load_results(control,results_file, memory, maptype, lf)
            goal_file= input("ponga el nombre del archivo goalscorers EJ:goalscorers-utf8-small.csv")
            goals, time_g, mem_g=load_goalscorers(control,goal_file, memory, maptype, lf)
            shootouts_file= input("ponga el nombre del archivo shootouts EJ: shootouts-utf8-small.csv")
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
