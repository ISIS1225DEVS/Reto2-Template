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
import time
import tracemalloc
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
    #Inicia el catálogo de videos en Array
def initCatalog(typemap, chargeFactor):
    catalog = model.newCatalog(typemap, chargeFactor)
    # print(typemap, "En el controller")
    # print(chargeFactor, "En el controller")
    return catalog
    #Inicia el catálogod de videos en Linked list
# def initCatalogLinked():
#     catalog = model.newCatalog_Linked()
#     return catalog
# # Funciones para la carga de datos
def Load_Data(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    # delta_time = -1.0
    # delta_memory = -1.0

    # tracemalloc.start()
    # start_time = getTime()
    # start_memory = getMemory()

    LoadVideos(catalog)
    LoadCategory(catalog)

    # stop_memory = getMemory()
    # stop_time = getTime()
    # tracemalloc.stop()

    # delta_time = stop_time - start_time
    # delta_memory = deltaMemory(start_memory, stop_memory)
    # return delta_time, delta_memory
def LoadVideos(catalog):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    videosfile = cf.data_dir + 'videos-supersmall.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for videos in input_file:
        model.addVideo(catalog,videos)

def LoadCategory(catalog):
    categoryfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(categoryfile, encoding='utf-8'))
    for category in input_file:
        model.addCategories(catalog,category)
# Funciones de ordenamiento
def sortVideos(catalog, size, sortType):
    """
    Ordena los videos por views
    """
    return model.sortVideos(catalog, size, sortType)
def LikesbyCategory (catalog, number, category):
    model.LikesbyCategory(catalog, number, category)
# Funciones de consulta sobre el catálogo
# def getGreatestTendency(catalog, n_category):
#     return model.greatestTendency(catalog, n_category)

#Funciones para contar información del cátalogo

def VideoSize(catalog):
    return model.VideoSize(catalog)

def CountrySize(catalog):
    return model.CountrySize(catalog)

def TagSize(catalog):
    return model.TagSize(catalog)

def CategoriesSize(catalog):
    return model.CategoriesSize(catalog)

#Funciones del reto 2

def n_videostrending(catalog, category_name, country, n_videos):
    return model.n_videostrending(catalog, category_name, country, n_videos)

#Funciones para tiempo y memoria

def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
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