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


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Imprimir los n mas antiguos por medio")
    print("3- Número de obras según nacionalidad indicada")
    print("4- Listar cronológicamente los artistas")
    print("5- Listar cronológicamente las adquisiciones")
    print("6- Clasificar las obras de un artista por técnica")
    print("7- Clasificar las obras por la hnacionalidad de sus creadores")
    print("8- Transportar obras de un departamento")
    print("9- Salir del programa")

catalog = None
def initCatalog() : 
    return controller.initCatalog() 

def loadData (catalog) : 
    controller.loadData(catalog) 

def oldestArtworksbyMedium(catalog,medium,n): 
    return controller.oldestbyMedium(catalog,medium,n) 

def printcountobrasnationality(numberArtWorks):
    if numberArtWorks:
        print('Se encontraron: ' + str(lt.size(numberArtWorks)) + ' obras')
    else:
        print('No se encontraron obras')

def transportarObras(depto,catalog) : 
    return controller.transportarObras(depto,catalog)

def printTransportarObras(transporte, depto):
    if transporte[4] > 0:
        print("El MoMA va a transportar " + str(transporte[4])+" obras del departamento " + str(depto))
        if transporte[1]:
            print("El peso estimado es de: " + str(transporte[1]) +" Kg")
        if transporte[0]:
            print("El costo estimado es de: " + str(transporte[0]) + " USD")
        if transporte[2]:
            print("Las 5 obras más costosas a transportar son: ")
            print(transporte[2])
            print("ObjectID: " + transporte[2]['ObjectID'] + '\t|\t' + 'Title ' + transporte[2]['Title'] + '\t|\t' +  
            "ArtistsNames: " + transporte[2]['ArtistsNames'] + '\t|\t' + "Medium: " + transporte[2]['Medium'] + "\t|\t" + 
            "Date: " + transporte[2]['Date'] + "\t|\t" + "Dimensions: " + transporte[2]['Dimensions'] + "\t|\t" + 
            "Classification: " + transporte[2]['Classification'] + "\t|\t" + "TransCost: " + transporte[2]['TransCost'] + "\t|\t" + 
            "URL: " + transporte[2]['URL'])
        if transporte[3]:
            print("Las 5 obras más antiguas a transportar son: ")
            print(transporte[3])
            print("ObjectID: " + transporte[3]['ObjectID'] + '\t|\t' + 'Title ' + transporte[3]['Title'] + '\t|\t' +  
            "ArtistsNames: " + transporte[3]['ArtistsNames'] + '\t|\t' + "Medium: " + transporte[3]['Medium'] + "\t|\t" + 
            "Date: " + transporte[3]['Date'] + "\t|\t" + "Dimensions: " + transporte[3]['Dimensions'] + "\t|\t" + 
            "Classification: " + transporte[3]['Classification'] + "\t|\t" + "TransCost: " + transporte[3]['TransCost'] + "\t|\t" + 
            "URL: " + transporte[3]['URL'])
    else:
        print("No se encuentran obras a transportar de ese departamento")

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog() 
        loadData(catalog)
        print('Se cargaron: ' + str(lt.size(catalog['Artwork'])) + ' artworks')        

    elif int(inputs[0]) == 2:
        Medium = input('Ingrese un medio a buscar: ')
        n = int(input('Ingrese el numero de obras a consultar: '))
        oldestbymedium = oldestArtworksbyMedium(catalog,Medium,n)
        for artWork in oldestbymedium : 
            print(oldestbymedium)
    
    elif int(inputs[0]) == 3:
        nationality = input("Buscando obras de la nacionalidad: ")
        numberArtWorks = controller.countobrasnationality(nationality, catalog)
        print(printcountobrasnationality(numberArtWorks))
    
    elif int(inputs[0]) == 4: 
        anioinicial = int(input("Ingrese el año inicial: "))
        aniofinal = int(input("Ingrese el año final: ")) 
        artistas = controller.listCronoArtist(anioinicial,aniofinal,catalog) 
        i = 1 
        while i <= 3 :
            print(lt.getElement(artistas,i))
            i += 1 
        j = lt.size(artistas) 
        print('-'*50)
        while j > lt.size(artistas) - 3 : 
            print(lt.getElement(artistas,j))
            j -= 1 

    elif int(inputs[0]) == 8: 
        depto = input('Ingrese el departamento a transportar: ')
        transporte = transportarObras(depto,catalog)
        print(printTransportarObras(transporte, depto))

    else:
        sys.exit(0)
sys.exit(0)
