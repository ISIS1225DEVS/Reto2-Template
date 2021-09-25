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
from datetime import datetime
from DISClib.ADT import list as lt
from datetime import datetime
import time
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
    print("\nBienvenido")
    print("1-Cargar información en el catálogo, y escoger el tipo de estructura")
    print("2-Listar cronológicamente los artistas")
    print("3-Listar cronológicamente las adquisiciones ")
    print("4-Clasificar las obras de un artista por técnica")
    print("5-Clasificar las obras por la nacionalidad de sus creadores ")
    print("6-Transportar obras de un departamento ")
    print("0-Salir ")
 
def initCatalog():
    """
    Inicializa el catalogo de libros
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    return controller.loadData(catalog)

#Funciones para imprimir#
def printartists(artistas, incluirObras):
    size = lt.size(artistas)
    if size:
        for artista in lt.iterator(artistas):
            print("--------------")
            print(' Nombre: ' +artista["DisplayName"] + ' Fecha de inicio: '+ 
                    artista["BeginDate"]+' Fecha fin: '+ artista["EndDate"]+
                  ' Nacionalidad: '+ artista["Nationality"]+ ' Género: '+artista["Gender"])
            if incluirObras:
                obras=artista["Artworks"]
                if lt.isEmpty(obras)==False:
                    print("    Obras del artista:")
                    printobras(obras,False)
                else:
                    print("No")
    else:
        print('No se han cargado artistas')

def printobras(obras,incluir):
    size = lt.size(obras)
    if size:
        for obra in lt.iterator(obras):
            print("--------------")
            print( ' Título: ' + obra["Title"] + ' Fecha Adquisión: ' + obra["DateAcquired"] +
            " Fecha de la obra: "+ obra["Date"]+ " Clasificación: " + obra["Classification"]+
             ' Medio: ' + obra["Medium"] + ' Dimensiones: ' + obra["Dimensions"])
            if incluir:
                artistas=obra["Artists"]
                if lt.isEmpty(artistas)==False:
                    print(" Artista(s) de la Obra:")
                    printartists(artistas,False)
                else:
                    print("No")
    else:
        print('No se han cargado obras')
def printPrimerosyUltimosartistas(listaEnRango):
    if lt.size(listaEnRango)>3:
            primeros= lt.subList(listaEnRango,1,3)
            ultimos= lt.subList(listaEnRango,lt.size(listaEnRango)-2,3)
            print("\n* Primeros 3 artisas")
            printartists(primeros,True)
            print("\n* Utlimos 3 artisas")
            printartists(ultimos,False)
    elif lt.size(listaEnRango)<=3:
            print("Como solo hay 3 o menos artistas, estos son:")
            printartists(listaEnRango,False)
def printPrimerosyUltimosobras(lista):
    if lt.size(lista)>3:
            primeros= lt.subList(lista,1,3)
            ultimos= lt.subList(lista,lt.size(lista)-2,3)
            print("\n* Primeras 3 obras ")
            printobras(primeros,True)
            print("\n* Utlimos 3 obras ")
            printobras(ultimos,True)
    elif lt.size(lista)<=3:
            print("Como solo hay 3 o menos obras, estas son:")
            printobras(lista,True)
def print5obrasMasAntiguas(lista):
    if lt.size(lista)>5:
            print("Las 5 obras mas caras a transportar")
            obras= lt.subList(lista,1,5)
            count=1
            for obra in lt.iterator(obras):
                print(str(count))
                print("--------------")
                print( ' Título: ' + obra["Title"] + " Fecha de la obra: "+ obra["Date"]+ 
                " Clasificación: " + obra["Classification"]+ ' Medio: ' + obra["Medium"] + 
                ' Dimensiones: ' + obra["Dimensions"]+' Costo asociado al transporte: ' + str(obra["precio"]))
                artistas=obra["Artists"]
                if lt.isEmpty(artistas)==False:
                        print(" Artista(s) de la Obra:")
                        for artista in lt.iterator(obra["Artists"]):
                            print("       -"+str(artista["DisplayName"]))
                count+=1
    elif lt.size(lista)<=5:
            print("Como solo hay 5 o menos obras, estos son:")
            printobras(lista,True)
def print5obrasMasCaras(lista):
    if lt.size(lista)>5:
            print("Las 5 obras mas caras a transportar")
            obras= lt.subList(lista,lt.size(lista)-4,5)
            count= 5
            for obra in lt.iterator(obras):
                print(str(count))
                print("--------------")
                print( ' Título: ' + obra["Title"] + " Fecha de la obra: "+ obra["Date"]+ 
                " Clasificación: " + obra["Classification"]+ ' Medio: ' + obra["Medium"] + 
                ' Dimensiones: ' + obra["Dimensions"]+' Costo asociado al transporte: ' + str(obra["precio"]))
                artistas=obra["Artists"]
                if lt.isEmpty(artistas)==False:
                        print(" Artista(s) de la Obra:")
                        for artista in lt.iterator(obra["Artists"]):
                            print("       -"+str(artista["DisplayName"]))
                count-=1
    elif lt.size(lista)<=5:
            print("Como solo hay 5 o menos obras")
"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        start_time = time.process_time()
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Obras cargadas: ' + str(lt.size(catalog['obras'])))
        print('Artistas cargados: ' + str(lt.size(catalog['artistas'])))
        stop_time = time.process_time()
        timepaso= stop_time-start_time
        print("Tiempo transcurrido "+ str(timepaso))

    elif int(inputs[0]) == 2:
        start_time = time.process_time()
        date1 = input("Indique año inicial (formato YYYY): ")
        date2 = input("Indique año final (formato YYYY): ")
        listaEnRango= controller.sortArtistInDateRange(catalog,date1,date2)
        if lt.isEmpty(listaEnRango):
            print("No hay artistas nacidos en el rango")
        else:
            print("Hay "+ str(lt.size(listaEnRango))+ " artistas que nacieron entre "+ str(date1) +" y "+ str(date2))
            printPrimerosyUltimosartistas(listaEnRango)
        stop_time = time.process_time()
        timepaso= stop_time-start_time
        print("Tiempo transcurrido "+ str(timepaso))

    elif int(inputs[0]) == 3:
        start_time = time.process_time()
        inicial= input("Indique la fecha inicial: ")
        final= input("Indique la fecha final: ")
        (lista,numPurchased) = (controller.sortArtworksandRange(catalog["obras"],inicial,final))
        if lt.isEmpty(lista):
            print("No hay obras en el rango")
        else:
            print("Hay "+ str(lt.size(lista))+ " obras  entre "+ str(inicial) +" y "+ str(final))
            print("Hay "+ str(numPurchased)+ " obras adquiridas por compra")
            printPrimerosyUltimosobras(lista)
            
        stop_time = time.process_time()
        timepaso= stop_time-start_time
        print("Tiempo transcurrido "+ str(timepaso))
        
    elif int(inputs[0]) == 4:
        start_time = time.process_time()
        nombre= input("Indique el nombre del artista: ")
        (obrasArtista, Tecnicas)= controller.ObrasPorArtistaPorTecnica(catalog,nombre)
        if Tecnicas != None and obrasArtista!= None:
            Tecnica= controller.buscarTecnicaMasRep(Tecnicas)
            print(str(nombre)+ " tiene un total de: "+ str(lt.size(obrasArtista))+" obras.")
            print("La tecnica más utilizada es: "+ str(Tecnicas[Tecnica]["nombre"])+". Con "+str(lt.size(Tecnicas[Tecnica]["obras"]))+" obras.")
            print("El listado de obras es: ")
            printobras((Tecnicas[Tecnica]["obras"]),False)
        else:
            print("Entrada invalida")
        stop_time = time.process_time()
        timepaso= stop_time-start_time
        print("Tiempo transcurrido "+ str(timepaso))
    elif int(inputs[0])==5:
        start_time = time.process_time()
        obras=catalog["obras"]
        nacionalidades=controller.RankingCountriesByArtworks(catalog,obras)
        print("El top 10 de los países en el MoMa son: ")
        num=0
        #for i in nacionalidades:
            #print(str(i)+ ":"+ str(nacionalidades[i]))
            #num+=1
            #if num==10:
                #break
        print (nacionalidades)
        stop_time = time.process_time()
        timepaso= stop_time-start_time
        print("Tiempo transcurrido "+ str(timepaso))
    elif int(inputs[0])==6:
        start_time = time.process_time()
        departamento= input("Por favor ingrese el nombre del departamento:") 
        respuesta= controller.OrdenarDepartamentoAsignarPrecioyPeso(catalog,departamento)
        peso_total= lt.getElement(respuesta,1)
        precio_total=lt.getElement(respuesta,2)
        listaObrasdeDepto=lt.getElement(respuesta,3)
        print("El total de obras en el departamento "+ str(departamento)+ "es de: "+ str(lt.size(listaObrasdeDepto)))
        print ("El estimado en USD del precio de servicio es de "+str(precio_total))
        print("El peso estimado de las obras es de "+ str(peso_total))
        listaporprecio= controller.sortArtworksByPrice(listaObrasdeDepto)
        print5obrasMasCaras(listaporprecio)
        listaporfecha= controller.sortArtworksByDate(listaObrasdeDepto)
        print5obrasMasAntiguas(listaporfecha)
        stop_time = time.process_time()
        timepaso= stop_time-start_time
        print("Tiempo transcurrido "+ str(timepaso))
    elif int(inputs[0]) >= 6 :
        print ("Lo sentimos, Requerimiento no disponible")
        pass
    else:
        sys.exit(0)
sys.exit(0)
