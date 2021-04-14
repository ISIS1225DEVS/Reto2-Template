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
    catalog["videos-id"]=mp.newMap(10000,
                                    maptype="CHAINING",
                                    loadfactor=4.0)
    catalog["categorias"]=mp.newMap(34500,
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
    if not mp.contains(catalog["videos"],country):
        videos=lt.newList(datastructure="ARRAY_LIST")
    lt.addLast(videos,video)
    mp.put(catalog["country"],country,videos)

        


# Funciones para creacion de datos

def newCategoria(name,id):
    categoria={"name":"",
                "id":"",
                "total_videos":0,
                "videos":None}
    categoria["name"]=name
    categoria["id"]=id
    categoria["videos"]=lt.newList()
    return categoria




# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
