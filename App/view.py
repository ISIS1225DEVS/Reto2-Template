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
    
    return controller.new_controller()

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Listar los ultimos N partidos de unequipo segun su condicion")
    print("3- Listar los primeros N goles anotados por un jugador")
    print("4- Consultar los partidos que disputo un equipo durante un periodo especifico")
    print("5- Consultar los partidos relacionados con un torneo durante un periodo especifico")
    print("6- Consultar las anotaciones de un jugador durante un periodo especifico")
    print("7- EClasificar los N mejores equipos del año dentro de un torno especifico")
    print("8- Clasificar los N mejores anotadores en partidos oficiales dentro de un periodo especifico")
    print("9- Consultar el desempeño historico de una seleccion en torneos oficiales")
    print("0- Salir")

def load_and_sort_data(control):
    """
    Carga los datos
    """
    
    tamaño = input("""Ingrese el numero asociado al tamaño de la muestra: \n
    1. Small \n
    2. 5% \n
    3. 10 % \n
    4. 20 % \n
    5. 30 % \n
    6. 50 % \n
    7. 80 % \n
    8. Large \n""")
    
    algoritmo = input("""Ingrese el numero asociado al algoritmo de ordenamiento que desea utilizar: \n
    1. Selection Sort \n
    2. Insertion Sort \n
    3. Shell Sort \n
    4. Merge Sort \n
    5. Quick Sort \n""")
    
    
    controller.load_and_sort_data(control, tamaño, algoritmo)
    
def print_table(data, headers):
    """
    Imprime los resultados
    """
    if lt.size(data) == 0:
        print("No se encontraron datos para mostrar")

    elif lt.size(data) > 6:
        first_three = lt.subList(data, 1, 3) 
        last_three = lt.subList(data, lt.size(data)-2, 3)
        combined_list = lt.newList("ARRAY_LIST")
        
        for i in lt.iterator(first_three):
            lt.addLast(combined_list, i)
        
        for i in lt.iterator(last_three):
            lt.addLast(combined_list, i)
        
        print(f"De {lt.size(data)} elementos, se muestran los primeros y ultimos 3\n")
        print(tabulate(lt.iterator(combined_list), headers, tablefmt="fancy_grid"))
        
    else:
        print(f"Se encontraron {lt.size(data)} elementos mostrados a continuacion\n")
        print(tabulate(lt.iterator(data), headers, tablefmt="fancy_grid"))
              
def print_data(control):
    
    headers_results = {"date": "Fecha",
                    "home_team": "Equipo local",
                    "away_team": "Equipo visitante",
                    "home_score": "Marcador local",
                    "away_score": "Marcador visitante",
                    "tournament": "Torneo",
                    "city": "Ciudad",
                    "country": "País",
                    "neutral": "Neutral"}
    
    headers_goalscorer = {"date": "Fecha",
                    "home_team": "Equipo local",
                    "away_team": "Equipo visitante",
                    "team": "Equipo",
                    "scorer": "Anotador",
                    "minute": "Minuto",
                    "own_goal": "Autogol",
                    "penalty": "Penal"}
    
    headers_shootouts = {"date": "Fecha",
                    "home_team": "Equipo local",
                    "away_team": "Equipo visitante",
                    "winner": "Ganador"}
    
    if lt.isEmpty(control["results"]) == False:
        print_table(control["results"], headers_results)
    
    if lt.isEmpty(control["goalscorers"]) == False:
        print_table(control["goalscorers"], headers_goalscorer)
    
    if lt.isEmpty(control["shootouts"]) == False:
        print_table(control["shootouts"], headers_shootouts)
        
