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
#REQ1
def printArtisbyBeginDate(list):

    print('La cantidad de artistas dentro del rango es de ' + str(list[0]))
    print('\nLos 3 primeros artistas son: ')
    for i in range(1,len(list)):
        a=list[i]

        print('Nombre: '+ a['DisplayName']+' | ' ,'Año de Nacimiento: '+ a['BeginDate']+' | ',
        'Genero: '+ a['Gender']+' | ', 'Nacionalidad: '+ a['Nationality'])

        if i == 3:
            print('\nLos 3 ultimos artistas son: ')

#REQ3
def printArtworksMediumsbyArtist(catalog,list):
    if list != 0:
        print(list[4]['DisplayName'] + ' con MOMA ID/ '+list[4]['ConstituentID']+' tiene '+str(list[0])+' obras a su nombre')
        print('\n Se usa un total de '+ str(len(list[1]))+' tecnicas diferentes')
        print('\nLas tecnicas que utiliza son: '+ str(list[1]))
        print('\nLa tecnica mas utilizada es '+ str(list[2]))

        print('\nAlgunas obras de este medio son:')
        
        if type(list[3])==type(lt.getElement(catalog['Artists'],1)):
            a=list[3]
            print('\nTitulo: '+a['Title']+' | ', 'Fecha de la obra: '+a['Date']+' | ', 'Tecnica o Medio: '+a['Medium']+' | ',
                    'Diemensiones: '+ a['Dimensions'])

        else:
            c=0
            for a in list[3]['elements']:

                print('\nTitulo: '+a['Title']+' | ', 'Fecha de la obra: '+a['Date']+' | ', 'Tecnica o Medio: '+a['Medium']+' | ',
                    'Diemensiones: '+ a['Dimensions'])
                c+=1
                if c>6:
                    break
    else:
        print('No hay obras para este artista')

    #BONO

def printprolificArtist(list):

    for a in list:

        if a[1] != 0:

            print('Nombre: '+ a[0]['DisplayName']+' | ' ,'Año de Nacimiento: '+ a[0]['BeginDate']+' | ',
            'Genero: '+ a[0]['Gender']+' | ', 'Total de obras: '+ str(a[1][0])+' | ' , 'Total técnicas utilizadas: '+ str(len(a[1][1]))+' | ', 
            'La técnica más utilizada: '+ str(a[1][2])+' | ', )
        else:
            print('Nombre: '+ a[0]['DisplayName']+' | ' ,'Año de Nacimiento: '+ a[0]['BeginDate']+' | ',
            'Genero: '+ a[0]['Gender']+' | ')






def printMenu():
    print('___________________________________________________________')
    print("\nBienvenido")
    print("1- Cargar información en el catálogo")
    #print("0- Numero de obras mas antiguas por medio")
    #print('3- Numero de obras por nacionalidad ')
    print("2- Listar cronológicamente los artistas")
    print("3- Listar cronológicamente las adquisiciones ")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Costos transportar obras de un departamento")
    print("7- Encontrar los artistas más prolíficos del museo")
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

        #x=mp.get(catalog['DisplayName'],'Louise Bourgeois')['value']['ConstituentID']
        #print(mp.get(catalog['DisplayName'],'Louise Bourgeois'))
        
          
    elif int(inputs[0]) == 2:
        print("Digite el rango de fechas en el que desea realizar la búsqueda (AAAA)")
        min = int(input("Fecha Inicial: "))
        max = int(input("Fecha Final: "))

        list=controller.ArtistbyBeginDate(catalog,min,max)
        printArtisbyBeginDate(list)

    elif int(inputs[0]) == 4:
        Name=input("Ingrese el nombre del artista:  ")

        list=controller.ArtworksMediumsbyArtist(catalog,Name)
        printArtworksMediumsbyArtist(catalog,list)

    elif int(inputs[0]) == 7:
        N=int(input("Ingrese Número de artistas que desea en la clasificación:  "))
        min = int(input("Fecha Inicial: "))
        max = int(input("Fecha Final: "))

        list=controller.prolificArtist(catalog,min,max,N)
        printprolificArtist(list)



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
