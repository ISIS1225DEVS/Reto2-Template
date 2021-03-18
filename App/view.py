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
assert cf

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo en una lista arreglo")
    print('2- Cuántos likes según n videos y x categoría')
    # print("4- Cargar el video con mayor cantidad de días en tendencia, según categoría")
    # print("6- Crear lista de los vídeos más vistos en un país y con categoría específica")

def initCatalog_Linked():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalogLinked()
    
def initCatalog_Array():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalogArray()

def printResults(videos, sample=3):
    size = lt.size(videos)
    if size > sample:
        print("Los primeros ", sample, " videos ordenados son: ")

def Load_Data(catalog):
    #Carga los datos del archivo
    controller.Load_Data(catalog)

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        catalog = initCatalog_Array()
        Load_Data(catalog)
        print("Cargando información de los archivos ....")
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Etiquetas cargadas: ' + str(lt.size(catalog['tagvideos'])))
        print('Categorías cargadas: ' + str(lt.size(catalog['categories'])))
        print(catalog['categories'])

    elif int(inputs[0]) == 2:
        catalog = initCatalog_Array()
        Load_Data(catalog)
        howMuch = int(input('Ingrese la cantidad de videos que desea archivar: '))
        whatCategory = str(input('Ingrese el nombre de la categoría que desea buscar: '))
        result = controller.LikesbyCategory(catalog, howMuch, whatCategory)
        print(result)
    # elif int(inputs[0]) == 4:
    #     n_category = input("¿A cuál categoría (según ID) desea consultar?")
    #     result = controller.getGreatestTendency(catalog, n_category)
    #     print("El video con mayor tendencia en la categoría ", n_category, "es ", result['title'], ", del canal ", result['channel_title'], " teniendo ", result['ammount_of_days'], " días en tendencia.")

    # elif int(inputs[0]) == 6:
    #     size = int(input("¿Cuántos vídeos desea enlistar?\n"))
    #     # country = str(input("Digite el nombre del país: \n"))
    #     # category_videos = str(input("Digite la categoría: \n"))
    #     if size > lt.size(catalog['videos']):
    #         print('La cantidad de videos a enlistar es mayor a la cantidad de videos disponibles.')
    #     else:
    #         print("1 - Selection Sort \n2 - Insertion Sort \n3 - Shell Sort \n4 - Merge Sort \n5 - Quick Sort \n")
    #         sortType = input("Seleccione el tipo de algoritmo de ordenamiento que desea usar: ")
    #         result = controller.sortVideos(catalog, int(size), sortType)
    #         # print("Usando una muestra de ", size, " elementos, el tiempo que tomó ordenar el catálogo (en milisegundos) es ", str(result[0]))
    #         print(result)


    else:
        sys.exit(0)
sys.exit(0)
