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
    if mp.contains(catalog['Medium'], artwork['Medium']):
        llave_valor=mp.get(catalog['Medium'],artwork['Medium'])
        valor=me.getValue(llave_valor)
        #print(llave_valor)
        lt.addLast(valor, artwork)
        #mp.put(catalog['Medium'], llave_valor,valor)
        #mp.put(catalog['Medium'], artwork['Medium'], artwork)
    else:
        lista_creada= lt.newList(cmpfunction=cmpMedio)
        lt.addLast(lista_creada, artwork)
        mp.put(catalog['Medium'],artwork['Medium'], lista_creada)
  

def addArtist(catalog, artistname):

    lt.addLast(catalog['Artist'], artistname)

def newCatalog(estructuraDatos):
    

    catalog = {'Art': None,
               'Medium': None,
               'Artist': None}

    catalog['Art'] = lt.newList(estructuraDatos)

    catalog['Medium'] = mp.newMap(1000, maptype='CHAINING', loadfactor=4.0, comparefunction=cmpMedio)#Cómo sé qué caracteristicas le pongo a este mapa?, cant de espacio por ejemplo, ?????.
                                   #Creería que un map de tipo chaining para que las obrascon el mismo medium se guarden en la misma llave, no?
                                   #Pero el tamño del mapa qué? Ni idea xd

    catalog['Artist'] = lt.newList(estructuraDatos)
 
    return catalog

def get_primeros(lista_global, inicial, final):
    lista_ordenada= sortArtists(lista_global)
    lista_filtrada= filtrar_anhos(lista_ordenada, inicial, final)
    lista_primeros= lt.subList(lista_filtrada, 1, 3)
    return lista_primeros

def get_ultimos(lista_global, inicial, final):
    lista_ordenada= sortArtists(lista_global)
    lista_filtrada= filtrar_anhos(lista_ordenada, inicial, final)
    lista_ultimos= lt.subList(lista_filtrada, (lt.size(lista_filtrada)-3),3)
    return lista_ultimos

def obras_medio(catalog, Medio):
    medium = mp.get(catalog['Medium'], Medio)
    mediofinal= me.getValue(medium)
    return mediofinal
    

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

def get_transporte(arte, nombre_departamento):
    lista_respuestas= lt.newList()
    obras_departamento= buscar_obrasxdepartamento(arte, nombre_departamento)
    totalobras= lt.size(obras_departamento)
    estimado_precio= get_estimado_precio(obras_departamento)
    estimado_peso= get_estimado_peso(obras_departamento)
    mas_antiguas= get_primerosobras(obras_departamento)
    lt.addLast(lista_respuestas, totalobras)
    lt.addLast(lista_respuestas, estimado_precio)
    lt.addLast(lista_respuestas, estimado_peso)
    lt.addLast(lista_respuestas, mas_antiguas)
    
def buscar_obrasxdepartamento(arte, departamento):
    obras_dep= lt.newList()
    for obras_recorridas in lt.iterator(arte):
        if departamento == obras_recorridas["Department"]:
            lt.addLast(obras_dep, obras_recorridas)
            break
    return obras_dep

def get_estimado_precio(obras_dep):
    precio_total=0
    precio_x_kg= 35
    precio_x_defecto= 48
    for obras_x_dep in lt.iterator(obras_dep):
        if obras_x_dep["Weight (kg)"] == "":
            precio_total+=precio_x_defecto
        else:
            precio_total+=precio_x_kg*(float(obras_x_dep["Weight (kg)"]))
    return precio_total

def get_estimado_peso(obras_dep):
    peso_total= 0
    for obras_x_dep in lt.iterator(obras_dep):
        peso_total+=(float(obras_x_dep["Weight (kg)"]))
    return peso_total
    
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
def AddArtFecha(art, fechai, fechaf, Lista):
    if cmpArtworkByDateAcquiredSolo(art, fechai, fechaf):
            lt.addLast(Lista, art)
    return Lista
            
    
    

# Funciones de consulta


def escompra(artwork):
    if artwork['CreditLine'] == 'Purchase':
        return True

def verID(catalog):
    nacionalidades = []
    nacionalidades1 = []
    listanacionalidades = lt.newList()
    for keys in catalog['Art']:   
         listaArte = catalog['Art'][keys]
         if type(listaArte) == list:
            for Artworks in listaArte:
                idx = Artworks['ConstituentID']
                id = idx.strip('[],')
                

                for keysa in catalog['Artist']:   
                    listaArtista = catalog['Artist'][keysa]
                    if type(listaArtista) == list:
                        for Artista in listaArtista:
                            ida = Artista['ConstituentID']
                            if(ida == id):
                                nacion = Artista['Nationality']
                                nacionalidades.append(nacion)
                                    
    for nacion in nacionalidades:
        a = [nacion, nacionalidades.count(nacion)]

        if nacion not in nacionalidades1:
            lt.addLast(listanacionalidades, a)
            nacionalidades1.append(nacion)
        
        
    return listanacionalidades



# Funciones utilizadas para comparar elementos dentro de una lista
def cmpMedio(key, medio):
    medentry = me.getKey(medio)
    if key == medentry:
        return 0
    elif (key > medentry):
        return 1
    else:
        return -1
 
def cmpNumNacionalidad(nac1, nac2):
    a = (nac1[1])
    b = (nac2[1])
    return int(a) > int(b)
    
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
    if artworka[0] != '':
        return (int(artworka[0]) >= int(fechai)) and (int(artworka[0]) <= int(fechaf))
    else: return False


   

# Funciones de ordenamiento

def OrganizarFecha(lista):
    return sa.sort(lista, cmpArtworkByDateAcquired)

def OrganizarNacionalidad(lista):
    return sa.sort(lista, cmpNumNacionalidad)

def organizar_medio(lista, num):
   # list = lt.newList()
    print (lista)
    listaOrganizadaPorAño = sa.sort(lista, ordenar_fecha)
    listaRecortada = lt.sublist(listaOrganizadaPorAño, 0, num)
    return listaRecortada


