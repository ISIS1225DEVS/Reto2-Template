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
 """

import config as cf
import model
import time
import csv
import tracemalloc
import os
"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def newController():
    """
    Crea una instancia del modelo
    """
    control = {
        'model': None
    }
    control['model'] = model.new_data_structs()
    return control


# Funciones para la carga de datos

def load_goalscorers(control, filename, memory, mapa, lf):
    """
    Carga los datos del reto
    """
    inicio_time = get_time()
    if memory==True:
        tracemalloc.start()
        inicio_memory = get_memory()
         
    data_structs = control["model"]
    
    goalscorersfile = os.path.join(cf.data_dir, filename)
    
    data_structs = model.add_goalscorers(data_structs, goalscorersfile, mapa, lf)
    stop_time = get_time()
    diff_time = delta_time(inicio_time, stop_time)
    if memory == True:
        stop_memory = get_memory()
        tracemalloc.stop()
        diff_memory = delta_memory(stop_memory, inicio_memory)
        return model.goalscorers_size(data_structs), diff_time, diff_memory
    else:
        return model.goalscorers_size(data_structs), diff_time, 0.0
    

def load_results(control, filename, memory, mapa, lf):
    inicio_time = get_time()
    if memory==True:
        tracemalloc.start()
        inicio_memory = get_memory()
        
    data_structs = control["model"]
    
    resultsfile = os.path.join(cf.data_dir, filename)
    
    data_structs = model.add_results(data_structs, resultsfile, mapa, lf)
    stop_time = get_time()
    diff_time = delta_time(inicio_time, stop_time)
    if memory == True:
        stop_memory = get_memory()
        tracemalloc.stop()
        diff_memory = delta_memory(stop_memory, inicio_memory) 
        return model.results_size(data_structs), diff_time, diff_memory
    else:
        return model.results_size(data_structs), diff_time, 0.0
    

def load_shootouts(control, filename, memory, mapa, lf):
    inicio_time = get_time()
    if memory==True:
        tracemalloc.start()
        inicio_memory = get_memory()
    data_structs = control["model"]
    
    shootoutsfile = os.path.join(cf.data_dir, filename)
    
    data_structs = model.add_shootouts(data_structs, shootoutsfile, mapa, lf)

    stop_time = get_time()
    diff_time = delta_time(inicio_time, stop_time)
    if memory == True:
        stop_memory = get_memory()
        tracemalloc.stop()
        diff_memory = delta_memory(stop_memory, inicio_memory)
        return model.shootouts_size(data_structs), diff_time, diff_memory
    else:
        return model.shootouts_size(data_structs), diff_time, 0.0


# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    pass


def req_1(control,numero,nombre,condicion):
    """
    Retorna el resultado del requerimiento 1
    """
    
    start_time= get_time()
    x=model.req_1(control,numero,nombre,condicion)
    end_time= get_time() 
    delta_time1=delta_time(start_time,end_time)
    return x,delta_time1


def req_2(control,numero_de_goles,nombre):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    
    start_time= get_time()
    x=model.req_2(control,numero_de_goles,nombre)
    end_time= get_time() 
    delta_time1=delta_time(start_time,end_time) 
    return x,delta_time1


def req_3(control,equipo,fecha_i,fecha_f):
    """
    Retorna el resultado del requerimiento 3
    """
    
    start_time= get_time()
    x=model.req_3(control,equipo,fecha_i,fecha_f)
    end_time= get_time() 
    delta_time1=delta_time(start_time,end_time)
    return x,delta_time1


def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion
def printLoadDataAnswer(tiempo, memoria, bool): 
    """ 
    Imprime los datos de tiempo y memoria de la carga de datos 
    """ 
    if bool == True and memoria != 0.0: 
        print("Tiempo [ms]: ", round(tiempo,2), "||", 
        "Memoria [kB]: ", round(memoria,2)) 
    else: 
        print("Tiempo [ms]: ",round(tiempo,2))
def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