def print_req_6(control):
    
    n_equipos = input("Ingrese el numero de equipos que desea consultar\n")
    torneo = input("Ingrese el nombre del torneo que desea consultar\n")
    año = input("Ingrese el año que desea consultar\n")
    
    equipos_a_mostrar, equipos_encontrados = controller.req_6(control, n_equipos, torneo, año)
    
    headers = {"equipo": "Equipo",
               "puntos_totales": "Puntos totales",
               "diferencia_goles": "Diferencia de goles",
               "partidos_jugados": "Partidos jugados",
               "goles_penal": "Goles de penal",
               "autogoles": "Autogoles",
               "victorias": "Victorias",
               "empates": "Empates",
               "derrotas": "Derrotas",
               "goles_favor": "Goles a favor",
               "goles_contra": "Goles en contra"}
    
    
    print("\n=============== Datos del usuario ==================")
    print(f"\nTorneo: {torneo}")
    print(f"\nAño de consulta: {año}")
    print(f"\nFecha inicial: {año}-01-01")
    print(f"\nFecha final: {año}-12-31")
    print(f"\nEquipos a mostrar: Top {n_equipos}")
    
    
    print("\n=============== Resultados ==================")
    print(f"Se encontraron {equipos_encontrados} equipos\n")
    print_table(equipos_a_mostrar, headers)

def print_req_7(control):
    
    headers = {"jugador": "Jugador",
               "puntos": "Puntos",
               "goles": "Goles",
               "goles_penal": "Goles de penal",
               "autogoles": "Autogoles",
               "minuto_promedio": "Minuto promedio",
               "goles_en_victorias": "Goles en victorias",
               "goles_en_empates": "Goles en empates",
                "goles_en_derrotas": "Goles en derrotas",
                "ultimo_partido": "Ultimo partido"}
    
    
    torneo = input("Ingrese el nombre del torneo que desea consultar\n")
    puntaje = input("Ingrese el puntaje que desea consultar\n")
    año_inicial = input("Ingrese el año inicial que desea consultar\n")
    mes_inicial = input("Ingrese el mes inicial que desea consultar\n")
    dia_inicial = input("Ingrese el dia inicial que desea consultar\n")
    año_final = input("Ingrese el año final que desea consultar\n")
    mes_final = input("Ingrese el mes final que desea consultar\n")
    dia_final = input("Ingrese el dia final que desea consultar\n")
    
    fecha_inicial = f"{año_inicial}-{mes_inicial}-{dia_inicial}"
    fecha_final = f"{año_final}-{mes_final}-{dia_final}"
    
    n_torneos, n_anotadores, n_anotadores_puntaje, n_goles, n_partidos, n_autogoles, n_penalties, jugadores = controller.req_7(control, torneo, puntaje, fecha_inicial, fecha_final)
    
    print("\n=============== Datos del usuario ==================")
    print(f"\nTorneo: {torneo}")
    print(f"\nJugadores con {puntaje} de puntaje")
    print(f"\nFecha inicial: {año_inicial}-{mes_inicial}-{dia_inicial}")
    print(f"\nFecha final: {año_final}-{mes_final}-{dia_final}")
    
    print("\n=============== Resultados ==================")
    print(f"\nSe encontraron {n_torneos} torneos")
    print(f"\nSe encontraron {n_anotadores} anotadores en el torneo {torneo}")
    print(f"\nSe encontraron {n_partidos} partidos en el torneo {torneo}")
    print(f"\nSe encontraron {n_goles} goles en el torneo {torneo}")
    print(f"\nSe encontraron {n_autogoles} autogoles en el torneo {torneo}")
    print(f"\nSe encontraron {n_penalties} penales en el torneo {torneo}")
    print(f"\nSe encontraron {n_anotadores_puntaje} anotadores con {puntaje} de puntaje")
    print_table(jugadores, headers)
    
    

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
            print("Cargando información de los archivos ....\n")
            data = load_and_sort_data(control)
            data_size = controller.get_datasize(control)
            print_data(control)
            print(f'Se cargaron {data_size[0]} resultados, {data_size[1]} penales y {data_size[2]} goleadores\n')
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
