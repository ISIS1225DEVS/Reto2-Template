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

def add_goalscorers(data_structs, filename):
    '''
    Función para agregar nuevos elementos a la lista
    '''
    data_structs['goalscorers']=mp.newMap(maptype='PROBING')
    goles = lt.newList('ARRAY_LIST', filename=filename)
    for element in lt.iterator(goles):
        dic = {}
        dic['date'] = element['date']
        dic['home_team'] = element['home_team']
        dic['away_team'] = element['away_team']
        dic['scorer'] = element['scorer']
        dic['team'] = element['team']
        dic['minute'] = element['minute']
        dic['penalty'] = element['penalty']
        dic['own_goal'] = element['own_goal']
        mp.put(data_structs['goalscorers'], element['scorer'] + "-" + element["date"],dic)
    return data_structs


def add_results(data_structs, filename):
    results= lt.newList('ARRAY_LIST', filename=filename)
    data_structs['results'] = mp.newMap()
    for element in lt.iterator(results):
        dic = {}
        dic['date'] = element['date']
        dic['home_team'] = element['home_team']
        dic['away_team'] = element['away_team']
        dic['home_score'] = element['home_score']
        dic['away_score'] = element['away_score']
        dic['country'] = element['country']
        dic['city'] = element['city']
        dic['tournament'] = element['tournament'] 
        mp.put(data_structs['results'],element['date']+"-"+element['home_team'],dic)

    return data_structs

def add_shootouts(data_structs, filename):
    shootouts = lt.newList('ARRAY_LIST', filename=filename)
    data_structs['shootouts']=mp.newMap()
    for element in lt.iterator(shootouts):
        dic={}
        dic['date']= element['date']
        dic['home_team']=element['home_team']
        dic['away_team']=element['away_team']
        dic['winner']=element['winner']
        mp.put(data_structs['shootouts'],element['date']+element['home_team'],dic)
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


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


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
