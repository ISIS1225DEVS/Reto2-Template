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
from datetime import datetime
import time
assert cf
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from prettytable import PrettyTable
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
    print("7-LAB 5-“las n obras más antiguas para un medio específico ")
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
        print('Artistas cargados: ' + str(mp.size(catalog['artistas']["mID"])))
        print("Medios utilizados " + str(mp.size(catalog["obras"]["mMedio"])))
        print("Nacionalidades obras " + str(mp.size(catalog["obras"]["mNacionalidad"])))
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
            
        stop_time = time.process_time()
        timepaso= stop_time-start_time
        print("Tiempo transcurrido "+ str(timepaso))
        
    elif int(inputs[0]) == 4:
        start_time = time.process_time()
        nombre= input("Indique el nombre del artista: ")
        (Tecnicas, tecnicaRep, numeroObrasGeneral,listaObrasTecnica )= controller.ObrasPorArtistaPorTecnica(catalog,nombre)
        print(str(nombre)+ " tiene un total de: "+ str(mp.size(Tecnicas))+" tecnicas y "+ str(numeroObrasGeneral)+ " obras.")
        print("La tecnica más utilizada es: "+ str(tecnicaRep) +" con "+ str(lt.size(listaObrasTecnica))+ " obras.")
        if lt.size(listaObrasTecnica) <= 3:
            print("Hay 3 o menos obras en esta técnica, estas son:")
            x = PrettyTable() 
            x.field_names = ["Titulo", "Fecha de la Obra", "Medio", "Dimensiones"]
            for i in lt.iterator(listaObrasTecnica):
                x.add_row([str(i["Title"]),str(i["Date"]),str(i["Medium"]),str(i["Dimensions"])])
            print(x)
        elif lt.size(listaObrasTecnica) > 3:
            primeras= lt.subList(listaObrasTecnica,1,3)
            a = PrettyTable() 
            a.field_names = ["Titulo", "Fecha de la Obra", "Medio", "Dimensiones"]
            for i in lt.iterator(primeras):
                a.add_row([str(i["Title"]),str(i["Date"]),str(i["Medium"]),str(i["Dimensions"])])
            ultimas= lt.subList(listaObrasTecnica,lt.size(listaObrasTecnica)-3,3)
            b = PrettyTable() 
            b.field_names = ["Titulo", "Fecha de la Obra", "Medio", "Dimensiones"]
            for i in lt.iterator(primeras):
                b.add_row([str(i["Title"]),str(i["Date"]),str(i["Medium"]),str(i["Dimensions"])])
            print("Las primeras 3  obras en esta técnica son:")  
            print(a)
            print("Las ultimas 3  obras en esta técnica son:") 
            print(b)
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
        listaporfecha= controller.sortArtworksByDate(listaObrasdeDepto)
        stop_time = time.process_time()
        timepaso= stop_time-start_time
        print("Tiempo transcurrido "+ str(timepaso))
    elif int(inputs[0]) == 7:
        start_time = time.process_time()
        nombre= input("Indique el nombre del medio: ")
        n= int(input("Indique el número de obras: "))
        obras_medio= controller.ObrasAntiguasMedio(catalog,nombre,n)
        print(str(obras_medio))
    elif int(inputs[0]) >= 8 :
        print ("Lo sentimos, Requerimiento no disponible")
        pass
    else:
        sys.exit(0)
sys.exit(0)
