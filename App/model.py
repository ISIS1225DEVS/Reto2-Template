﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import time
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos

def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    football_data = {"results": None,
                     "shootouts": None,
                     "goalscorers": None,
                     "hash_results": None,
                     "hash_shootouts": None,
                     "hash_goalscorers": None}
    
    football_data["results"] = lt.newList("ARRAY_LIST")
    football_data["shootouts"] = lt.newList("ARRAY_LIST")
    football_data["goalscorers"] = lt.newList("ARRAY_LIST")
    football_data["hash_results"] = mp.newMap()
    football_data["hash_shootouts"] = mp.newMap()
    football_data["hash_goalscorers"] = mp.newMap()
    football_data["hash_scorers"] = mp.newMap()
        
    return football_data

# Funciones para agregar informacion al modelo

def add_data(data_structs, data, archivo):
    """
    Función para agregar nuevos elementos a la lista
    """
    lt.addLast(data_structs[archivo], data)
    
def get_datasize(data_structs):
    """
    Retorna el tamaño de los datos cargados
    """
    results_size = lt.size(data_structs["results"])
    shootouts_size = lt.size(data_structs["shootouts"])
    goalscorers_size = lt.size(data_structs["goalscorers"])
    
    return results_size, shootouts_size, goalscorers_size

def creating_hash(control):
    
    hash_results = mp.newMap()
    
    for i in lt.iterator(control["results"]):
        key = f'{i["date"]}-{i["home_team"]}-{i["away_team"]}'
        value = i
        mp.put(hash_results, key, value)
        
    hash_shootouts = mp.newMap()
    
    for i in lt.iterator(control["shootouts"]):
        key = f'{i["date"]}-{i["home_team"]}-{i["away_team"]}'
        value = i
        mp.put(hash_shootouts, key, value)
        
    hash_goalscorers = mp.newMap()
    
    for i in lt.iterator(control["goalscorers"]):
        key = f'{i["date"]}-{i["home_team"]}-{i["away_team"]}'
        
        if not mp.contains(hash_goalscorers, key):
            temporal_list = lt.newList("ARRAY_LIST")
            lt.addLast(temporal_list, i)
            mp.put(hash_goalscorers, key, temporal_list)
        
        else:
            temporal_list = mp.get(hash_goalscorers, key)["value"]
            lt.addLast(temporal_list, i)
            mp.put(hash_goalscorers, key, temporal_list)
            
            
    hash_scorers = mp.newMap()
    
    for i in lt.iterator(control["goalscorers"]):
        key = i["scorer"]
        
        if not mp.contains(hash_scorers, key):
            temporal_list = lt.newList("ARRAY_LIST")
            lt.addLast(temporal_list, i)
            mp.put(hash_scorers, key, temporal_list)
        
        else:
            temporal_list = mp.get(hash_scorers, key)["value"]
            lt.addLast(temporal_list, i)
            mp.put(hash_scorers, key, temporal_list)
        

    control["hash_results"] = hash_results
    control["hash_shootouts"] = hash_shootouts
    control["hash_goalscorers"] = hash_goalscorers
    control["hash_scorers"] = hash_scorers
    
#Requerimientos

def req_1(control, n_partidos, equipo, condicion):
    
    partidos = lt.newList("ARRAY_LIST")
    equipos = set()
    partidos_equipo = 0
    
    for resultado in lt.iterator(control["results"]):
        
        equipos.add(resultado["home_team"])
        equipos.add(resultado["away_team"])
       
        if resultado["home_team"] == equipo or resultado["away_team"] == equipo:
            
            partidos_equipo += 1
            
            if condicion == "3":
                lt.addLast(partidos, resultado)
            
            elif condicion == "2":
                if resultado["away_team"] == equipo or (resultado["home_team"] == equipo and resultado["neutral"] == "True"):
                    lt.addLast(partidos, resultado)
            
            elif condicion == "1":
                if resultado["home_team"] == equipo and resultado["neutral"] == "False":
                    lt.addLast(partidos, resultado)
            
            
    return len(equipos), partidos_equipo, lt.size(partidos), partidos
            
