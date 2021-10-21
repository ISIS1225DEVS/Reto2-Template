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


from math import atan2
from DISClib.DataStructures.arraylist import newList
from DISClib.DataStructures.chaininghashtable import newMap
import config as cf
import copy
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
import time 
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as mg
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    """ Inicializa el catálogo de libros

    Crea una lista vacia para guardar todos los libros

    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion

    Retorna el catalogo inicializado.
    """
    catalog = {'Artists': None,
               'Artworks': None,
               'Constituen ID': None,
               "DateAcquired" : None,
               'tags': None,
               'tagIds': None,
               'years': None}

    
    catalog['Artists'] = lt.newList('ARRAY_LIST', compareArtistIds)
    catalog['Artworks'] = lt.newList('ARRAY_LIST', compareArtworksIds)

    

    catalog['ArtistID'] = mp.newMap(10000,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareArtworksIds)

    
    
    catalog['BeginDate'] = mp.newMap(500,
                                   maptype='CHAINING',
                                   loadfactor=5,
                                   comparefunction=compareBeginDate)
    
    catalog['Medium'] = mp.newMap(34500,
                                maptype='CHAINING',
                                loadfactor=2,
                                comparefunction=compareArtworksbymedium)


    
    catalog['Work_Nationality'] = mp.newMap(34500,
                                  maptype='CHAINING',
                                  loadfactor=4.0,
                                  comparefunction=compareNationality)
    
    catalog['Artists_ConstituentID'] = mp.newMap(16000,
                                 maptype='PROBING',
                                 loadfactor=0.5,)
    
    catalog["DateAcquired"] = mp.newMap(16000,
                                maptype="PROBING",
                                loadfactor=0.5)
    catalog['Department'] = mp.newMap(34500,
                                maptype='CHAINING',
                                loadfactor=2,
                                comparefunction=compareArtworksbyDepartment)  
    '''
    catalog['Work_ConstituentID'] = mp.newMap(16000,
                                 maptype='PROBING',
                                 loadfactor=0.5,)
                                 
    '''

    return catalog
  

# Funciones para agregar informacion al catalogo
def addtomap(map,key,object):

    if mp.contains(map,key):

        if type(mp.get(map,key)['value']) == type(object):    
            l=lt.newList(datastructure='ARRAY_LIST')
            lt.addLast(l,mp.get(map,key)['value'])
            lt.addLast(l,object)
            mp.put(map,key,l)
            
        else:     
            entry=mp.get(map,key)
            list=entry['value']
            
            lt.addLast(list,object)
            #print(mp.get(catalog['BeginDate'],artist['BeginDate']))
            
    else: 
        mp.put(map,key,object)
    
def addtomap2(map,key,object):

    if mp.contains(map,key):

        if type(mp.get(map,key)['value']) == type(object):    
            l=lt.newList(datastructure='SINGLED_LIST')
            lt.addLast(l,mp.get(map,key)['value'])
            lt.addLast(l,object)
            
            mp.put(map,key,l)
            
        else:     
            entry=mp.get(map,key)
            list=entry['value']
            
            lt.addLast(list,object)
            #print(mp.get(catalog['BeginDate'],artist['BeginDate']))
            
    else: 
        mp.put(map,key,object)
    
 

def addArtist(catalog, artist):
    lt.addLast(catalog["Artists"], artist)

    addtomap(catalog['BeginDate'],artist['BeginDate'],artist)
    mp.put(catalog['Artists_ConstituentID'],artist['ConstituentID'],artist)



    
def addArtwork(catalog, artwork):
    lt.addLast(catalog["Artworks"], artwork)

    addtomap(catalog['Medium'],artwork['Medium'],artwork)
    addtomap2(catalog["Department"],artwork["Department"],artwork)
    #mp.put(catalog['Work_ConstituentID'],artwork['ConstituentID'],artwork)
    


def addDateAcquired(catalog,artwork):
    addtomap(catalog["DateAcquired",artwork["DateAcquired"],artwork])







    

   





# Funciones para creacion de datos



# Funciones de consulta


    #Requerimiento 2

def purchase(gd):
    
    count=0
    a=gd["elements"]
    
    
    for purch in a:
        
        i= purch["CreditLine"]
    
        if "purchase" in i.lower():
            count += 1

    return count

def getAdquisiciones(catalog, min, max):

    a=mp.newMap()
    x=lt.newList("ARRAY_LIST")
    i=0
    for byDate in catalog["Artworks"]["elements"]:
        
        if byDate["DateAcquired"]!= "":
            date=byDate["DateAcquired"].replace("-","")
            
            if int(date)>=min and int(date)<=max:
                lt.addLast(x,byDate)

    mg.sort(x,compareDateAcquired)

    return x

#Req 4

