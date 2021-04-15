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
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
from DISClib.Algorithms.Sorting import quicksort as qcks
"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    catalog={"videos": None,
             "videos-id": None,
             "categorias": None,
             "category-id": None,
             "country": None}
    catalog["videos"]=lt.newList(datastructure="ARRAY_LIST")
    catalog["videos-id"]=mp.newMap(10,
                                    maptype="CHAINING",
                                    loadfactor=4.0)
    catalog["categorias"]=mp.newMap(10,
                                    maptype="PROBING",
                                    loadfactor=0.5)
    catalog["category-id"]=mp.newMap(37,
                                     maptype="CHAINING",
                                     loadfactor=4.0)
                                     
    catalog["country"]=mp.newMap(20,
                                 maptype="PROBING",
                                 loadfactor=0.5)
    return catalog
                                                                                            

# Funciones para agregar informacion al catalogo

def addVideo(catalog,video):
    if video["video_id"]!="#NAME?":
        lt.addLast(catalog["videos"],video)
        mp.put(catalog["videos-id"],video["video_id"],video)


def addCategoria(catalog,categoria):
    tag=newCategoria(categoria["name"],categoria["id"])
    mp.put(catalog["categorias"],categoria["name"],tag)
    mp.put(catalog["category-id"],categoria["id"],tag)

def addCountry(catalog,video):
    country=video["country"]
    if not mp.contains(catalog["country"],country):
        videos=lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(videos,video)
        mp.put(catalog["country"],country,videos)
    else:
        videos=mp.get(catalog["country"],country)
        lt.addLast(videos["value"],video)
        mp.put(catalog["country"],country,videos["value"])

        


# Funciones para creacion de datos

def newCategoria(name,id):
    categoria={"name":"",
                "id":""}
    categoria["name"]=name
    categoria["id"]=id
    return categoria




# Funciones de consulta

def sameCountryCategory(catalogo_pais,catalogo_categoria,country,category):
    country_cringe=mp.get(catalogo_pais,country)
    country_vids=country_cringe["value"]
    lista_categoria=mp.valueSet(catalogo_categoria)
    final_vids=lt.newList(datastructure="ARRAY_LIST")
    Id=None
    for i in range(1,lt.size(lista_categoria)+1):
        categoria=lt.getElement(lista_categoria,i)
        name=categoria["name"]
        if category==name:
            Id=categoria["id"]
            break
    for i in range(1,lt.size(country_vids)+1):
        video=lt.getElement(country_vids,i)
        if video["category_id"]==Id:
            lt.addLast(final_vids,video)
    sorted_vids=sortVideosViews(final_vids)
    return sorted_vids

def mostTrending(sorted_list):
    pass





# Funciones utilizadas para comparar elementos dentro de una lista

def cmpVideosbyViews(video1,video2):
    return (int(video1["views"])>int(video2["views"]))

def cmpVideosbyName(video1,video2):
    return (str(video1["title"]).lower()>str(video2["title"]).lower()) 

# Funciones de ordenamiento

def sortVideosViews(lista):
    sorted_list=qcks.sort(lista,cmpVideosbyViews)
    return sorted_list

def sortVideosName(lista):
    sorted_list=qcks.sort(lista,cmpVideosbyName)
    return sorted_list