def req_2(control, n_goles, jugador):
    
    goles = mp.get(control["hash_scorers"], jugador)["value"]
    jugadores = mp.size(control["hash_scorers"])
    goles_jugador = lt.size(goles)
    goles_penal = 0
    
    for gol in goles:
        if gol["penalty"] == "True":
            goles_penal += 1
            
    if n_goles > goles_jugador:
        goles_a_mostrar = lt.subList(goles, 1, goles_jugador)
        
    else:
        goles_a_mostrar = goles
        
    return jugadores, goles_jugador, goles_penal, goles_a_mostrar
    
def req_3(control, equipo, fecha_inicial, fecha_final):
    
    equipos = set()
    partidos_local = 0
    partidos_visitante = 0
    partidos_por_equipo = lt.newList("ARRAY_LIST")
    
    for resultado in lt.iterator(control["results"]):
        
        equipos.add(resultado["home_team"])
        equipos.add(resultado["away_team"])
        
        if (resultado["home_team"] == equipo or resultado["away_team"] == equipo) and intervalo(fecha_inicial, fecha_final, resultado["date"]):
            
            resultado["penalties"] = "Falso"
            resultado["autogoles"] = "Falso"
            
            if mp.contains(control["hash_goalscorers"], f"{resultado['date']}-{resultado['home_team']}-{resultado['away_team']}"):
                lista_goles = mp.get(control["hash_goalscorers"], f"{resultado['date']}-{resultado['home_team']}-{resultado['away_team']}")["value"]
                for i in lt.iterator(lista_goles):
                    if i["team"] == equipo and i["own_goal"] == "True":
                        resultado["autogoles"] = "Verdadero"
                    if i["team"] == equipo and i["penalty"] == "True":
                        resultado["penalties"] = "Verdadero"
            
            if resultado["home_team"] == equipo:
                partidos_local += 1
            else:
                partidos_visitante += 1
                
            lt.addLast(partidos_por_equipo, resultado)
            
    return len(equipos), partidos_local, partidos_visitante, partidos_por_equipo, lt.size(partidos_por_equipo)     

def req_4(control, torneo, fecha_inicial, fecha_final):
    
    torneos = set()
    paises = set()
    ciudades = set()
    partidos_con_penales = 0
    partidos_torneo = lt.newList("ARRAY_LIST")
    
    for resultado in lt.iterator(control["results"]):
        
        if resultado["tournament"] == torneo and intervalo(fecha_inicial, fecha_final, resultado["date"]):
            
            
            if not mp.contains(control["hash_shootouts"], f'{resultado["date"]}-{resultado["home_team"]}-{resultado["away_team"]}'):
                resultado["penalties"] = "Falso"
                resultado["ganador_penales"] = "Nadie"
                
            else:
                resultado["penalties"] = "Verdadero"
                resultado["ganador_penales"] = mp.get(control["hash_shootouts"], f'{resultado["date"]}-{resultado["home_team"]}-{resultado["away_team"]}')['value']["winner"]
                partidos_con_penales += 1
            
            if resultado["tournament"] not in torneos:
                torneos.add(resultado["tournament"])
                
            if resultado["country"] not in paises:
                paises.add(resultado["country"])
                
            if resultado["city"] not in ciudades:
                ciudades.add(resultado["city"])
                
            lt.addLast(partidos_torneo, resultado)
            
    return len(torneos), len(paises), len(ciudades), lt.size(partidos_torneo), partidos_con_penales, partidos_torneo
                
def req_5(control, anotador, fecha_inicial, fecha_final):
    
    goles = lt.newList("ARRAY_LIST")
    jugadores = set()
    torneos = set()
    penales = 0
    autogoles = 0
    
    for gol in lt.iterator(control["goalscorers"]):
        
        if not gol["scorer"] in jugadores:
            jugadores.add(gol["scorer"])
        
        if gol["scorer"] == anotador and intervalo(fecha_inicial, fecha_final, gol["date"]):
            if not mp.contains(control["hash_results"], f'{gol["date"]}-{gol["home_team"]}-{gol["away_team"]}'):
                gol["home_score"] = "Desconocido"
                gol["away_score"] = "Desconocido"
                gol["tournament"] = "Desconocido"
                lt.addLast(goles, gol)
                
            else:
                partido = mp.get(control["hash_results"], f'{gol["date"]}-{gol["home_team"]}-{gol["away_team"]}')['value']
                gol["home_score"] = partido["home_score"]
                gol["away_score"] = partido["away_score"]
                gol["tournament"] = partido["tournament"]
                lt.addLast(goles, gol)
                
            if gol["penalty"] == "True":
                penales += 1
            
            if gol["own_goal"] == "True":
                autogoles += 1
                
            if not gol["tournament"] in torneos:
                torneos.add(gol["tournament"])
            
               
            
    return len(jugadores), len(goles), len(torneos), penales, autogoles, goles

