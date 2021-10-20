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
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as mg
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
        a=list[i]

        print('Nombre: '+ a['DisplayName']+' | ' ,'Año de Nacimiento: '+ a['BeginDate']+' | ',
        'Genero: '+ a['Gender']+' | ', 'Nacionalidad: '+ a['Nationality'])

        if i == 3:
            print('\nLos 3 ultimos artistas son: ')



def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    #print("0- Numero de obras mas antiguas por medio")
    #print('3- Numero de obras por nacionalidad ')
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

        #mg.sort(mp.get(catalog['BeginDate'],'1920'['value']),controller.)
        print(mp.get(catalog['BeginDate'],'1984'))
        #sssssssssprint((lt.getElement(catalog['Artworks'],3)['ConstituentID']).replace('[','').replace(']','').split(','))
        #print(type(mp.get(catalog['Work_Nationality'],'American')['value']))
        
    elif int(inputs[0]) == 2:
        print("Digite el rango de fechas en el que desea realizar la búsqueda (AAAA)")
        min = int(input("Fecha Inicial: "))
        max = int(input("Fecha Final: "))

        list=controller.ArtistbyBeginDate(catalog,min,max)
        printArtisbyBeginDate(list)

    elif int(inputs[0]) == 4:
        input


    elif int(inputs[0]) == 0:

        Name=input("El nombre del medio:  ")
        n=input("Numero de obras:  ")
        
        list=controller.ArtworksbyMedium(catalog,Name,n)
      
        for i in list['elements']:
            print('Title: '+ i['Title'] +' / ' ,'ConstituentID: '+ i['ConstituentID'] +' / ',
                    'Date: '+ i['Date'] +' / ', 'Medium - tecnica: '+ i['Medium'])

    elif int(inputs[0]) == 3:

        Nation=input("Ingrese la nacionalidad:  ")
        
        rta=controller.ArtworksbyNationality(catalog,Nation)
        print('De la nacionalidad '+ Nation+ ' hay '+ str(rta) + ' obras')

    else:
        sys.exit(0)
sys.exit(0)
