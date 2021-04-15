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
from DISClib.ADT import map as mp
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Buscar n videos con mas visitas por categoria y pais")
    print("4-")

def initCatalog():
    return controller.initCatalog()

def loadData(catalog):
    controller.loadData(catalog)

def printReq1(lista,sample):
    print("Los",sample,"videos con mas visitas son: ")
    for i in range(1,sample+1):
        video=lt.getElement(lista,i)
        print(' Fecha Trending: ' + video['trending_date'] + "," + ' Nombre: ' +
                video['title'] + ","+ ' Canal: ' + video['channel_title'] + ","+ " Fecha de Publicacion: "+ video["publish_time"] +
                "," + " Visitas: " + video["views"]+ ","+ " Likes: "+ video["likes"]+ "," + " Dislikes: " +video["dislikes"])


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog=initCatalog()
        loadData(catalog)
        print("Videos cargados: " + str(lt.size(catalog["videos"])))
        print("Categorias cargadas: " + str(mp.size(catalog["categorias"])))
    elif int(inputs[0]) == 2:
        country=input("Escriba el pais del cual quiere buscar: ")
        category=input("Escriba la categoria de la cual quiere buscar: ")
        sample=int(input("Escriba el tamaño de la lista que quiere recibir: "))
        try:
            printReq1(controller.sameCountryCategory(catalog["country"],catalog["category-id"],country,category),sample)
        except IndexError:
            print("No hay tantos videos de este pais y categoria, estos son todos los que hay")

    else:
        sys.exit(0)
sys.exit(0)