def req_6(control, n_equipos, torneo, año):
    
    #Funciones auxiliares
    
    def puntos_obtenidos(partido, equipo):
        
        if equipo == partido["home_team"]:
            if int(partido["home_score"]) > int(partido["away_score"]):
                return 3, [1, 0, 0]
            elif int(partido["home_score"]) == int(partido["away_score"]):
                return 1, [0, 1, 0]
            else:
                return 0, [0, 0, 1]
        
        elif equipo == partido["away_team"]:
            if int(partido["home_score"]) < int(partido["away_score"]):
                return 3, [1, 0, 0]
            elif int(partido["home_score"]) == int(partido["away_score"]):
                return 1, [0, 1, 0]
            else:
                return 0, [0, 0, 1]
    
    def calcular_goles_tipo(control, partido, equipo):
        
        llave = f'{partido["date"]}-{partido["home_team"]}-{partido["away_team"]}'
        
        
        
        if mp.contains(control["hash_goalscorers"], llave):
            
            lista_goles = mp.get(control["hash_goalscorers"], llave)["value"]
            
            penalty_goals = 0
            own_goals = 0
            
            for i in lt.iterator(lista_goles):
                if i["team"] == equipo and i["penalty"] == "True":
                    penalty_goals += 1
                elif i["team"] == equipo and i["own_goal"] == "True":
                    own_goals += 1
            return penalty_goals, own_goals          
        else:
            return 0, 0
    
    def crear_informacion(control, partido):
        
        equipo_uno = {"equipo": partido["home_team"],
                      "puntos_totales": puntos_obtenidos(partido, partido["home_team"])[0],
                      "diferencia_goles": int(partido["home_score"]) - int(partido["away_score"]),
                      "partidos_jugados": 1,
                      "goles_penal": calcular_goles_tipo(control, partido, partido["home_team"])[0],
                      "autogoles": calcular_goles_tipo(control, partido, partido["home_team"])[1],
                      "victorias": puntos_obtenidos(partido, partido["home_team"])[1][0],\
                      "empates": puntos_obtenidos(partido, partido["home_team"])[1][1],
                      "derrotas": puntos_obtenidos(partido, partido["home_team"])[1][2],
                      "goles_favor": int(partido["home_score"]),
                      "goles_contra": int(partido["away_score"])}
        
        equipo_dos = {"equipo": partido["away_team"],
                      "puntos_totales": puntos_obtenidos(partido, partido["away_team"])[0],
                      "diferencia_goles": int(partido["away_score"]) - int(partido["home_score"]),
                      "partidos_jugados": 1,
                      "goles_penal": calcular_goles_tipo(control, partido, partido["away_team"])[0],
                      "autogoles": calcular_goles_tipo(control, partido, partido["away_team"])[1],
                      "victorias": puntos_obtenidos(partido, partido["away_team"])[1][0],\
                      "empates": puntos_obtenidos(partido, partido["away_team"])[1][1],
                      "derrotas": puntos_obtenidos(partido, partido["away_team"])[1][2],
                      "goles_favor": int(partido["away_score"]),
                      "goles_contra": int(partido["home_score"])}
        
        return equipo_uno, equipo_dos
        
    def modificar_informacion(nueva_info, info):
        
        info["puntos_totales"] += nueva_info["puntos_totales"]
        info["diferencia_goles"] += nueva_info["diferencia_goles"]
        info["partidos_jugados"] += nueva_info["partidos_jugados"]
        info["goles_penal"] += nueva_info["goles_penal"]
        info["autogoles"] += nueva_info["autogoles"]
        info["victorias"] += nueva_info["victorias"]
        info["empates"] += nueva_info["empates"]
        info["derrotas"] += nueva_info["derrotas"]
        info["goles_favor"] += nueva_info["goles_favor"]
        info["goles_contra"] += nueva_info["goles_contra"]
        
        return info   
        
    def sort_criteria_equipos(data1, data2):
        
        if data1["puntos_totales"] > data2["puntos_totales"]:
            return True
        elif data1["puntos_totales"] == data2["puntos_totales"]:
            if data1["diferencia_goles"] > data2["diferencia_goles"]:
                return True
            elif data1["diferencia_goles"] == data2["diferencia_goles"]:
                if data1["goles_penal"] > data2["goles_penal"]:
                    return True
                elif data1["goles_penal"] == data2["goles_penal"]:
                    if data1["partidos_jugados"] < data2["partidos_jugados"]:
                        return True
                    elif data1["partidos_jugados"] == data2["partidos_jugados"]:
                        if data1["autogoles"] < data2["autogoles"]:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

        
    mapa_indices = mp.newMap()
    equipos = lt.newList("ARRAY_LIST")

    #Implementacion algoritmo principal
    
    torneos = set()
    ciudades = set()
    paises = set()
    partidos = 0
    
    for resultado in lt.iterator(control["results"]):
        
        if resultado["tournament"] == torneo and resultado["date"].split("-")[0] == año:
            
            equipo_uno, equipo_dos = crear_informacion(control, resultado)
            
            if not mp.contains(mapa_indices, equipo_uno["equipo"]):
                lt.addLast(equipos, equipo_uno)
                mp.put(mapa_indices, equipo_uno["equipo"], lt.size(equipos))
                
            else:
                indice = mp.get(mapa_indices, equipo_uno["equipo"])["value"]
                info = lt.getElement(equipos, indice)
                nueva_info = modificar_informacion(equipo_uno, info)
                lt.changeInfo(equipos, indice, nueva_info)
                
            if not mp.contains(mapa_indices, equipo_dos["equipo"]):
                lt.addLast(equipos, equipo_dos)
                mp.put(mapa_indices, equipo_dos["equipo"], lt.size(equipos))
            
            else:
                indice = mp.get(mapa_indices, equipo_dos["equipo"])["value"]
                info = lt.getElement(equipos, indice)
                nueva_info = modificar_informacion(equipo_dos, info)
                lt.changeInfo(equipos, indice, nueva_info)
                
            if not resultado["tournament"] in torneos:
                torneos.add(resultado["tournament"])
            
            if not resultado["city"] in ciudades:
                ciudades.add(resultado["city"])
            
            if not resultado["country"] in paises:
                paises.add(resultado["country"])
                
                
    merg.sort(equipos, sort_criteria_equipos)
    equipos_encontrados = lt.size(equipos)
    
    if equipos_encontrados >= int(n_equipos):
        equipos_a_mostrar = lt.subList(equipos, 1, int(n_equipos))
    
    else:
        equipos_a_mostrar = equipos
        
    return equipos_a_mostrar, equipos_encontrados, len(torneos), partidos, len(ciudades), len(paises)
        
