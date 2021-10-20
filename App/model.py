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
import math 
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

    catalog['Artist'] = lt.newList('ARRAY_LIST', compareArtistID)

    catalog['Artwork'] = lt.newList('ARRAY_LIST', compareArtistID)

    catalog['Medium'] = mp.newMap(69000,
                                maptype='CHAINING',
                                loadfactor=4.0,
                                comparefunction=compareArtistMedium) 
    catalog['ArtworksByArtist'] = mp.newMap(69000,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=compareArtistMedium) 
    
    catalog["Nationality"] = mp.newMap(20000,
                                maptype='CHAINING',
                                loadfactor=4.0,
                                comparefunction=compareNationality)

    catalog['DateAcquired'] = mp.newMap(69000,
                                maptype='CHAINING',
                                loadfactor=4.0,
                                comparefunction=cmpArtworkByDateAcquired)

    catalog['ArtistBeginYear'] = mp.newMap(69000,
                                maptype='CHAINING',
                                loadfactor=4.0,
                                comparefunction=compareMapYear)
    
    catalog['ArtworksDepartment'] = mp.newMap(69000,
                                maptype='PROBING',
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
    artistID = artWork['ConstituentID']
    department = artWork['Department']
    DateAquired = artWork['DateAcquired']
    addArtWorkMedium(catalog,medium,artWork)
    addArtWorkbyArtist(catalog,artistID,artWork)
    addArtWorkDepartment(catalog,department,artWork) 
    addArtworkDateAdquired(catalog,DateAquired,artWork)



# Funciones Artistas
def addArtWorkDateAdquired(catalog,DateAquired,artWork) : 
    pass

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

# Funciones Atworks
def addArtWorkDepartment(catalog,department,artWork):
    departments = catalog['ArtworksDepartment'] 
    existedDepartment = mp.contains(departments,department)
    if existedDepartment : 
        entry = mp.get(departments,department)
        ArtworksDept = me.getValue(entry)
    else : 
        ArtworksDept = newArtworkDepartment(department)
        mp.put(departments,department,ArtworksDept)
    lt.addLast(ArtworksDept['artWorks'],artWork)


def addArtWorkbyArtist(catalog,artistIDs,artwork) :
    ListaIds = artistIDs.strip('[]').split(',')
    i = 0
    ArtistsArtworks = catalog['ArtworksByArtist'] 
    while i < len(ListaIds) : 
        ID = int(ListaIds[i])
        posArtista = searchArtistInfo(catalog,ID) 
        artistInfo = lt.getElement(catalog['Artist'],posArtista)
        DisplayName = artistInfo['DisplayName']
        existArtist = mp.contains(ArtistsArtworks,DisplayName)
        if existArtist : 
            entry = mp.get(ArtistsArtworks,DisplayName)
            ArtistArtworks = me.getValue(entry)
        else : 
            ArtistArtworks = newArtistArtwork(DisplayName)
            mp.put(ArtistsArtworks,DisplayName,ArtistArtworks)
        lt.addLast(ArtistArtworks['artWorks'],artwork)
        i += 1 


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

def newArtworkDepartment(department) : 
    Dept = {'Department':'','artWorks' : None}
    Dept['Department'] = department 
    Dept['artWorks'] = lt.newList('ARRAY_LIST')
    return Dept

def newArtistArtwork(DisplayName) : 
    Artist = {'DisplayName': '', 'artWorks' : None} 
    Artist['DisplayName'] = DisplayName
    Artist['artWorks']= lt.newList('ARRAY_LIST')
    return Artist

    
def newMedium (medium) : 
    """
    Relaciona un medio con las obras. 
    """
    Medium = {'Medium': '', 'artWorks': ''} 
    Medium['Medium'] = medium
    Medium['artWorks'] = lt.newList('ARRAY_LIST') 
    return Medium
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

def searchArtistInfo(catalog,constituentID) : 
    """
    La funcion busca un artista por su constituent ID. 
    """
    artistas = catalog['Artist']
    low = 0 
    high = lt.size(artistas)
    mid = 0 

    while low <= high : 
        mid = (high + low) // 2
        artist = lt.getElement(artistas,mid)
        ID = int(artist['ConstituentID'])
        if ID < constituentID : 
            low = mid + 1
        elif ID > constituentID : 
            high = mid - 1
        else : 
            return mid 

    return -1
    

# Funciones utilizadas para comparar elementos dentro de una lista
def compareArtistID (artist1,artist2) : 
    ID_1 = int(artist1['ConstituentID'])
    ID_2 = int(artist2['ConstituentID'])
    return ID_1 < ID_2

def compareArtworkCost(artwork1,artwork2) : 
    Cost_1 = float(artwork1['TransCost'])
    Cost_2 = float(artwork2['TransCost'])
    return Cost_1 < Cost_2


def compareArtistBeginYear(artist1,artist2) : 
    D1 = int(artist1['BeginDate'])
    D2 = int(artist2['BeginDate'])
    return D1 < D2 
def compareArtworkDate(artwork1,artwork2) :
    if len(artwork1['Date']) == 0 : 
        D1 = 99999 
    else : 
        D1 = int(artwork1['Date'])
    if len(artwork2['Date']) == 0 :  
        D2 = 99999 
    else : 
        D2 = int(artwork2['Date'])

    return D1 < D2 

def compareMapYear(id, tag):
    tagentry = me.getKey(tag)
    if (id == tagentry):
        return 0
    elif (id > tagentry):
        return 1
    else:
        return 0

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

def cmpArtworkByDateAcquired(artwork1,artwork2):
    cadena_fecha_A = artwork1['DateAcquired']
    cadena_fecha_B = artwork2['DateAcquired']
    if len(cadena_fecha_A) > 0 and len(cadena_fecha_B) > 0: 
        fecha_A = date.datetime.strptime(cadena_fecha_A,'%Y-%m-%d')
        fecha_B = date.datetime.strptime(cadena_fecha_B,'%Y-%m-%d')
        return fecha_A < fecha_B
    elif len(cadena_fecha_A) > 0 and len(cadena_fecha_B) == 0 : 
        return True
    elif len(cadena_fecha_A) == 0 and len(cadena_fecha_B) > 0 : 
        return False 

# Funciones de ordenamiento
def sortArtistID(artists,orden) : 
    if orden == 1:
      ins.sort(artists,compareArtistID)
    elif orden == 2:
      sa.sort(artists,compareArtistID)
    elif orden == 3:
      mer.sort(artists,compareArtistID)
    elif orden == 4:
      quic.sort(artists,compareArtistID)

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

def sortArtwork(catalog,orden):
    if orden == 1:
      ins.sort(catalog['Artwork'], cmpArtworkByDateAcquired)
    elif orden == 2:
      sa.sort(catalog['Artwork'], cmpArtworkByDateAcquired)
    elif orden == 3:
      mer.sort(catalog['Artwork'], cmpArtworkByDateAcquired)
    elif orden == 4:
      quic.sort(catalog['Artwork'], cmpArtworkByDateAcquired)

# Funciones conteo
def countobrasnationality(nationality, catalog):
    nationality = mp.get(catalog['Nationality'], nationality)
    if nationality:
        return me.getValue(nationality)['ArtWork']
    return None
def sortArtworkCost(artWorks,orden):
    if orden == 1:
      ins.sort(artWorks,compareArtworkCost)
    elif orden == 2:
      sa.sort(artWorks,compareArtworkCost)
    elif orden == 3:
      mer.sort(artWorks,compareArtworkCost)
    elif orden == 4:
      quic.sort(artWorks,compareArtworkCost)

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

def listArtworkbyDate(fechainicial,fechafinal,catalog):
    size= lt.size(catalog['Artwork'])
    sortArtwork(catalog,3)
    datosart = lt.newList("ARRAY_LIST")
    stop = False
    i = 1
    while i <= size and not stop:
        obra = lt.getElement(catalog['Artwork'],i)
        if len(obra['DateAcquired']) > 0 :
            fecha_obra  = date.datetime.strptime(obra['DateAcquired'],'%Y-%m-%d') 
            if fechainicial <= fecha_obra and fechafinal >= fecha_obra : 
                lt.addLast(datosart,obra) 
            elif fecha_obra > fechafinal : 
                stop = True 
        i += 1
    return datosart

def countPurchasedArtwork(artworks) : 
    size = lt.size(artworks)
    i = 1 
    count = 0 
    while i < size : 
        artwork = lt.getElement(artworks, i)
        if 'Purchase' in artwork['CreditLine'] : 
            count += 1 
        i += 1 
    return count 

#TODO: Funciones req 3
def ArtistArtworksbyMedium (DisplayName,catalog) : 
    entry = mp.get(catalog['ArtworksByArtist'],DisplayName)
    Artworks = me.getValue(entry) 
    tamanio = lt.size(Artworks) 
    mediumArtwork = {'NA':''}
    i = 1 
    while i <= tamanio : 
        artwork = lt.getElement(Artworks,i) 
    pass 

#TODO: Funciones req 5 
def calcularCosto(artwork) :

    if len(artwork['Height (cm)']) > 0 : 
        height = float(artwork['Height (cm)'])/100 
    else : 
        height = 0 
    if len(artwork['Width (cm)']) > 0 : 
        width = float(artwork['Width (cm)'])/100
    else : 
        width = 0 
    if len(artwork['Depth (cm)']) > 0 : 
        depth = float(artwork['Depth (cm)'])/100
    else : 
        depth = 0 
    if len(artwork['Diameter (cm)']) > 0 : 
        diameter = float(artwork['Diameter (cm)'])/100
    else : 
        diameter = 0 
    if len(artwork['Weight (kg)']) > 0 : 
        weight = float(artwork['Weight (kg)'])/100 
    else : 
        weight = 0 
    estimaciones = []
    
    if height > 0 and width > 0 : 
        Area = height*width 
        costoArea = Area*72 
        estimaciones.append(costoArea)
        if depth > 0 : 
            Volumen = Area*depth
            costoVolumen = Volumen*72 
            estimaciones.append(costoVolumen)
    if weight > 0 : 
        costoPeso = weight*48 
        estimaciones.append(costoPeso)
    if diameter > 0 : 
        Area = math.pi*((diameter/2)**2) 
        costoArea = Area*72 
        estimaciones.append(costoArea)
        if depth > 0 : 
            Volumen = Area*depth 
            costoVolumen = Volumen*72
            estimaciones.append(costoVolumen)
    if len(estimaciones) == 0 :
        estimaciones.append(48)
    costo = max(estimaciones) 
    return costo 





def transportarObras(department,catalog) : 
    entry = mp.get(catalog['ArtworksDepartment'],department)
    Value = me.getValue(entry) 
    artworks = Value['artWorks']
    tamanio = lt.size(artworks)
    i = 1 
    sumaCosto = 0 
    sumaPeso = 0 
    while i <= tamanio : 
        artwork = lt.getElement(artworks,i)
        weight = artwork['Weight (kg)']
        artistIDs = artwork['ConstituentID']
        listaIDs = artistIDs.strip('[]').split(',')
        DisplayName = ''
        for ID in listaIDs: 
            posArtist = searchArtistInfo(catalog,int(ID))
            artistInfo = lt.getElement(catalog['Artist'],posArtist)
            DisplayName += artistInfo['DisplayName'] + ', '
        if len(weight) == 0 : 
            weight = 0 
        sumaPeso += float(weight)    
        costo = calcularCosto(artwork) 
        sumaCosto += costo
        artwork['TransCost'] = costo 
        artwork['ArtistsNames'] = DisplayName
        i +=1 
    masCostosas = obrasMasCaras(artworks) 
    masAntiguas = obrasMasAntiguas(artworks)
    return sumaCosto,sumaPeso,masCostosas,masAntiguas,tamanio 



def obrasMasCaras(artworks) :  
    sortArtworkCost(artworks,3)
    tamanio = lt.size(artworks)
    masCaras = lt.subList(artworks,tamanio - 4,5)
    return masCaras 

def obrasMasAntiguas(artworks) : 
    sortArtworkDate(artworks,3)
    tamanio = lt.size(artworks)
    masAntiguas = lt.subList(artworks,1,5)
    return masAntiguas




    







    
