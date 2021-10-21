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
import time
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def printArtisbyBeginDate(list):

    print('La cantidad de artistas dentro del rango es de ' + str(list[0]))
    print('\nLos 3 primeros artistas son: ')
    for i in range(1,len(list)):
        a=list[i]["value"]

        print('Nombre: '+ a['DisplayName'] ,'Año de Nacimiento: '+ a['BeginDate'],
        'Genero: '+ a['Gender'], 'Nacionalidad: '+ a['Nationality'])

        if i == 3:
            print('\nLos 3 ultimos artistas son: ')

def print_3(gd):
    tamaño=lt.size(gd)
    print("Número total de obras: " + str(tamaño))
    purchase= controller.purchase(gd)
    print("Obras compradas: " + str(purchase))
    print("Primeras 3 obras: ")
    print("ObjectID: " + str(gd["elements"][0]["ObjectID"]) + ", Título: " + str(gd["elements"][0]['Title'])
    + ", Fecha: " + str(gd["elements"][0]['DateAcquired'])
    + ", Medio: " +str(gd["elements"][0]['Medium']) + ", Dimensiones: " + str(gd["elements"][0]['Dimensions']))

    print("\nObjectID: " + str(gd["elements"][1]["ObjectID"]) + ", Título: " + str(gd["elements"][1]['Title'])
    + ", Fecha: " + str(gd["elements"][1]['DateAcquired'])
    + ", Medio: " +str(gd["elements"][1]['Medium']) + ", Dimensiones: " + str(gd["elements"][1]['Dimensions']))

    print("\nObjectID: " + str(gd["elements"][2]["ObjectID"]) + ", Título: " + str(gd["elements"][2]['Title'])
    + ", Fecha: " + str(gd["elements"][2]['DateAcquired'])
    + ", Medio: " +str(gd["elements"][2]['Medium']) + ", Dimensiones: " + str(gd["elements"][2]['Dimensions']))

    print("\nÚltimas 3 obras: ")

    print("\nObjectID: " + str(gd["elements"][tamaño-3]["ObjectID"]) + ", Título: " + str(gd["elements"][tamaño-3]['Title'])
    + ", Fecha: " + str(gd["elements"][tamaño-3]['DateAcquired'])
    + ", Medio: " +str(gd["elements"][tamaño-3]['Medium']) + ", Dimensiones: " + str(gd["elements"][tamaño-3]['Dimensions']))

    print("\nObjectID: " + str(gd["elements"][tamaño-2]["ObjectID"]) + ", Título: " + str(gd["elements"][tamaño-2]['Title'])
    + ", Fecha: " + str(gd["elements"][tamaño-2]['DateAcquired'])
    + ", Medio: " +str(gd["elements"][tamaño-2]['Medium']) + ", Dimensiones: " + str(gd["elements"][tamaño-2]['Dimensions']))

    print("\nObjectID: " + str(gd["elements"][tamaño-1]["ObjectID"]) + ", Título: " + str(gd["elements"][tamaño-1]['Title'])
    + ", Fecha: " + str(gd["elements"][tamaño-1]['DateAcquired'])
    + ", Medio: " +str(gd["elements"][tamaño-1]['Medium']) + ", Dimensiones: " + str(gd["elements"][tamaño-1]['Dimensions']))

def print_5(result):
    nationality=result[1]["elements"]
    i=0
    while i<10:
        print(nationality[i])
        i+=1

def printArtDepa(list):

    print('\nEl departamento tiene un total de ',lt.size(list[0]), 'obras')

    print('El costo por el servicio de transporte es de ',round(list[1]), 'USD')

    print('Todas las obras tienen un peso estimado de' , round(list[2]), 'kg')
    print('\n5 obras mas antiguas a transportar:')
    for i in range(1,6):
#'|Artista: '+a['Artist'],
        a=lt.getElement(list[0],i)
        print('\nTitulo: '+ a['Title'],  '|Clasificacion: '+ a['Classification'], '|Fecha: '+ a['Date'],
         '|Medio: '+ a['Medium'], '|Dimensiones: '+ a['Dimensions'], '|Costo Transporte: '+ a['Cost'])
    print('\n5 obras mas costosas a transportar:')
    for i in range(1,6):
#'|Artista: '+b['Artist'],
        b=lt.getElement(list[3],i)
        print('\nTitulo: '+ b['Title'],  '|Clasificacion: '+ b['Classification'], '|Fecha: '+ b['Date'],
         '|Medio: '+ b['Medium'], '|Dimensiones: '+ b['Dimensions'], '|Costo Transporte: '+ b['Cost'])

"""def print_6(dep):
    print("Total de obras a trasportar: " + str(dep[0]))
    print("Precio del Servicio: " + str(dep[1]))
    print("Peso total de las obras: "+ str(dep[2])+ " kg")
    i=0
    while i < 5:
        print("Titulo: " + str(dep[0][0][i]))"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas")
    
    print("3- Listar cronológicamente las adquisiciones ")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Costos transportar obras de un departamento")
    print("7- Proponer una nueva exposición en el museo")
    print("8- Salir")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog=controller.initCatalog()
        controller.loadData(catalog)

        print("\nArtistas cargadas: " + str(lt.size(catalog["Artists"])))
        print("\nObras cargadas: " + str(lt.size(catalog["Artworks"])))

        #print(mp.get(catalog['BeginDate'],'1920'))
        #sssssssssprint((lt.getElement(catalog['Artworks'],3)['ConstituentID']).replace('[','').replace(']','').split(','))
        #print(type(mp.get(catalog['Work_Nationality'],'American')['value']))
        
    elif int(inputs[0]) == 2:
        print("Digite el rango de fechas en el que desea realizar la búsqueda (AAAA)")
        min = int(input("Fecha Inicial: "))
        max = int(input("Fecha Final: "))

        list=controller.ArtistbyBeginDate(catalog,min,max)
        printArtisbyBeginDate(list)


    elif int(inputs[0]) == 0:

        Name=input("El nombre del medio:  ")
        n=input("Numero de obras:  ")
        
        list=controller.ArtworksbyMedium(catalog,Name,n)
      
        for i in list['elements']:
            print('Title: '+ i['Title'] +' / ' ,'ConstituentID: '+ i['ConstituentID'] +' / ',
                    'Date: '+ i['Date'] +' / ', 'Medium - tecnica: '+ i['Medium'])

    
    elif int(inputs[0]) == 3:
        

        min=int(input("Ingrese la Fecha Inicial: ").replace("-",""))
        max=int(input("Ingrese la Fehca final: ").replace("-",""))

        start= time.process_time()
        adq=controller.getAdquisiciones(catalog, min, max)
        print_3(adq)

        stop=time.process_time()

        print("Tiempo"+ str(stop-start))

    elif int(inputs[0]) == 5:
        start= time.process_time()
        result=controller.getbyNationality(catalog)

        print_5(result)
        stop=time.process_time()
        print("Tiempo"+ str(stop-start))

    elif int(inputs[0]) == 6:
        start= time.process_time()
        depa=input('Digite el nombre del departamento que desea costear: ')
        list=controller.TransportCos(catalog,depa)
        printArtDepa(list)
        stop=time.process_time()
        print("Tiempo"+ str(stop-start))
    else:
        sys.exit(0)
sys.exit(0)
