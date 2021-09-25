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


from DISClib.DataStructures.arraylist import  iterator, newList, size
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import shellsort as sh
from DISClib.Algorithms.Sorting import mergesort as me
from DISClib.Algorithms.Sorting import quicksort as qu
from datetime import datetime
import time
assert cf
import operator

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""
#VERSION RETO 2 (lo dejo comentado para comprobar que carga con la versión del reto1 luego de copiar y pegar todo)
# Construccion de modelos
#def newCatalog():
    """Inicializa el catálogo de libros

    Crea una lista vacia para guardar todos los libros

    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion

    Retorna el catalogo inicializado.
    estructura= "SINGLE_LINKED"
    catalog = {'obras': None,
               'artistas': None,
               'medium': None
               }
    catalog['artistas'] = lt.newList(estructura, cmpfunction=compareArtistId)
    catalog['obras'] = lt.newList(estructura, cmpfunction=compareObraId)
    catalog['medio'] = mp.newMap(2000,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareMediumName) """



#VERSION RETO1
# Construccion de modelos
def newCatalog():
    estructura= "ARRAY_LIST"
    catalog = {'obras': None,
               'artistas': None,
               }

    catalog['artistas'] = lt.newList(estructura, cmpfunction=compareArtistId)
    catalog['obras'] = lt.newList(estructura, cmpfunction=compareObraId)

    return catalog

# Funciones para creacion de datos

# Funciones de consulta
def buscarTecnicaMasRep(dicTecnicas):
        TecnicaMas= " "
        size_mayor=0
        for tecnica in dicTecnicas:
            size= lt.size(dicTecnicas[tecnica]["obras"])
            if size>size_mayor:
                size_mayor= size
                TecnicaMas= tecnica
        return TecnicaMas
def ObrasPorArtistaPorTecnica(catalogo,nombre):
    artistas= catalogo["artistas"]
    for artista in lt.iterator(artistas):
        if nombre == artista["DisplayName"]:
            obrasArtista= artista["Artworks"]
            Tecnicas={}
            if lt.isEmpty(obrasArtista)==False: 
                for obra in lt.iterator(obrasArtista):
                    tecnica= obra["Medium"]
                    if tecnica != "":
                        if tecnica not in Tecnicas:
                            Tecnicas[tecnica]={}
                            Tecnicas[tecnica]["nombre"]= tecnica
                            Tecnicas[tecnica]["obras"]= lt.newList("ARRAY_LIST")
                            lt.addLast(Tecnicas[tecnica]["obras"],obra)
                        else:
                            lt.addLast(Tecnicas[tecnica]["obras"],obra)
                break
        else:
            obrasArtista=None
            Tecnicas=None
    return (obrasArtista,Tecnicas) 
# Funciones utilizadas para comparar elementos dentro de una lista
# Funciones utilizadas para comparar elementos dentro de una lista

def compareArtistId(artist1, artist2):
    if artist1["ConstituentID"] < artist2["ConstituentID"]:
        return -1 
    elif artist1["ConstituentID"] == artist2["ConstituentID"]:
        return 0
    else: 
        return 1
def compareObraId(obra1, obra2):
    if obra1["ObjectID"] < obra2["ObjectID"]:
        return -1 
    elif obra1["ObjectID"] == obra2["ObjectID"]:
        return 0
    else: 
        return 1

def cmpArtistByDate(artist1, artist2):
    fecha1= (artist1['BeginDate'])
    fecha2=(artist2['BeginDate'])
    if fecha1=="":
        fecha1=0 
    if fecha2=="":
        fecha2=0
    if  int(fecha1)<int(fecha2):
        return -1 
    elif int(fecha1)==int(fecha2):
        return 0
    else: 
        return 1

def cmpArtworkByDateAcquired(artwork1, artwork2):
    #req 2, re utilizò la librerìa datetime#
    fecha1= str(artwork1['DateAcquired'])
    fecha2=str(artwork2['DateAcquired'])
    if fecha1=="":
        fecha1="0001-01-01"
    if fecha2=="":
        fecha2="0001-01-01"
    date1 = datetime.strptime(fecha1, "%Y-%m-%d")
    date2 = datetime.strptime(fecha2, "%Y-%m-%d")
    if  int(date1)<int(date2):
        return -1 
    elif int(date1)==int(date2):
        return 0
    else: 
        return 1

def cmpArtworkByDate(artwork1, artwork2):
    fecha1= (artwork1['Date'])
    fecha2=(artwork2['Date'])
    temp=False
    if fecha1=="" and fecha2 =="":
        temp= False
    elif fecha1=="" and fecha2 !="":
        temp= False
    elif fecha2=="" and fecha1 !="":
        temp= True
    else:
        temp= int(fecha1)<int(fecha2)
    return temp
