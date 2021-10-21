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
import time
from DISClib.ADT import map as mp

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas")
    print("3- Listar cronológicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Transportarcobras de un departamento ")
    print("7- Proponer una nueva exposición en el museo")
    print("8- Listar las obras más antiguas para un medio especifico")
    print("9- Contar en numero total de obras por nacionalidad")
    print("0- Salir")

catalog = None

def initCatalog(TipoEstructura):
    """
    Inicializa el catalogo o
    """
    return controller.initCatalog(TipoEstructura)


def loadData(catalog):

    controller.loadData(catalog)
"""
Menu principal
"""
TipoEstructura= "SINGLE_LINKED"
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        input1 = input('Seleccione una opción para continuar\n'+
                        'Presione 1 para cargar la lista como un Array List\n' +
                         'Presione 2 para cargar la lista como un Linked List\n')
        if int(input1) == 1:
            #Cargar como Array List
            TipoEstructura = 'ARRAY_LIST'
            print("Se ha configurado como Array List")
            
        elif int(input1) == 2:
            #Cargar como Linked List
            TipoEstructura = 'SINGLE_LINKED'
            print("Se ha configurado como Linked List")
                
        print("Cargando información de los archivos ....")
        catalog = initCatalog(TipoEstructura)
        loadData(catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['Artist'])))
        print('Obras cargados: ' + str(lt.size(catalog['Art'])))
        #print('Ultimos 3 artistas: ') #+ str(lt.size(catalog[''])))
        #print('Ultimas 3 obras ' ) #str(lt.size(catalog[''])))
    
    elif int(inputs[0]) == 2:
        print("Ingrese año inicial: ")
        inicial= int(input())
        print("Ingrese año final: ")
        final= int(input())
        
        start_time= time.process_time()
        
        lista_respuesta1= controller.get_req1(catalog['Artist-hash'], inicial, final)
        conteo= lt.getElement(lista_respuesta1, 1)
        print ("La cantidad de artistas en dicho rango son: " + str(conteo))
        lista_artistas= lt.getElement(lista_respuesta1, 2)
        contador= 1
        print ("\nLos tres primeros artistas son: \n")
        for artista in range(1, lt.size(lista_artistas)):
            if contador<4:
                llave=lt.getElement(lista_artistas, artista)
                i=(mp.get(catalog['Artist-hash'], llave))
                print(i['value']['DisplayName'] + ", ",i['value']['BeginDate'] + "-",i['value']['EndDate'] + ", ", i['value']['Nationality'] + ", ", i['value']['Gender'])
            contador=contador+1
        contador_2= 1
        print ("\nLos tres últimos artistas son: \n")
        for artista in range(1, lt.size(lista_artistas)):       
            if contador_2>lt.size(lista_artistas)-4:
                llave=lt.getElement(lista_artistas, artista)
                i=(mp.get(catalog['Artist-hash'], llave))
                print(i['value']['DisplayName'] + ", ",i['value']['BeginDate'] + "-",i['value']['EndDate'] + ", ", i['value']['Nationality'] + ", ", i['value']['Gender'])
            contador_2=contador_2+1
        
        stop_time= time.process_time()
        elapsed_time_mseg= (stop_time-start_time)*1000
        print("\nEl programa se demoro " + str(elapsed_time_mseg) + " mseg en ordenar los datos.\n")

    elif int(inputs[0]) == 4:
        print("Ingrese nombre del artista: ")
        nombre_artista= str(input())

        start_time= time.process_time()

        lista_respuesta= controller.get_req3(catalog, nombre_artista)
        
    
    elif int(inputs[0]) == 8:
        print("Ingrese el numero de obras que quiere conocer: ")
        num = int(input())
        print("Ingrese el medio especifico: ")
        medio = input()
        lista = controller.obras_porMedio(catalog, num, medio)
        print(lista)

    elif int(inputs[0]) == 9:
        print("Ingrese la nacionalidad")
        nac = input()
        num = controller.obrasPorNacionalidad(catalog, nac)
        print('Hay ' + num + ' obras de la nacionalidad ' + nac)
       

    else:
        sys.exit(0)
sys.exit(0)
