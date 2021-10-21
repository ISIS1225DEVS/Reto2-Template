"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.arraylist import newList, size
import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

"""
Esta función contiene un condicional el cual identifica si el medio ya esta identificado, para asi mismo incluir dentro, la obra encontrada (perteniciente).
De lo contrario generaría una nueva lista del medio no encontrado y añadiria esa obra que encontro (perteneciente).
"""
def addArt(catalog, artwork):

    lt.addLast(catalog['Art'], artwork)
    if artwork['Weight (kg)'] != '':
        pass

    
    #print('Altura' + artwork['Height (cm)'])

    if mp.contains(catalog['Medium'], artwork['Medium']):
        llave_valor=mp.get(catalog['Medium'],artwork['Medium'])
        valor=me.getValue(llave_valor)
        lt.addLast(valor, artwork)

    else:
        lista_creada= lt.newList()
        lt.addLast(lista_creada, artwork)
        mp.put(catalog['Medium'],artwork['Medium'], lista_creada)

    txt = artwork['ConstituentID']
    id = txt.strip('[]')
    if ',' in id:
        ids = id.strip(' ')
        lista = ids.split(',')
        for ID in lista:
            if mp.contains(catalog['ID'], ID):
                llave_valor=mp.get(catalog['ID'], ID)
                valor=me.getValue(llave_valor)
                lt.addLast(valor, artwork)
                
            else:
                lista_creada= lt.newList()
                lt.addLast(lista_creada, artwork)
                

                mp.put(catalog['ID'],ID , lista_creada)
    else:
        if mp.contains(catalog['ID'], id):
                llave_valor=mp.get(catalog['ID'], id)
                valor=me.getValue(llave_valor)
                lt.addLast(valor, artwork)
                
        else:
            lista_creada= lt.newList()
            lt.addLast(lista_creada, artwork)
        
            mp.put(catalog['ID'],id , lista_creada)

    if mp.contains(catalog['Department'], artwork['Department']):
        llave_valor=mp.get(catalog['Department'],artwork['Department'])
        valor=me.getValue(llave_valor)
        lt.addLast(valor, artwork)

    else:
        lista_creada= lt.newList()
        lt.addLast(lista_creada, artwork)
        mp.put(catalog['Department'],artwork['Department'], lista_creada)


def addArtist(catalog, artistname):

    lt.addLast(catalog['Artist'], artistname)
    mp.put(catalog['IDA'],artistname['ConstituentID'],artistname['Nationality'])

    #if mp.contains(catalog['IDA'], artistname['ConstituentID']):
    #    llave_valor=mp.get(catalog['IDA'],artistname['ConstituentID'])
    #    valor=me.getValue(llave_valor)
    #    lt.addLast(valor, artistname)
    #else:
    #    lista_creada= lt.newList(cmpfunction=cmpMedio)
    #    lt.addLast(lista_creada, artistname)
    #    mp.put(catalog['IDA'],artistname['ConstituentID'], lista_creada)


    

def newCatalog(estructuraDatos):
    

    catalog = {'Art': None,
               'Medium': None,
               'Artist': None}

    catalog['Art'] = lt.newList(datastructure=estructuraDatos)

    catalog['Medium'] = mp.newMap(1000, maptype='CHAINING', loadfactor=4.0, comparefunction=cmpMedio)
    catalog['Nationality'] = mp.newMap(300, maptype='CHAINING', loadfactor=4.0, comparefunction=cmpMedio)
    catalog['ID'] = mp.newMap(1000, maptype='CHAINING', loadfactor=4.0, comparefunction=cmpMedio)
    catalog['Artist'] = lt.newList(datastructure=estructuraDatos)
    catalog['IDA'] = mp.newMap(1000, maptype='PROBING', loadfactor=0.5, comparefunction=cmpMedio)
    catalog['Department'] = mp.newMap(1000, maptype='PROBING', loadfactor=0.5, comparefunction=cmpMedio)

    
 
    return catalog


def obras_medio(catalog, Medio):
    medium = mp.get(catalog['Medium'], Medio)
    mediofinal= me.getValue(medium)
    return mediofinal

def nacionalidadPorObra(catalog):
    ids = mp.keySet(catalog['ID'])
    size = lt.size(ids)
    
    for pos in range(size):
        id = lt.getElement(ids, pos)

        if id is not None:

            valorobras = mp.get((catalog['ID']), id) 
            obras = me.getValue(valorobras)

            valornacionalidad = (mp.get(catalog['IDA'], id))
            
            if valornacionalidad is not None:
                nacionalidad = me.getValue(valornacionalidad)
                
            
                if mp.contains(catalog['Nationality'], nacionalidad):

                    llave_valor = mp.get(catalog['Nationality'],nacionalidad)
                    valor = me.getValue(llave_valor)
                    lt.addLast(valor, obras)
                    #mp.put(catalog['Nationality'], llave_valor, valor)

                else:
                    lista_creada= lt.newList()
                    lt.addLast(lista_creada, obras)
                    mp.put(catalog['Nationality'], nacionalidad, lista_creada)

                 

