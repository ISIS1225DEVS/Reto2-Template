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


from csv import DictReader
from sys import call_tracing
import sys 
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as mer
from DISClib.Algorithms.Sorting import quicksort as quic
from DISClib.DataStructures import mapentry as me
assert cf
import datetime as date
from DISClib.Utils import error as error
import time
sys.setrecursionlimit(10**6)


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""


# Construccion de modelos


def newCatalog():

    catalog = {'Artwork':None ,'Artist': None,
               'ArtistID': None,
               'Medium': None}

    catalog['Artist'] = lt.newList('SINGLE_LINKED', compareArtistID)

    catalog['Artwork'] = lt.newList('SINGLE_LINKED', compareArtistID)

    catalog['Medium'] = mp.newMap(69000,
                                maptype='CHAINING',
                                loadfactor=0.5,
                                comparefunction=compareArtistMedium) 
    
    catalog["Nationality"] = mp.newMap(20000,
                                maptype='CHAINING',
                                loadfactor=0.5,
                                comparefunction=compareNationality)

    catalog['ArtistBeginYear'] = mp.newMap(69000,
                                maptype='CHAINING',
                                loadfactor=0.5,
                                comparefunction=compareMapYear)
    return catalog

# Funciones para agregar informacion al catalogo
def addArtist(catalog, name, id,bio,nationality,gender,begin,end,wiki,ulan):
    artist = {'DisplayName': '','ConstituentID': 0,'ArtistBio': '',
        'Nationality': '','Gender': '','BeginDate': 0, 'EndDate': 0,
            'Wiki QID': '','ULAN': 0}
    artist['DisplayName'] = name
    artist['ConstituentID'] = id  
    artist['ArtistBio'] = bio 
    artist['Nationality'] = nationality
    artist['Gender'] = gender
    artist['BeginDate'] = begin
    artist['EndDate'] = end
    artist['Wiki QID'] = wiki 
    artist['ULAN'] = ulan
    return artist

def addArtWork (catalog,artWork) : 
    lt.addLast(catalog['Artwork'],artWork)
    medium = artWork['Medium'] 
    addArtWorkMedium(catalog,medium,artWork)

def addArtist(catalog,artist) : 
    lt.addLast(catalog['Artist'],artist)
    year = artist['BeginDate'] 
    addArtistYear(catalog,year,artist) 

def addArtistYear(catalog,year,artist) : 
    years = catalog['ArtistBeginYear'] 
    existedYear = mp.contains(years,year)
    if existedYear : 
        entry = mp.get(years,year)
        Year = me.getValue(entry)
    else : 
        Year = newArtistBeginYear(year)
        mp.put(years,year,Year)
    lt.addLast(Year['Artists'],artist)



def addArtWorkMedium(catalog,medium,artWork) : 
    mediums = catalog['Medium']
    existmedium = mp.contains(mediums,medium)
    if existmedium : 
        entry = mp.get(mediums,medium)
        Medium = me.getValue(entry) 
    else : 
        Medium = newMedium(medium) 
        mp.put(mediums,medium,Medium)
    lt.addLast(Medium['artWorks'],artWork)


# Funciones para creacion de datos

    
def newMedium (medium) : 
    """
    Relaciona un medio con las obras. 
    """
    medium = {'Medium': '', 'artWorks': None} 
    medium = medium['Medium'] = medium
    medium['artWorks'] = lt.newList('ARRAY_LIST') 
    return medium
def newArtistBeginYear(Year) : 
    year = {'Begin Year': '', 'Artists': None}
    year['Begin Year'] = Year 
    year['Artists'] = lt.newList('ARRAY_LIST')
    return year

# Funciones de consulta
def artWorksbyMedium(catalog,medium) :
    Medium = mp.get(catalog['Medium'],medium)
    if Medium : 
        return me.getValue(Medium)
def oldestn(artWorks,n) : 
    size = lt.size(artWorks) 
    i = 0
    oldest = [] 
    while i < n : 
        pos = -n + size 
        oldest.append(lt.getElement(artWorks,pos))

# Funciones utilizadas para comparar elementos dentro de una lista
def compareArtistBeginYear(artist1,artist2) : 
    D1 = int(artist1['BeginDate'])
    D2 = int(artist2['BeginDate'])
    return D1 < D2 
def compareArtworkDate(artwork1,artwork2) : 
    return int(artwork1['Date']) < int(artwork2['Date'])
def compareMapYear(id, tag):
    tagentry = me.getKey(tag)
    if (id == tagentry):
        return 0
    elif (id > tagentry):
        return 1
    else:
        return 0
def compareArtistID(artistid1, artistid2):
    if (int(artistid1) == int(artistid2)):
        return 0
    elif int(artistid1) > int(artistid2):
        return 1
    else:
        return -1

def compareArtistMedium(keyname, medium):
    mediumentry = me.getKey(medium)
    if (keyname == mediumentry):
        return 0
    elif (keyname > mediumentry):
        return 1
    else:
        return -1

def compareNationality(keyname, nationality):
    nationalityentry = me.getKey(nationality)
    if (keyname == nationalityentry):
        return 0
    elif (keyname > nationalityentry):
        return 1
    else:
        return -1


# Funciones de ordenamiento
def sortArtistBegin(artists,orden) : 
    if orden == 1:
      ins.sort(artists,compareArtistBeginYear)
    elif orden == 2:
      sa.sort(artists,compareArtistBeginYear)
    elif orden == 3:
      mer.sort(artists,compareArtistBeginYear)
    elif orden == 4:
      quic.sort(artists,compareArtistBeginYear)

def sortArtworkDate(artWorks,orden):
    if orden == 1:
      ins.sort(artWorks,compareArtworkDate)
    elif orden == 2:
      sa.sort(artWorks,compareArtworkDate)
    elif orden == 3:
      mer.sort(artWorks,compareArtworkDate)
    elif orden == 4:
      quic.sort(artWorks,compareArtworkDate)

# Funciones conteo
def countobrasnationality(nationality, catalog):
    nationality = mp.get(catalog['Nationality'], nationality)
    if nationality:
        return me.getValue(nationality)['ArtWork']
    return None
#TODO: Funciones req 1 

def listCronoArtist(anioinicial,aniofinal,catalog) : 
    """
    La funcion retorna los artistas nacidos en un anio.

    """
    beginYears = catalog['ArtistBeginYear']
    anios = mp.keySet(catalog['ArtistBeginYear'])
    artists = lt.newList('ARRAY_LIST')
    i = 1 
    while i <= lt.size(anios) : 
        anio = int(lt.getElement(anios,i))
        if anio >= anioinicial and anio <= aniofinal : 
            entry = mp.get(beginYears, str(anio))
            valor = me.getValue(entry)
            j = 1 
            while j <= lt.size(valor['Artists']) :
                artista = lt.getElement(valor['Artists'],j)
                lt.addLast(artists, artista)
                j +=1 
        i += 1 
    return artists


#TODO: Funciones req 2 