def cmpArtworktByPrice(obra1, obra2):
    precio1= float(obra1["precio"])
    precio2=float(obra2["precio"])
    return precio1<precio2

def compareMediumName(name, tag):
    tagentry = me.getKey(tag)
    if (name == tagentry):
        return 0
    elif (name > tagentry):
        return 1
    else:
        return -1
# Funciones de ordenamiento
def sortArtistInDateRange(catalog, date1,date2):
    # req1
    date1 = int(date1)
    date2 = int(date2)
    #primero ordeno la lista#
    listaOrdenada= me.sort((catalog['artistas']),cmpArtistByDate)
    listaEnRango = lt.newList("ARRAY_LIST") #porque luego se accede por pos#s
    for i in lt.iterator(listaOrdenada):
        date= int(i['BeginDate'])
        if date != 0 and date >= date1 and date<=date2:
            lt.addLast(listaEnRango, i)
    return (listaEnRango)

def sortArtworksandRange(lista,inicial,final):
    inicial=datetime.strptime(str(inicial),"%Y-%m-%d")
    final=datetime.strptime(str(final),"%Y-%m-%d")
    listaEnRango= lt.newList("ARRAY_LIST")
    purchased=0
    for i in lt.iterator(lista):
        date=i['DateAcquired']
        if date=="":
            date="0001-01-01"
        date_format=datetime.strptime(str(date),"%Y-%m-%d")
        if date_format<= final and date_format>=inicial:
                lt.addLast(listaEnRango,i)
                credit_line= str(i["CreditLine"]).lower()
                if ("Purchase").lower() in credit_line or ("Purchased").lower() in credit_line :
                    purchased+=1
    lista_ordenada= ins.sort(listaEnRango,cmpArtworkByDateAcquired)
    return (lista_ordenada,purchased)
def sortArtworksByDate(lista):
    lista_ordenada= lista.copy()
    lista_ordenada= me.sort(lista_ordenada,cmpArtworkByDate)
    return lista_ordenada

def sortArtworksByPrice(listaog):
    lista= listaog.copy()
    me.sort(lista,cmpArtworktByPrice)
    return lista
def RankingCountriesByArtworks (catalog,obras):
    #req4
    lista_artistas=catalog["artistas"]
    dict_nacionalidades= {}
    for i in obras:
        for n in lt.iterator(lista_artistas):
            if i in n["Artworks"]:
                nacionalidad= n["Nationality"]
                if nacionalidad not in dict_nacionalidades:
                    dict_nacionalidades[nacionalidad]=1
                else:
                    dict_nacionalidades[nacionalidad]+=1
    return (dict_nacionalidades)


#Requisito 5#
def AsignarPrecio(object):
    #considerar datos vacios revisar reglas#
    m3=-1
    if object["Width (cm)"]!="" and object["Height (cm)"]!="" and object["Depth (cm)"]!="":
        m3= ((float(object["Width (cm)"]))*(float(object["Height (cm)"]))*(float(object["Depth (cm)"])))
        m3= m3/1000000
    m2=-1
    if object["Width (cm)"]!="" and object["Height (cm)"]!="":
        m2=(float(object["Width (cm)"]))*(float(object["Height (cm)"]))
        m2=m2/10000
    precio=-1
    preciom3= 0
    preciom2= 0
    precioKg= 0
    if object["Weight (kg)"] != "":
        precioKg= 72* float(object["Weight (kg)"])
    if m3>0:
        preciom3= 72* float(m3)
    if m2>0:
        preciom2= 72* float(m2)
    if preciom3 ==0 and preciom2==0 and precioKg==0:
        precio=48
    elif preciom2> preciom3 and preciom2> precioKg:
        precio= preciom2
    elif preciom3> preciom2 and preciom3> precioKg:
        precio= preciom3
    elif precioKg> preciom2 and precioKg> preciom3:
        precio= precioKg 
    return (precio)

def OrdenarDepartamentoAsignarPrecioyPeso(catalogo, departamento):
    obrasPorDepartamento= lt.newList()
    lista_artwork= catalogo["obras"]
    listaR = lt.newList("ARRAY_LIST") #la lista R va a tener peso,precio,listaobras#
    precio=0
    peso=0
    for obra in lt.iterator (lista_artwork):
        if obra["Department"]== departamento:
            obra["precio"]=AsignarPrecio(obra)
            lt.addLast(obrasPorDepartamento,obra)
            precio+=float(obra["precio"])
            if obra["Weight (kg)"] != "":
                peso+=float(obra["Weight (kg)"])
    lt.addLast(listaR, peso)
    lt.addLast(listaR, round(precio,3))
    lt.addLast(listaR, obrasPorDepartamento)
    return listaR

def cmpArtworkPorPrecio(Artwork1,Artwork2):
    precio1=Artwork1["precio"]
    precio2=Artwork2["precio"]
    return precio1< precio2