def req_7(control, torneo, puntaje, fecha_inicio, fecha_fin):
    
    def check_penalty(gol):
        
        if gol["penalty"] == "True":
            return 2, 1
        else:
            return 1, 0
        
    def check_autogol(gol):
        
        if gol["own_goal"] == "True":
            return 1
        else:
            return 0
    
    def determinar_condicion(gol, control):
        
        llave = f'{gol["date"]}-{gol["home_team"]}-{gol["away_team"]}'
        
        if mp.contains(control["hash_results"], llave):
            
            partido = mp.get(control["hash_results"], llave)["value"]
            
            if gol["team"] == partido["home_team"]:
                if int(partido["home_score"]) > int(partido["away_score"]):
                    return [1, 0, 0]
                
                elif int(partido["home_score"]) == int(partido["away_score"]):
                    return [0, 1, 0]
                
                else:
                    return [0, 0, 1]
                
            elif gol["team"] == partido["away_team"]:
                if int(partido["home_score"]) < int(partido["away_score"]):
                    return [1, 0, 0]
                
                elif int(partido["home_score"]) == int(partido["away_score"]):
                    return [0, 1, 0]
                
                else:
                    return [0, 0, 1]
                
        else:
            return [0, 0, 0]     
    
    def crear_informacion(control, gol):
        info = {"jugador": gol["scorer"],
               "puntos": check_penalty(gol)[0],
               "goles": 1,
               "goles_penal": check_penalty(gol)[1],
               "autogoles": check_autogol(gol),
               "minuto_promedio": float(gol["minute"]),
               "goles_en_victorias": determinar_condicion(gol, control)[0],
               "goles_en_empates": determinar_condicion(gol, control)[1],
               "goles_en_derrotas": determinar_condicion(gol, control)[2],
               "ultimo_partido": mp.get(control["hash_results"], f'{gol["date"]}-{gol["home_team"]}-{gol["away_team"]}' )["value"]}
        
        return info
           
    def modificar_informacion(nueva_info, info):
        
        info["puntos"] += nueva_info["puntos"]
        info["goles"] += nueva_info["goles"]
        info["goles_penal"] += nueva_info["goles_penal"]
        info["autogoles"] += nueva_info["autogoles"]
        info["minuto_promedio"] = ((info["minuto_promedio"] * (info["goles"]-1)) + nueva_info["minuto_promedio"] ) / (info["goles"])
        info["goles_en_victorias"] += nueva_info["goles_en_victorias"]
        info["goles_en_empates"] += nueva_info["goles_en_empates"]
        info["goles_en_derrotas"] += nueva_info["goles_en_derrotas"]
        info["ultimo_partido"] = nueva_info["ultimo_partido"]
    
        return info
    
    def sort_criteria_req_7(data_1, data_2):
        
        if data_1["puntos"] > data_2["puntos"]:
            return True
        elif data_1["puntos"] == data_2["puntos"]:
            if data_1["goles"] > data_2["goles"]:
                return True
            elif data_1["goles"] == data_2["goles"]:
                if data_1["goles_penal"] > data_2["goles_penal"]:
                    return True
                elif data_1["goles_penal"] == data_2["goles_penal"]:
                    if data_1["autogoles"] < data_2["autogoles"]:
                        return True
                    elif data_1["autogoles"] == data_2["autogoles"]:
                        if data_1["minuto_promedio"] < data_2["minuto_promedio"]:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
        
    
    lista_jugadores = lt.newList("ARRAY_LIST")
    mapa_indices = mp.newMap()
    
    torneos = set()
    partidos = set()
    n_goles = 0
    n_autogoles = 0
    n_penalties = 0
    
    for gol in lt.iterator(control["goalscorers"]):
        
        llave = f'{gol["date"]}-{gol["home_team"]}-{gol["away_team"]}'
        
        if mp.contains(control["hash_results"], llave):
            
            partido = mp.get(control["hash_results"], llave)["value"]
            gol_torneo = partido["tournament"]
        
            if gol_torneo == torneo and intervalo(fecha_inicio, fecha_fin, gol["date"]):
                
                if not mp.contains(mapa_indices, gol["scorer"]):
                    lt.addLast(lista_jugadores, crear_informacion(control, gol))
                    mp.put(mapa_indices, gol["scorer"], lt.size(lista_jugadores))
                    
                else:
                    indice = mp.get(mapa_indices, gol["scorer"])["value"]
                    info = lt.getElement(lista_jugadores, indice)
                    nueva_info = modificar_informacion(crear_informacion(control, gol), info)
                    lt.changeInfo(lista_jugadores, indice, nueva_info)
                    
                if not gol_torneo in torneos:
                    torneos.add(gol_torneo)
                    
                if not llave in partidos:
                    partidos.add(llave)
                    
                n_goles += 1
                n_autogoles += check_autogol(gol)
                n_penalties += check_penalty(gol)[1]
            
    jugadores_puntos = lt.newList("ARRAY_LIST")
    
    for i in lt.iterator(lista_jugadores):
        if i["puntos"] == int(puntaje):
            lt.addLast(jugadores_puntos, i)
                        
    n_anotadores_puntaje = lt.size(jugadores_puntos)
    merg.sort(jugadores_puntos, sort_criteria_req_7)
            
            
                
    return len(torneos), lt.size(lista_jugadores), n_anotadores_puntaje, n_goles, len(partidos), n_autogoles, n_penalties, jugadores_puntos       
    