def getbyNationality(catalog):

    nac=mp.newMap()
    x=lt.newList("ARRAY_LIST")
    dic={}
    

    for artist in catalog["Artists"]["elements"]:
        count=0
        
        for artwork in catalog["Artworks"]["elements"]:
            
            if artist["ConstituentID"] in artwork["ConstituentID"]:
                count+=1
                
            
        if artist["Nationality"] in dic.keys():
            z=dic[artist["Nationality"]]
            z+=count
            dic[artist["Nationality"]]=z
        else:  
            dic[artist["Nationality"]]=count 

    for o in dic:
        p=[]
        p=[o,dic[o]]
        mp.put(nac,o,dic[o])
        lt.addLast(x,p)
    
    mg.sort(x,cmpNationality)

    return nac,x






#REQ5

def TransportCos(catalog,depa):
    start = time.process_time_ns()

    listD = ArtbyDepartment(catalog,depa)
    
    Cost=0
    Weight=0
    
    for artwork in listD['elements']:
        costA=48
        Costs=[]
        
        if artwork['Weight (kg)'] != '':
            costW = float(artwork['Weight (kg)']) * 35
            Weight += float(artwork['Weight (kg)'])
        else:
            costW=0
        Costs.append(costW)

        if artwork['Height (cm)'] != '' and artwork['Width (cm)'] != '':
            costm_2 = float(artwork['Height (cm)']) * float(artwork['Width (cm)']) * 35
        else:
            costm_2=0
        Costs.append(costm_2)

        if artwork['Height (cm)'] != '' and artwork['Width (cm)'] != '' and artwork['Depth (cm)'] != '':
            costm_3 = float(artwork['Height (cm)'])/100 * float(artwork['Width (cm)'])/100 * float(artwork['Depth (cm)'] )/100 *35
        else:
            costm_3=0
        Costs.append(costm_3)

        if max(Costs) != 0:
         
            Cost += max(Costs)
            artwork['Cost']=str(round(max(Costs),2)) +' USD'
        else:
            Cost += costA
            artwork['Cost']=str(round(costA,2)) + ' USD'

    #Artworks_Artist(listD,catalog['Artists'])    

    mg.sort(listD,cmpArtworkDate)
    expensive = copy.deepcopy(listD)
    mg.sort(expensive,cmpArtworkCost)

    stop = time.process_time_ns()

    sgs = (stop-start)/1000000000
    print(sgs) 

    return [listD ,Cost , Weight, expensive]

def ArtbyDepartment(catalog,depa):


    listA = catalog['Artworks']
    a=lt.newList("ARRAY_LIST")

    for artwork in listA['elements']:
        if artwork['Department'] == depa:

            lt.addLast(a,artwork)

    return a



# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def compareArtistIds(id1, id2):
   
    if int(id1 == id2):
        return 0
    elif int(id1 > id2):
        return 1
    else:
        return -1



def compareArtworksIds(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def compareBeginDate(date, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    datentry = me.getKey(entry)
    if (int(date) == int(datentry)):
        return 0
    elif (int(date) > int(datentry)):
        return 1
    else:
        return -1

def compareArtworksbymedium(Medium, artwork):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    artentry = me.getKey(artwork)
    if (Medium == artentry):
        return 0
    elif (Medium > artentry):
        return 1
    else:
        return -1

def compareArtworksbyDepartment(d1,d2):

    artentry = me.getKey(d2)
    if (d1 == artentry):
        return 0
    elif (d1 > artentry):
        return 1
    else:
        return -1


def compareAuthorsByName(keyname, author):
    """
    Compara dos nombres de autor. El primero es una cadena
    y el segundo un entry de un map
    """
    authentry = me.getKey(author)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1

def compareNationality(Nationality,entry):
    NationalityE = me.getKey(entry)
    if Nationality == NationalityE:
        return 0
    elif Nationality > NationalityE:
        return 1
    else:
        return -1


##################################################
##################################################


def cmpArtistBegindate(Date1, Date2):

    if Date1 < Date2:
        return True
    else:
        return False

def compareDateAcquired(d1,d2):
    

    if d1["DateAcquired"]<=d2["DateAcquired"]:
        return True
    else:
        return False

def cmpArtworkDate(artwork1, artwork2):

    if artwork1["Date"] == '':
        artwork1["Date"]='No se sabe'
    if artwork2["Date"] == '':
        artwork2["Date"]='No se sabe'

    if (artwork1["Date"]) < (artwork2["Date"]):
        return True
    else:
        return False

def cmpArtistNationality(artist1, artist2):

    if artist1['ArtistBio'] < artist2['ArtistBio']:
        return True
    else:
        return False

def compareID(a,b):
    if a["ConstituentID"]<b["ConstituentID"]:
        return True
    else:
        return False

def cmpNationality(n1,n2):
    if n1[1]>n2[1]:
        return True
    else: 
        return False

def compareDate(q,w):
    if q["Date"]>w["Date"]:
        return True
    else:
        return False

def cmpArtworkCost(artwork1, artwork2):
    if (artwork1["Cost"]) > (artwork2["Cost"]):
        return True
    else:
        return False