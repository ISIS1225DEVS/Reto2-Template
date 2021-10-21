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
    
    
    elif int(inputs[0]) == 3:
        print("Ingrese la fecha inicial")
        fechai = (input())
        print("Ingrese la fecha final")
        fechaf = (input())
        r = controller.obrasPorAnio(catalog, fechai, fechaf)
        
        print('==============================================================================================================')
        print('')
        print('El total de obras en el rango dado fueron: ' + str(r[1]))
        print('')
        print('==============================================================================================================')
        print('')
        print('El total de obras en el rango obtenidas por compra fueron: ' + str(r[2]))
        print('')
        print('==============================================================================================================')
        print('')
        print('Las primeras 3 obras son')
        print('')
        print(lt.getElement(r[0], r[1]))
        print('')
        print(lt.getElement(r[0], r[1] - 1))
        print('')
        print(lt.getElement(r[0], r[1] - 2))
        print('')
        print('==============================================================================================================')
        print('')
        print('Las primeras 3 obras son')
        print('')
        print(lt.getElement(r[0], 1))
        print('')
        print(lt.getElement(r[0], 2))
        print('')
        print(lt.getElement(r[0], 3))
        
        


    elif int(inputs[0]) == 5:
        lista = controller.ObrasPorNacionalidades(catalog)
        size = lt.size(lista)
        top1 = (lt.getElement(lista, size))[0]

        llave_valor = mp.get(catalog['Nationality'], top1)
        valor = me.getValue(llave_valor)
        sizevalor = lt.size(valor)
        print('==============================================================================================================')
        print('Las TOP 10 Nacionalidades son:')
        print('==============================================================================================================')
        print(lt.getElement(lista, size))
        print(lt.getElement(lista, size-1))
        print(lt.getElement(lista, size-2))
        print(lt.getElement(lista, size-3))
        print(lt.getElement(lista, size-4))
        print(lt.getElement(lista, size-5))
        print(lt.getElement(lista, size-6))
        print(lt.getElement(lista, size-7))
        print(lt.getElement(lista, size-8))
        print(lt.getElement(lista, size-9))
        print('')
        print('==============================================================================================================')
        print('')
        print('Las primeras 3 obras son')
        print(lt.getElement(lt.getElement(valor, 1), 1))
        print('')
        print(lt.getElement(lt.getElement(valor, 2), 1))
        print('')
        print(lt.getElement(lt.getElement(valor, 3), 1))
        print('')
        print('==============================================================================================================')
        print('')
        print('Las ultimas 3 obras')
        print(lt.getElement(lt.getElement(valor, sizevalor), 1))
        print('')
        print(lt.getElement(lt.getElement(valor, sizevalor-1), 1))
        print('')
        print(lt.getElement(lt.getElement(valor, sizevalor-2), 1))

    elif int(inputs[0]) == 6:
        print("Ingrese el departamento")
        dept = input()
        r = controller.transportarobras(catalog, dept)
        size = r[0]
        precio = r[1]
        peso = r[3]

        listaprecio = r[2]
        sizeprecio = lt.size(listaprecio)

        listadate = r[4]
        sizedate = lt.size(listadate)

        print('El total de obras a transportar es de: '+ str(size))
        print('El precio estimado es de:' + str(precio))
        print('El peso estimado es de: ' + str(peso))
        print('Las 5 obras más costosas son:')
        print((lt.getElement(listaprecio, sizeprecio))[0])
        print((lt.getElement(listaprecio, sizeprecio - 1))[0])
        print((lt.getElement(listaprecio, sizeprecio - 2))[0])
        print((lt.getElement(listaprecio, sizeprecio - 3))[0])
        print((lt.getElement(listaprecio, sizeprecio - 4))[0])
        print('')
        print('')
        print('Las 5 obras más antiguas son:')
        print((lt.getElement(listadate, sizedate))[0])
        print((lt.getElement(listadate, sizedate - 1))[0])
        print((lt.getElement(listadate, sizedate - 2))[0])
        print((lt.getElement(listadate, sizedate - 3))[0])
        print((lt.getElement(listadate, sizedate - 4))[0])
        
           
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
        num = controller.obrasPorNacionalidadEspecifica(catalog, nac)
        print('Hay ' + str(num) + ' obras de la nacionalidad ' + nac)
       

    else:
        sys.exit(0)
sys.exit(0)
