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
    print("2- Listar cronológicamente los artistas")
    print("3- Listar cronológicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Transportarcobras de un departamento ")
    print("7- Proponer una nueva exposición en el museo")
    print("0- Salir")

catalog = None

def initCatalog():
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
        catalog = initCatalog()
        loadData(catalog)
        print('Artistas cargados: ' + str(lt.size(catalog['Artist'])))
        print('Obras cargados: ' + str(lt.size(catalog['Art'])))
        print('Ultimos 3 artistas: ') #+ str(lt.size(catalog[''])))
        print('Ultimas 3 obras ' ) #str(lt.size(catalog[''])))
    elif int(inputs[0]) == 3:
        input1 = int(input('Ingrese la fecha inicial '))
        input2 = int(input('Ingrese la fecha final '))
        Resultado = (controller.Req2(catalog, input1, input2))
        #print('La lista organizada es: ')
        #print(Resultado[0])
        print('El numero total de obras en el rango es: ')
        print(Resultado[1])
        print('El total de obras en el rango adquiridas por compra es: ')
        print(Resultado[2])
        print('Las primeras 3 obras en orden cronologico')
        print((Resultado[3])[0])
        print((Resultado[3])[1])
        print((Resultado[3])[2])
        print('Las ultima obra en orden cronologico')
        print(Resultado[4])

    elif int(inputs[0]) == 5:
        lista = controller.Req4(catalog)
        print('Los 10 nacionalidades con más obras son: ')
        print(lista['first']['info'])
        print(lista['first']['next']['info'])
        print(lista['first']['next']['next']['info'])
        print(lista['first']['next']['next']['next']['info'])
        print(lista['first']['next']['next']['next']['next']['info'])
        print(lista['first']['next']['next']['next']['next']['next']['info'])
        print(lista['first']['next']['next']['next']['next']['next']['next']['info'])
        print(lista['first']['next']['next']['next']['next']['next']['next']['next']['info'])
        print(lista['first']['next']['next']['next']['next']['next']['next']['next']['next']['info'])
        print(lista['first']['next']['next']['next']['next']['next']['next']['next']['next']['next']['info'])

    elif int(inputs[0]) == 2:
        print("Ingrese año inicial: ")
        inicial= int(input())
        print("Ingrese año final: ")
        final= int(input())
        print ("La cantidad de artistas en dicho rango son: " + str(controller.conteo_artistas(catalog['Artist'], inicial, final)))
        print ("\nLos tres primeros artistas son: \n")
        primeros= controller.primeros_tres(catalog['Artist'], inicial, final)
        for i in lt.iterator(primeros):
            print(i['DisplayName'],i['BeginDate'], i['Nationality'], i['Gender'])
        print ("\nLos tres últimos artistas son: \n")
        ultimos= controller.ultimos_tres(catalog['Artist'], inicial, final)
        for i in lt.iterator(ultimos):
            print(i['DisplayName'],i['BeginDate'], i['Nationality'], i['Gender'])
    
    elif int(inputs[0]) == 4:
        print("Ingrese nombre del artista: ")
        nombre_artista= str(input())
        lista_respuesta= controller.get_obras(catalog, nombre_artista)
        print("El total de obras de " + nombre_artista + " es: " + str(lt.getElement(lista_respuesta, 1)))
        print("El total de técnicas utilizadas por " + nombre_artista + " fue: " + str(lt.getElement(lista_respuesta, 2)))
        print("La técnica más utilizada por " + nombre_artista + " fue: " + str(lt.getElement(lista_respuesta, 3)))
        lista_obras= lt.getElement(lista_respuesta, 4)
        for obra in lt.iterator(lista_obras):
            print("------------------------------------------------")
            print("\nTítulo: " + obra['Title'])
            print("\nAño de la obra: " + obra['Date'])
            print("\nTécnica: " + obra['Medium'])
            print("\nDimensiones: " + obra['Dimensions'])
            print("\n")

    
    elif int(inputs[0]) == 6:
        print("Ingrese nombre del departamento: ")
        nombre_departamento= str(input())
        lista_respuesta_departamento= controller.get_info_transporte(catalog['Art'], nombre_departamento)
    

    else:
        sys.exit(0)
sys.exit(0)