#Funcion de ordenamiento y sus auxiliares
    
def sort(control, algoritmo):
    if algoritmo == "1":
        ins.sort(control["results"], sort_criteria_results)
        ins.sort(control["shootouts"], sort_criteria_shootouts)
        ins.sort(control["goalscorers"], sort_criteria_goalscorers)
    elif algoritmo == "2":
        se.sort(control["results"], sort_criteria_results)
        se.sort(control["shootouts"], sort_criteria_shootouts)
        se.sort(control["goalscorers"], sort_criteria_goalscorers)
    elif algoritmo == "3":
        sa.sort(control["results"], sort_criteria_results)
        sa.sort(control["shootouts"], sort_criteria_shootouts)
        sa.sort(control["goalscorers"], sort_criteria_goalscorers)
    elif algoritmo == "4":
        merg.sort(control["results"], sort_criteria_results)
        merg.sort(control["shootouts"], sort_criteria_shootouts)
        merg.sort(control["goalscorers"], sort_criteria_goalscorers)
    elif algoritmo == "5":
        quk.sort(control["results"], sort_criteria_results)
        quk.sort(control["shootouts"], sort_criteria_shootouts)
        quk.sort(control["goalscorers"], sort_criteria_goalscorers)
    else:
        print("Algoritmo no valido")        
        
