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
from datetime import datetime
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
    list1 = lt.newList("ARRAY_LIST")
    for element in lt.iterator(mp.keySet(data_structs['model']['results'])):
        lista=me.getValue(mp.get(data_structs['model']['results'],element))
        
        if condicion.lower() == "home":
            if lista["home_team"].lower() == nombre.lower():
                lt.addLast(list1, lista)
        elif condicion.lower() == "away":
            if lista["away_team"].lower() == nombre.lower():
                lt.addLast(list1, lista)
        else:
            if lista["home_team"].lower() == nombre.lower():
                lt.addLast(list1, lista)
            if lista["away_team"].lower() == nombre.lower():
                lt.addLast(list1, lista)
    return list1

def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs,equipo,fecha_i,fecha_f):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    fecha_i = datetime.strptime(fecha_i, "%Y-%m-%d")
    fecha_f = datetime.strptime(fecha_f, "%Y-%m-%d")
    
    lista1 = lt.newList("ARRAY_LIST")
    for element in lt.iterator(mp.keySet(data_structs['model']['results'])):
        lista=me.getValue(mp.get(data_structs['model']['results'],element))
    
        if equipo in (lista["home_team"], lista["away_team"]):
            fecha_partido = datetime.strptime(lista["date"], "%Y-%m-%d")
            if fecha_i <= fecha_partido <= fecha_f:
                lt.addLast(lista1, lista)
    
    return lista1
    


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


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


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass

