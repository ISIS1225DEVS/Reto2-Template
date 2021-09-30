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
from DISClib.Algorithms.Sorting import mergesort as merge
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog={"artists":None,"artworks":None ,"medio/tecnica":None}
    catalog['artists'] = lt.newList('SINGLE_LINKED')
    catalog['artworks'] = lt.newList('SINGLE_LINKED')
    catalog["medio/tecnica"] = mp.newMap(30, maptype='PROBING',loadfactor=0.5)
    return catalog

# Funciones para agregar informacion al catalogo
def addArtist(catalog, artist):              
    lt.addLast(catalog['artists'], artist)
def addArtwork(catalog, artwork):              
    lt.addLast(catalog['artworks'], artwork)
    mp.put(catalog["medio/tecnica"],artwork["Medium"],artwork) 

# Funciones para creacion de datos

# Funciones de consulta
def medioEspecifico(obraPorMedios,medio): 
    obrasEnMedio=mp.get(obraPorMedios,medio)
    listR=lt.newList('SINGLE_LINKED')
    for obra in lt.iterator(obrasEnMedio):
        lt.addLast(listR,obra)
    listR=merge.sort(listR, cmpDate)   
    return listR 
# Funciones utilizadas para comparar elementos dentro de una lista

def cmpDate(obra1,obra2): 
    return ((str(obra1['Date']) < str(obra2['Date'])))

# Funciones de ordenamiento