def listaNacionalidad(catalog):
    listaNacionalidades = lt.newList()
    lista = mp.keySet(catalog['Nationality'])
    size = lt.size(lista)
    for pos in range(size):
        nacionalidad = lt.getElement(lista, pos)
        num = tamañoMapaNacionalidad(catalog, nacionalidad)
        lst = [nacionalidad, num]
        lt.addLast(listaNacionalidades, lst)

    ms.sort(listaNacionalidades, cmpNumNacionalidad)
    return listaNacionalidades
    
def tamañoMapaNacionalidad(catalog, nacionalidad):
    valor = mp.get(catalog['Nationality'], nacionalidad)
    return lt.size(me.getValue(valor))
    

def get_conteo(lista_global, inicial, final):
    lista_ordenada= sortArtists(lista_global)
    lista_filtrada= filtrar_anhos(lista_ordenada, inicial, final)
    return lt.size(lista_filtrada)
    

def ordenar_anhos(artista1, artista2):
    return (int(artista1['BeginDate']) < int(artista2['BeginDate']))

def sortArtists(lista):
    return sa.sort(lista, ordenar_anhos)

def filtrar_anhos(lista, inicial, final):
    index_inicial= 0
    index_final= 0
    cont_inicial= 0
    cont_final= 0
    for artista in lt.iterator(lista):
        if int(artista['BeginDate'])>= inicial:
            index_inicial= cont_inicial+1
            break
        cont_inicial+=1
    for artista in lt.iterator(lista):
        if int(artista['BeginDate'])> final:
            index_final= cont_final+1
            break
        cont_final+=1
    num_pos= index_final-index_inicial
    lista_filtrada= lt.subList(lista, index_inicial, num_pos)
    return lista_filtrada

def get_obrasxtecnica(catalog, nombre_artista):
    id= get_idArtista(catalog['Artist'], nombre_artista)
    respuesta= lt.newList()
    if id == -1:
        print("El artista no existe en la lista de artistas.")
        return -1
    else:
        obras= buscar_obrasxartista(catalog['Art'], id)
        total= lt.size(obras)
        total_tecnicas= conteo_tecnicas_obras(obras)
        conteo_total= lt.size(total_tecnicas)
        tecnica_mas_utilizada= get_tecnica_mas_utilizada(total_tecnicas)
        lista_obras_tecnica= get_listado(obras, tecnica_mas_utilizada)
        lt.addLast(respuesta, total)
        lt.addLast(respuesta, conteo_total)
        lt.addLast(respuesta, tecnica_mas_utilizada)
        lt.addLast(respuesta, lista_obras_tecnica)
    return respuesta

def get_listado(obras, tecnica_mas_utilizada):
    lista= lt.newList()
    for obra in lt.iterator(obras):
        if obra['Medium']== tecnica_mas_utilizada:
            lt.addLast(lista, obra)
    return lista

def get_tecnica_mas_utilizada(total_tecnicas):
    orden= sa.sort(total_tecnicas, ordenar_conteo)
    tecnica= lt.firstElement(orden)
    return tecnica['Nombre']

def ordenar_conteo(tecnica1, tecnica2):
    return (int(tecnica1['Count']) > int(tecnica2['Count']))

def conteo_tecnicas_obras(obras):
    obras_ordenadas= sortObras(obras)
    conteo_tecnicas= lt.newList()
    nombre_tecnica= ""
    cantidad_tecnica= 0
    primera= True
    tam_obras_ordenadas= lt.size(obras_ordenadas)
    cambio= False
    for obra in lt.iterator(obras_ordenadas):
        #solo para la primera la iteración
        if primera== True:
            nombre_tecnica= str(obra['Medium'])
            cantidad_tecnica+= 1
            primera= False
        else:
            if str(obra['Medium'])== nombre_tecnica:
               cantidad_tecnica+=1
            else: 
                cambio= True
                dict_tecnica={"Nombre": nombre_tecnica, "Count": cantidad_tecnica}
                lt.addLast(conteo_tecnicas, dict_tecnica)
                #se reinicia, cambia la tecnica
                nombre_tecnica=str(obra['Medium'])
                cantidad_tecnica=1
    if tam_obras_ordenadas==1 or cambio== False:
        dict_tecnica={"Nombre": nombre_tecnica, "Count": cantidad_tecnica}
        lt.addLast(conteo_tecnicas, dict_tecnica)
    return conteo_tecnicas

def ordenar_obrasxtecnica(obra1, obra2):
    return (str(obra1['Medium']) < str(obra2['Medium']))

def sortObras(lista):
    return sa.sort(lista, ordenar_obrasxtecnica)

def get_idArtista(artistas, nombre_artista):
    for i in lt.iterator(artistas):
        if i['DisplayName']==nombre_artista:
            return i["ConstituentID"]
    return -1

