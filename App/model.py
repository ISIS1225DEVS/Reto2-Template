"""
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
import time as tm
import pandas as pd

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
    data={
        'results':None,
        'goalscorers':None,
        'shootouts':None,
        'scores':None
    }
    data["scores"] = mp.newMap()
    return data



# Funciones para agregar informacion al modelo

def add_goalscorers(data_structs, filename,colision,lf):
    '''
    Función para agregar nuevos elementos a la lista
    '''
    data_structs['goalscorers']=mp.newMap(maptype=colision,loadfactor=lf)
    goles = lt.newList('ARRAY_LIST', filename=filename)
    for element in lt.iterator(goles):
        mp.put(data_structs['goalscorers'], element['scorer'] + "-" + element["date"], element)
    return data_structs


def add_results(data_structs, filename,colision,lf):
    results= lt.newList('ARRAY_LIST', filename=filename)
    data_structs['results'] = mp.newMap(maptype=colision,loadfactor=lf)
    for element in lt.iterator(results):
        mp.put(data_structs['results'],element['date']+"-"+element['home_team'],element)
    return data_structs

def add_shootouts(data_structs, filename,colision,lf):
    shootouts = lt.newList('ARRAY_LIST', filename=filename)
    data_structs['shootouts']=mp.newMap(maptype=colision,loadfactor=lf)
    for element in lt.iterator(shootouts):
        mp.put(data_structs['shootouts'],element['date']+element['home_team'],element)
    return data_structs

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass


def goalscorers_size(data_structs):
    return mp.size(data_structs['goalscorers'])

def results_size(data_structs):
    return mp.size(data_structs['results'])

def shootouts_size(data_structs):
    return mp.size(data_structs['shootouts'])


def req_1(data_structs,numero,nombre,condicion):
    '''
    Función que soluciona el requerimiento 1
    '''
    lista1 = lt.newList("ARRAY_LIST")
    for element in lt.iterator(mp.keySet(data_structs['model']['results'])):
        lista=me.getValue(mp.get(data_structs['model']['results'],element))
        
        if condicion == "home":
            if lista["home_team"] == nombre:
                lt.addLast(lista1, lista)
        elif condicion == "away":
            if lista["away_team"] == nombre:
                lt.addLast(lista1, lista)
        else:
            if lista["home_team"] == nombre:
                lt.addLast(lista1, lista)
            if lista["away_team"] == nombre:
                lt.addLast(lista1, lista)
    lista1= merg.sort(lista1, sort_criteria2)
    lista_p3 = lt.newList("ARRAY_LIST")
    pos1 = 2
    while pos1 >= 0:
        lt.addFirst(lista_p3, lista1["elements"][pos1])
        pos1 -= 1
    tamaño = lt.size(lista1) - 2
    lista_u3 = lt.subList(lista1, tamaño, 3)
    lista_p3_u3 = lt.newList("ARRAY_LIST")
    for element in lista_p3["elements"]:
        lt.addLast(lista_p3_u3, element)
    for element in lista_u3["elements"]:
        lt.addLast(lista_p3_u3, element)
    return lista_p3_u3  

def req_2(data_structs, numero_de_goles, nombre):
    """
    Función que soluciona el requerimiento 2 
    """
    lista1 = lt.newList("ARRAY_LIST")
    

    for element in lt.iterator(mp.keySet(data_structs['model']['goalscorers'])):
        lista = me.getValue(mp.get(data_structs['model']['goalscorers'], element))
        if lista["scorer"] == nombre:
            lt.addLast(lista1,lista)
    lista1= merg.sort(lista1, sort_criteria1)
    lista_p3 = lt.newList("ARRAY_LIST")
    pos1 = 2
    while pos1 >= 0:
        lt.addFirst(lista_p3, lista1["elements"][pos1])
        pos1 -= 1
    tamaño = lt.size(lista1) - 2
    lista_u3 = lt.subList(lista1, tamaño, 3)
    lista_p3_u3 = lt.newList("ARRAY_LIST")
    for element in lista_p3["elements"]:
        lt.addLast(lista_p3_u3, element)
    for element in lista_u3["elements"]:
        lt.addLast(lista_p3_u3, element)
    return lista_p3_u3 
    


def req_3(data_structs,equipo,fecha_i,fecha_f):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    fecha_i = tm.strptime(fecha_i, "%Y-%m-%d")
    fecha_f = tm.strptime(fecha_f, "%Y-%m-%d")
    
    lista1 = lt.newList("ARRAY_LIST")
    for element in lt.iterator(mp.keySet(data_structs['model']['results'])):
        lista=me.getValue(mp.get(data_structs['model']['results'],element))
    
        if equipo in (lista["home_team"], lista["away_team"]):
            fecha_partido = tm.strptime(lista["date"], "%Y-%m-%d")
            if fecha_i <= fecha_partido <= fecha_f:
                lt.addLast(lista1, lista)
    lista1= merg.sort(lista1, sort_criteria3)            
    lista_p3 = lt.newList("ARRAY_LIST")
    pos1 = 2
    while pos1 >= 0:
        lt.addFirst(lista_p3, lista1["elements"][pos1])
        pos1 -= 1
    tamaño = lt.size(lista1) - 2
    lista_u3 = lt.subList(lista1, tamaño, 3)
    lista_p3_u3 = lt.newList("ARRAY_LIST")
    for element in lista_p3["elements"]:
        lt.addLast(lista_p3_u3, element)
    for element in lista_u3["elements"]:
        lt.addLast(lista_p3_u3, element)
    return lista_p3_u3  
    


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    class AnotacionesModel:
        def __init__(self):
            self.goalscorers_df = data_structs["goalscorers"]

        def filtrar_anotaciones(self, nombre_jugador, fecha_inicio, fecha_fin):
            anotaciones_del_jugador = self.goalscorers_df[
                (self.goalscorers_df["Nombre del jugador que marcó el gol"] == nombre_jugador) &
                (self.goalscorers_df["Fecha del partido"] >= fecha_inicio) &
                (self.goalscorers_df["Fecha del partido"] <= fecha_fin)
            ]
            return anotaciones_del_jugador

        def obtener_estadisticas(self, anotaciones_del_jugador):
            total_jugadores = self.goalscorers_df["Nombre del jugador que marcó el gol"].nunique()
            total_anotaciones = len(anotaciones_del_jugador)
            total_torneos = anotaciones_del_jugador["Nombre del torneo"].nunique()
            anotaciones_penal = anotaciones_del_jugador[anotaciones_del_jugador["Tipo de anotación, si fue por falta desde el penal"] == "Sí"]
            total_penal = len(anotaciones_penal)
            autogoles = anotaciones_del_jugador[anotaciones_del-jugador["Tipo de anotación, si fue autogol"] == "Sí"]
            total_autogoles = len(autogoles)

            return total_jugadores, total_anotaciones, total_torneos, total_penal, total_autogoles




def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs, nombre_torneo, puntaje):
    # Inicializamos las variables para estadísticas
    total_torneos = 0
    total_anotadores = 0
    total_partidos = 0
    total_goles = 0
    total_penales = 0
    total_autogoles = 0

    # Creamos una lista para almacenar los datos de los anotadores
    lista_anotadores = []

    # Recorremos los resultados y buscamos las anotaciones dentro del torneo
    for elemento in mp.iterator(data_structs['results']):
        resultado = me.getValue(elemento)
        nombre_torneo_partido = resultado['Nombre del torneo']
        if nombre_torneo_partido == nombre_torneo:
            total_torneos += 1
            total_partidos += 1
            # Obtenemos las anotaciones de este partido
            anotaciones = resultado['Anotaciones']
            for anotacion in anotaciones:
                # Verificamos si el anotador ya está en la lista
                anotador_en_lista = False
                for jugador in lista_anotadores:
                    if jugador['Nombre del jugador'] == anotacion['Nombre del jugador']:
                        anotador_en_lista = True
                        jugador['Goles'] += 1
                        if anotacion['Tipo de anotación'] == 'Penal':
                            jugador['Penales'] += 1
                        if anotacion['Tipo de anotación'] == 'Autogol':
                            jugador['Autogoles'] += 1
                        jugador['Tiempos de anotación'].append(anotacion['Minuto'])
                        jugador['Torneos'].append(nombre_torneo)
                        jugador['Anotaciones por Resultado'][resultado['Resultado']] += 1
                        jugador['Último Gol'] = {
                            'Fecha': resultado['Fecha del partido'],
                            'Equipos': resultado['Equipos'],
                            'Puntaje': resultado['Puntaje'],
                            'Minuto': anotacion['Minuto'],
                            'Tipo de anotación': anotacion['Tipo de anotación']
                        }
                        break
                if not anotador_en_lista:
                    total_anotadores += 1
                    jugador = {
                        'Nombre del jugador': anotacion['Nombre del jugador'],
                        'Goles': 1,
                        'Penales': 0,
                        'Autogoles': 0,
                        'Tiempos de anotación': [anotacion['Minuto']],
                        'Torneos': [nombre_torneo],
                        'Anotaciones por Resultado': {
                            'Victoria': 0,
                            'Empate': 0,
                            'Derrota': 0
                        },
                        'Último Gol': {
                            'Fecha': resultado['Fecha del partido'],
                            'Equipos': resultado['Equipos'],
                            'Puntaje': resultado['Puntaje'],
                            'Minuto': anotacion['Minuto'],
                            'Tipo de anotación': anotacion['Tipo de anotación']
                        }
                    }
                    if anotacion['Tipo de anotación'] == 'Penal':
                        jugador['Penales'] = 1
                    if anotacion['Tipo de anotación'] == 'Autogol':
                        jugador['Autogoles'] = 1
                    jugador['Anotaciones por Resultado'][resultado['Resultado']] = 1
                    lista_anotadores.append(jugador)

                    total_goles += 1
                    if anotacion['Tipo de anotación'] == 'Penal':
                        total_penales += 1
                    if anotacion['Tipo de anotación'] == 'Autogol':
                        total_autogoles += 1

    # Ordenamos la lista de anotadores by the specified criteria
    lista_anotadores = sorted(lista_anotadores, key=lambda jugador: (-jugador['Goles'], jugador['Penales'], jugador['Autogoles'], min(jugador['Tiempos de anotación'])))
    
    # Filter the list of scorers based on the specified score (N)
    lista_anotadores_filtrada = [jugador for jugador in lista_anotadores if jugador['Goles'] - jugador['Autogoles'] + jugador['Penales'] >= puntaje]

    # Prepare the response with statistics
    respuesta = {
        'Total de Torneos Disponibles': total_torneos,
        'Total de Anotadores que Participaron en el Torneo': total_anotadores,
        'Total de Partidos dentro del Torneo': total_partidos,
        'Total de Anotaciones o Goles Obtenidos durante los Partidos del Torneo': total_goles,
        'Total de Goles por Penal Obtenidos en ese Torneo': total_penales,
        'Total de Autogoles en que Incurrieron los Anotadores en ese Torneo': total_autogoles,
        'Listado de Anotadores en ese Torneo': lista_anotadores_filtrada
    }

    return respuesta



def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria1(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    fecha1 = tm.strptime(data_1["date"], "%Y-%m-%d")
    fecha2 = tm.strptime(data_2["date"], "%Y-%m-%d")
    if fecha1 > fecha2:
        return True
    elif fecha1 == fecha2:
        if data_1["minute"] > data_2["minute"]:
            return True
        elif data_1["minute"] == data_2["minute"]:
            if data_1["scorer"].lower() >= data_2["scorer"].lower():
                return True
            else:
                return False
        else:
            return False
    else: 
        return False
    

def sort_criteria2(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    fecha1 = tm.strptime(data_1["date"], "%Y-%m-%d")
    fecha2 = tm.strptime(data_2["date"], "%Y-%m-%d")
    if fecha1 > fecha2:
        return True
    elif fecha1 == fecha2:
        if int(data_1["home_score"]) > int(data_2["home_score"]):
            return True
        elif int(data_1["home_score"]) == int(data_2["home_score"]):
            if int(data_1["away_score"]) >= int(data_2["away_score"]):
                return True
            else:
                return False
        else:
            return False
    else: 
        return False
            
def sort_criteria3(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    fecha1 = tm.strptime(data_1["date"], "%Y-%m-%d")
    fecha2 = tm.strptime(data_2["date"], "%Y-%m-%d")
    if fecha1 > fecha2:
        return True
    elif fecha1 == fecha2:
        if data_1["home_team"].lower() > data_2["home_team"].lower():
            return True
        elif data_1["home_team"].lower() == data_2["home_team"].lower():
            if data_1["away_team"].lower() >= data_2["away_team"].lower():
                return True
            else:
                return False
        else:
            return False
    else: 
        return False


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass