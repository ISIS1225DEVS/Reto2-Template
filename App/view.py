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
    print("1- Inicializar cátalogo")
    print('2- Cargar cátalogo')
    print("3- Requerimiento 1")
    # print("4- Cargar el video con mayor cantidad de días en tendencia, según categoría")
    # print("6- Crear lista de los vídeos más vistos en un país y con categoría específica")


def initCatalog(typemap, chargeFactor):
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog(typemap, chargeFactor)

def printResults(videos, sample=3):
    size = lt.size(videos)
    if size > sample:
        print("Los primeros ", sample, " videos ordenados son: ")

def Load_Data(catalog):
    #Carga los datos del archivo
    controller.Load_Data(catalog)

catalog = None
cont = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Iniciando cátalogo...")
        Prob_or_Chain = "CHAINING"
        chargeFactor = 2.0
        cont = initCatalog(Prob_or_Chain, chargeFactor)
    elif int(inputs[0]) == 2:
        print("Cargando información...")
        answer = controller.Load_Data(cont)
        print("Cargando información de los archivos ....")
        print('Videos cargados: ' + str(controller.VideoSize(cont)))
        print('Países cargados: ' + str(controller.CountrySize(cont)))
        print('Etiquetas cargadas: ' + str(controller.TagSize(cont)))
        print('Categorías cargadas: ' + str(controller.CategoriesSize(cont)))
        # print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
        #       "Memoria [kB]: ", f"{answer[1]:.3f}")

    elif int(inputs[0]) == 3:
        category_name = input("Introduzca el nombre de la categoría deseada:\n")
        country = input("Introduzca el nombre del país deseado:\n")
        n_videos = int(input("Introduzca el número de videos en lista que desea ver:\n"))
        imprime = controller.n_videostrending(cont, category_name, country, n_videos)
        print(imprime)

    else:
        sys.exit(0)
sys.exit(0)