def buscar_obrasxartista(artworks, id):
    obras= lt.newList()
    for obras_recorridas in lt.iterator(artworks):
        ids=(obras_recorridas["ConstituentID"]).strip('][').split(', ')
        for idArtist in ids:
            if idArtist == id:
                lt.addLast(obras, obras_recorridas)
                break
    return obras


def get_estimado_precio(catalog, dept):
    listaobras = lt.newList()
    valor_list = mp.get(catalog['Department'], dept)
    list = me.getValue(valor_list)
    precio_total=0
    precio_x_kg= 35
    precio_x_defecto= 48

    for obras_x_dep in lt.iterator(list):
        if obras_x_dep["Weight (kg)"] == "":
            precio_obra = precio_x_defecto
        else:
            precio_obra = precio_x_kg*(float(obras_x_dep["Weight (kg)"]))
        listaprecio = [obras_x_dep, precio_obra]
        lt.addLast(listaobras, listaprecio)
        precio_total += precio_obra
    return precio_total, listaobras

def get_estimado_peso(catalog, dept):
    valor_list = mp.get(catalog['Department'], dept)
    list = me.getValue(valor_list)
    peso_total= 0
    for obras_x_dep in lt.iterator(list):
        if type(obras_x_dep["Weight (kg)"]) != str:
            peso_total+=(float(obras_x_dep["Weight (kg)"]))
    return peso_total
    
def obras_antiguas(catalog, dept):
    listaobras = lt.newList()
    valor_list = mp.get(catalog['Department'], dept)
    list = me.getValue(valor_list)

    for obras_x_dep in lt.iterator(list):
        if obras_x_dep["Date"] != '':
            listaDate = [obras_x_dep, obras_x_dep["Date"]]
            lt.addLast(listaobras, listaDate )
    return listaobras
    
def get_primerosobras(lista):
    lista_ordenada= sortObrasxfecha(lista)
    lista_primeros= lt.subList(lista_ordenada, 1, 5)
    return lista_primeros

def ordenar_fecha(obra1, obra2):
    return (int(obra1['Date']) < int(obra2['Date']))

def sortObrasxfecha(lista):
    return sa.sort(lista, ordenar_fecha)

# Construccion de modelos

# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos
def AddArtFecha(art, fechai, fechaf, lista):
    if cmpArtworkByDateAcquiredSolo(art, fechai, fechaf):
            lt.addLast(lista, art)
            
    
    

# Funciones de consulta

def sizelistaDepart(catalog, dept):
    valor_list = mp.get(catalog['Department'], dept)
    list = me.getValue(valor_list)

    return lt.size(list)
    


def escompra(artwork):
    if artwork['CreditLine'] == 'Purchase':
        return True

# Funciones utilizadas para comparar elementos dentro de una lista
def cmpMedio(key, medio):
    medentry = me.getKey(medio)
    if key == medentry:
        return 0
    elif (key > medentry):
        return 1
    else:
        return -1

def cmpArtistID(artist1, artist2):
    if artist1['ConstituentID'] == artist2['ConstituentID']:
        return 0
    elif (artist1['ConstituentID'] > artist2['ConstituentID']):
        return 1
    else:
        return -1
 

def cmpNumNacionalidad(nac1, nac2):
    num1 = nac1[1]
    num2 = nac2[1]
    return num1 < num2
    
def cmpArtworkByDateAcquired(artwork1, artwork2):
                    # Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork
    artwork1a = (artwork1['DateAcquired']).split('-')
    artwork2a = (artwork2['DateAcquired']).split('-')
    if float(artwork1a[0]) == float(artwork2a[0]):
        if float(artwork1a[1]) == float(artwork2a[1]):
            return (float(artwork1a[2]) < float(artwork2a[2]))
                
        else:
            return (float(artwork1a[1]) < float(artwork2a[1]))

    else:
        return (float(artwork1a[0]) < float(artwork2a[0]))

def cmpArtworkByDateAcquiredSolo(artwork, fechai, fechaf):
    artworka = (artwork['DateAcquired']).split('-')
    fechai = fechai.split('-')
    fechaf = fechaf.split('-')
    if artworka[0] != '':
        if (int(artworka[0]) >= int(fechai[0])) and (int(artworka[0]) <= int(fechaf[0])):
            if (int(artworka[1]) >= int(fechai[1])) and (int(artworka[1]) <= int(fechaf[1])):
                if (int(artworka[1]) >= int(fechai[1])) and (int(artworka[1]) <= int(fechaf[1])):
                    return True
    
    else: return False

def cmpPrecio(art1, art2):
    return art1[1] < art2[1]


   

# Funciones de ordenamiento

def OrganizarFecha(lista):
    return ms.sort(lista, cmpArtworkByDateAcquired)

def organizarPrecio(lista):
    return ms.sort(lista, cmpPrecio)

def OrganizarNacionalidad(lista):
    return sa.sort(lista, cmpNumNacionalidad)

def organizar_medio(lista, num):
   # list = lt.newList()
    listaOrganizadaPorAño = sa.sort(lista, ordenar_fecha)
    listaRecortada = lt.sublist(listaOrganizadaPorAño, 0, num)
    return listaRecortada