def sort_criteria_results(data1, data2):
    
    date_1 = data1["date"]
    date_2 = data2["date"]
    
    if comparar_fechas(date_1, date_2) == 1:
        return True
    elif comparar_fechas(date_1, date_2) == 0:
        if int(data1["home_score"]) > int(data2["home_score"]):
            return True
        elif int(data1["home_score"]) == int(data2["home_score"]):
            if int(data1["away_score"]) > int(data2["away_score"]):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
def sort_criteria_goalscorers(data1, data2):
    
    date_1 = data1["date"]
    date_2 = data2["date"]
    
    if comparar_fechas(date_1, date_2) == 1:
        return True
    elif comparar_fechas(date_1, date_2) == 0:
        if (data1["minute"]) > (data2["minute"]):
            return True
        elif (data1["minute"]) == (data2["minute"]):
            if data1["scorer"] > data2["scorer"]:
                return True
            else:
                return False
        else:
            return False       
    else:
        return False  

def sort_criteria_shootouts(data1, data2):
    
    date_1 = data1["date"]
    date_2 = data2["date"]
    
    if comparar_fechas(date_1, date_2) == 1:
        return True
    elif comparar_fechas(date_1, date_2) == 0:
        if data1["home_team"] > data2["home_team"]:
            return True
        elif data1["home_team"] == data2["home_team"]:
            if data1["away_team"] > data2["away_team"]:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
def comparar_fechas(fecha_1, fecha_2):
    
    #Retorna 1 si la fecha 1 es mayor que la fecha 2
    #Retorna 0 si las fechas son iguales
    #Retorna -1 si la fecha 1 es menor que la fecha 2
    
    fecha_1 = fecha_1.split("-")
    fecha_2 = fecha_2.split("-")
    
    
    if int(fecha_1[0]) > int(fecha_2[0]):
        return 1
    elif int(fecha_1[0]) == int(fecha_2[0]):
        if int(fecha_1[1]) > int(fecha_2[1]):
            return 1
        elif int(fecha_1[1]) == int(fecha_2[1]):
            if int(fecha_1[2]) > int(fecha_2[2]):
                return 1
            elif int(fecha_1[2]) == int(fecha_2[2]):
                return 0
            else:
                return -1
        else:
            return -1
    else:
        return -1

def intervalo(fecha_inicial, fecha_final, fecha):
    
    #Retorna True si la fecha esta dentro del intervalo y False si no lo está
    
    if comparar_fechas(fecha, fecha_inicial) == 1 and comparar_fechas(fecha, fecha_final) == -1:
        return True
    elif comparar_fechas(fecha, fecha_inicial) == 0 or comparar_fechas(fecha, fecha_final) == 0:
        return True
    else:
        return False