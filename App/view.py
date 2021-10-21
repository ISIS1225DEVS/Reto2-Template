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

def listArtworkbyDate (fecha_inicial, fecha_final,catalog) : 
    return controller.listArtworkbyDate(fecha_inicial, fecha_final,catalog)

def printArtWork(artWork): 
    print("ObjectID: " + artWork['ObjectID'] + '\t|\t' + 'Title ' + artWork['Title'] + '\t|\t'  + 
    "Medium: " + artWork['Medium'] + "\t|\t" + "Dimensions: " + artWork['Dimensions'] + "\t|\t" + "Date: " + artwork['Date'] + "\t|\t" +
    'DateAcquired: ' + artWork['DateAcquired'] + "\t|\t" + "URL: " + artWork['URL'])

def printArtworksbyNationality(artwork):
    print('Nationality: ' + artwork['Nationality'] + '\t|\t' + 'Artworks: ' + str(lt.size(artwork['Artworks'])) + '\t|\t')

def transportarObras(depto,catalog) : 
    return controller.transportarObras(depto,catalog)

def printTransportarObras(transporte, depto):
    
    if transporte[4] > 0:
        print("El MoMA va a transportar " + str(transporte[4])+" obras del departamento " + str(depto))
        print("El tiempo de ejecución del requerimiento 5 es de: " + str(transporte[5]))
        if transporte[1]:
            print("El peso estimado es de: " + str(transporte[1]) +" Kg")
        if transporte[0]:
            print("El costo estimado es de: " + str(transporte[0]) + " USD")
        if transporte[2]:
            print("\n" +"Las 5 obras más costosas a transportar son: \n")
            if lt.size(transporte[2])>0:
                for i in range(0,5):
                    obra = lt.getElement(transporte[2],i) 
                    print("ObjectID: " + str(obra['ObjectID']) + '\t|\t' + 'Title ' + obra['Title'] + '\t|\t' +  
                     "ArtistsNames: " + obra['ArtistsNames'] + '\t|\t' + "Medium: " + obra['Medium'] + "\t|\t" + 
                    "Date: " + str(obra['Date']) + "\t|\t" + "Dimensions: " + obra['Dimensions'] + "\t|\t" + 
                    "Classification: " + obra['Classification'] + "\t|\t" + "TransCost: " + str(obra['TransCost']) + "\t|\t" + 
                    "URL: " + obra['URL'])
        if transporte[3]:
            print("\n" +"Las 5 obras más antiguas a transportar son: \n")
            if lt.size(transporte[3])>0:
                for i in range(0,5):
                    artwork = lt.getElement(transporte[3],i) 
                    print("ObjectID: " + str(artwork['ObjectID']) + '\t|\t' + 'Title ' + artwork['Title'] + '\t|\t' + "ArtistsNames: " + obra['ArtistsNames'] + '\t|\t' +
                    "Medium: " + artwork['Medium'] + "\t|\t" + "Date: " + str(artwork['Date']) + "\t|\t" + "Dimensions: " + artwork['Dimensions'] + "\t|\t" + 
                    "Classification: " + artwork['Classification'] + "\t|\t" + "TransCost: " + str(artwork['TransCost']) + "\t|\t" + "URL: " + artwork['URL'])
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
        print("El tiempo de ejecución del requerimiento 1 es de: " + str(artistas[1]))
        i = 1 
        while i <= 3 :
            print(lt.getElement(artistas[0],i))
            i += 1 
        j = lt.size(artistas[0]) 
        print('-'*50)
        while j > lt.size(artistas[0]) - 3 : 
            print(lt.getElement(artistas[0],j))
            j -= 1 
        

    elif int(inputs[0]) == 5: 
        fecha_inicial = input("Fecha inicial(AAAA-MM-DD): ")
        fecha_final = input("Fecha final(AAAA-MM-DD): ")
        result = listArtworkbyDate(fecha_inicial,fecha_final,catalog)
        print("El numero total de obras entre " + str(fecha_inicial) + " y " + str(fecha_final) + " es: " + str(lt.size(result[0][0]))) 
        print("El numero de obras adquiridas por compra es: " + str(result[1]))
        print("El tiempo de ejecución del requerimiento 2 es de: " + str(result[0][1]))
        if lt.size(result[0][0])>0:
            print("\n" +"Las primeras 3 obras son: \n")
            for i in range(1,4):
                artwork = lt.getElement(result[0][0],i) 
                printArtWork(artwork)
            print("\n" +'Las ultimas 3 obras en el rango son: \n')
            for i in range(lt.size(result[0][0])-2,lt.size(result[0][0])+1): 
                artwork = lt.getElement(result[0][0],i) 
                printArtWork(artwork) 
        else:
            print("No se encontraron obras de " + str(fecha_final) + " a " + str(fecha_final))

    elif int(inputs[0]) == 7:
        obras = controller.Artworksbynationality(catalog)
        print("Los 10 paises con el mayor número de obras: ")
        for i in range(lt.size(obras)-9,lt.size(obras)+1):
            artwork = lt.getElement(obras,i)
            printArtworksbyNationality(artwork)
        topnationality = lt.getElement(obras,lt.size(obras))
        sizetopnationality = lt.size(topnationality['Artworks'])
        print("La nacionalidad con mayor número de obras fue: " + topnationality['Nationality'] + " con " + str(sizetopnationality) + " obras")
        print("Las 3 primeras y últimas obras de " + topnationality['Nationality'] + " fueron: ")
        if sizetopnationality>0:
            for i in range(1,4):
                artwork = lt.getElement(obras,i) 
                printArtWork(artwork)
            for j in range(lt.size(obras)-2,lt.size(obras)+1): 
                artwork = lt.getElement(obras,j) 
                printArtWork(artwork) 
        else:
            print("No se encontraron obras de " + str(fecha_final) + " a " + str(fecha_final))
        
        

    elif int(inputs[0]) == 8: 
        depto = input('Ingrese el departamento a transportar: ')
        transporte = transportarObras(depto,catalog)
        print(printTransportarObras(transporte, depto))

    else:
        sys.exit(0)
sys.exit(0)
