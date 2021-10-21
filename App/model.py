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
import time
import config as cf
import copy
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
import time 
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as mg
from DISClib.Algorithms.Sorting import insertionsort as ins
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

    
    #REQ1
    catalog['BeginDate'] = mp.newMap(500,
                                   maptype='CHAINING',
                                   loadfactor=5,
                                   comparefunction=compareBeginDate)
    
    
    #REQ3
    catalog['DisplayName'] = mp.newMap(14500,
                                maptype='CHAINING',
                                loadfactor=2,
                                comparefunction=compareArtworksbymedium)
    #REQ3
    catalog['Work_artists'] = mp.newMap(16000,
                                 maptype='PROBING',
                                 loadfactor=0.5,)
    #REQ3
    catalog['Artists_ConstituentID'] = mp.newMap(16000,
                                 maptype='PROBING',
                                 loadfactor=0.5,)
    '''
    catalog['Work_ConstituentID'] = mp.newMap(16000,
                                 maptype='PROBING',
                                loadfactor=0.5,)

    
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

    '''
    catalog['Department'] = mp.newMap(34500,
                                maptype='CHAINING',
                                loadfactor=2,
                                comparefunction=compareArtworksbyDepartment)  
    
    catalog['Medium'] = mp.newMap(34500,
                                maptype='CHAINING',
                                loadfactor=2,
                                comparefunction=compareArtworksbymedium)
    
    
                                 
    

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
    
 ######

def addArtist(catalog, artist):
    lt.addLast(catalog["Artists"], artist)

    addtomap(catalog['BeginDate'],artist['BeginDate'],artist)
    mp.put(catalog['Artists_ConstituentID'],artist['ConstituentID'],artist)
    mp.put(catalog['DisplayName'],artist['DisplayName'],artist)



    
def addArtwork(catalog, artwork):
    lt.addLast(catalog["Artworks"], artwork)

    addtomap(catalog['Medium'],artwork['Medium'],artwork)
    addtomap2(catalog["Department"],artwork["Department"],artwork)
    #mp.put(catalog['Work_ConstituentID'],artwork['ConstituentID'],artwork)
    ArtworksbyArtist(catalog,artwork)


def addDateAcquired(catalog,artwork):
    addtomap(catalog["DateAcquired",artwork["DateAcquired"],artwork])


    #addtomap(catalog['Medium'],artwork['Medium'],artwork)
    #mp.put(catalog['Work_ConstituentID'],artwork['ConstituentID'],artwork)
    #ArtworksbyNationalityMap(catalog,artwork)
    ArtworksbyArtist(catalog,artwork)

# Funciones para creacion de datos
#REQ3
def ArtworksbyArtist(catalog,artwork):

    list=artwork['ConstituentID'].replace('[','').replace(']','').split(',')
    Artists=[]
    for i in list:

        Artist=mp.get(catalog['Artists_ConstituentID'],i)
        if Artist != None:
            Name=mp.get(catalog['Artists_ConstituentID'],i)['value']['DisplayName']
            if Name not in Artists:
                Artists.append(Name)

                addtomap(catalog['Work_artists'],i,artwork)



'''
def ArtworksbyNationalityMap(catalog,artwork):


    
        Artist=mp.get(catalog['Artists_ConstituentID'],i)
        if Artist != None:
            Nation=mp.get(catalog['Artists_ConstituentID'],i)['value']['Nationality']
            if Nation not in Nations:
                Nations.append(Nation)
                addtomap(catalog['Work_Nationality'],Nation,artwork)
'''  

   





# Funciones para creacion de datos



# Funciones de consulta

####### REQ 1 #######

def ArtistbyBeginDate(catalog, min, max):

    start = time.process_time_ns()

    rta=[]

    Dates=mp.keySet(catalog['BeginDate'])
    b=lt.newList(datastructure='ARRAY_LIST')

    for i in range(1,lt.size(Dates)+1):

        date=int(lt.getElement(Dates,i))

        if int(min) <= date and date <= int(max):
            lt.addLast(b,date)

    mg.sort(b,cmpArtistBegindate)
    
  
    size=0
    for i in range(1,lt.size(b)+1):

        if type(mp.get(catalog['BeginDate'],str(lt.getElement(b,i)))['value']) == type(lt.getElement(catalog['Artists'],1)):
            size+=1

        else:
            size+=lt.size(mp.get(catalog['BeginDate'],str(lt.getElement(b,i)))['value'])




    rta.append(size)

#######

    pos=1
    x=True
    
    while pos <=3 and x :

        if type(mp.get(catalog['BeginDate'],str(lt.getElement(b,pos)))['value']) == type(lt.getElement(catalog['Artists'],1)):
            listvalues=mp.get(catalog['BeginDate'],str(lt.getElement(b,pos)))['value']
            rta.append(listvalues)
            pos+=1

        if type(mp.get(catalog['BeginDate'],str(lt.getElement(b,pos)))['value']) != type(lt.getElement(catalog['Artists'],1)):
            listvalues=mp.get(catalog['BeginDate'],str(lt.getElement(b,pos)))['value']
            mg.sort(listvalues,cmpArtistConstituentID)

            if lt.size(listvalues) >= 3:

                if len(rta)==1:
                    for i in range(1,4):
                        rta.append(lt.getElement(listvalues,i))
                elif len(rta)==2:
                    for i in range(1,3):
                        rta.append(lt.getElement(listvalues,i))
                elif len(rta)==3:
                    rta.append(lt.getElement(listvalues,1))
                x=False
                
            elif lt.size(listvalues) == 2:
                
                if len(rta)==1:
                    for i in range(1,3):
                        rta.append(lt.getElement(listvalues,i))
                    pos+=1   
                elif len(rta)==2:
                    for i in range(1,3):
                        rta.append(lt.getElement(listvalues,i))
                    x=False
                elif len(rta)==3:
                    rta.append(lt.getElement(listvalues,1))
                    x=False
              
    
    pos=lt.size(b)
    x=True
    l=lt.newList(datastructure='ARRAY_LIST')
    while pos >=lt.size(b)-2 and x :
        
        if type(mp.get(catalog['BeginDate'],str(lt.getElement(b,pos)))['value']) == type(lt.getElement(catalog['Artists'],1)):
            listvalues=mp.get(catalog['BeginDate'],str(lt.getElement(b,pos)))['value']
            lt.addLast(l,listvalues)
            pos-=1
        
        if type(mp.get(catalog['BeginDate'],str(lt.getElement(b,pos)))['value']) != type(lt.getElement(catalog['Artists'],1)):
            listvalues=mp.get(catalog['BeginDate'],str(lt.getElement(b,pos)))['value']
            mg.sort(listvalues,cmpArtistConstituentID)

            if lt.size(listvalues) >= 3:

                if lt.size(l)==0:
                    for i in range(1,4):
                        lt.addLast(l,lt.getElement(listvalues,i))
                elif lt.size(l)==1:
                    for i in range(1,3):
                        lt.addLast(l,lt.getElement(listvalues,i))
                elif lt.size(l)==2:
                    lt.addLast(l,lt.getElement(listvalues,1))
                x=False
                
            elif lt.size(listvalues) == 2:
                
                if lt.size(l)==0:
                    for i in range(1,3):
                        lt.addLast(l,lt.getElement(listvalues,i))
                elif lt.size(l)==1:
                    for i in range(1,3):
                        lt.addLast(l,lt.getElement(listvalues,i))
                    x=False
                elif lt.size(l)==2:
                    lt.addLast(l,lt.getElement(listvalues,1))
                    x=False
        pos-=1      

    mg.sort(l,cmpArtistBeginDateSublist)

    for i in l['elements']:
      
        rta.append(i)

      
    stop = time.process_time_ns()

    sgs = (stop-start)/1000000000
    print(sgs) 

    return rta



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

def ArtworksMediumsbyArtist(catalog,ArtistName):
    
    start = time.process_time_ns()

    key=mp.get(catalog['DisplayName'],ArtistName)['value']['ConstituentID']

    if mp.get(catalog['Work_artists'],key) != None:
        artworks=mp.get(catalog['Work_artists'],key)['value']

        
        if type(artworks) != type(lt.getElement(catalog['Artists'],1)):

            mg.sort(artworks,cmpArtworkMedium)

            size=lt.size(artworks)
            rta=[size]+ ArtwroksMedium(artworks)

            rta.append(mp.get(catalog['DisplayName'],ArtistName)['value'])
            #len de lista = 5

            stop = time.process_time_ns()

            sgs = (stop-start)/1000000000
            print(sgs)

            return rta

        else:
            rta=[1,[artworks['Medium']],artworks['Medium'],artworks,mp.get(catalog['DisplayName'],ArtistName)['value']]
            
            stop = time.process_time_ns()

            sgs = (stop-start)/1000000000
            print(sgs)

            return rta

            
            
    else: 

        stop = time.process_time_ns()

        sgs = (stop-start)/1000000000
        print(sgs)

        return 0

def ArtwroksMedium(list):
    

    Mediums=[lt.getElement(list,1)['Medium']]
    big_M =lt.getElement(list,1)['Medium']
    dic={}

    

    for artwork in list['elements']:
        if artwork['Medium'] not in Mediums:  
            Mediums.append(artwork['Medium'])

    biggest=0
    for medium in Mediums:
        count=0
        for art in list['elements']:
            if medium == art['Medium']:
                count+=1
        dic[medium]=count
        if biggest <= count:
            biggest = count
            big_M = medium

    
    return [dic, big_M , Artwork_big_M(list,big_M)]

def Artwork_big_M(list,big_M):

    a=lt.newList("ARRAY_LIST")

    for artwork in list['elements']:
        if artwork['Medium'] == big_M:

            lt.addLast(a,artwork)

    return a

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

#### BONO ####

def prolificArtist(catalog, min, max, n):

    start = time.process_time_ns()

    Dates=mp.keySet(catalog['BeginDate'])
    b=lt.newList(datastructure='ARRAY_LIST')

    for i in range(1,lt.size(Dates)+1):

        date=int(lt.getElement(Dates,i))

        if int(min) <= date and date <= int(max):
            lt.addLast(b,date)

    mg.sort(b,cmpArtistBegindate)

    listArtist=lt.newList(datastructure='ARRAY_LIST')

    x=True
    pos=1

    while pos <=n and x :

        if type(mp.get(catalog['BeginDate'],str(lt.getElement(b,pos)))['value']) == type(lt.getElement(catalog['Artists'],1)):
            artist=mp.get(catalog['BeginDate'],str(lt.getElement(b,pos)))['value']
            
            result=ArtworksMediumsbyArtist(catalog,artist['DisplayName'])
            if result != 0:
                lt.addLast(listArtist,[mp.get(catalog['BeginDate'],str(lt.getElement(b,pos)))['value'],result])
            else:
                lt.addLast(listArtist,[mp.get(catalog['BeginDate'],str(lt.getElement(b,pos)))['value'],[0,[],'','',a]])
            
            

        if type(mp.get(catalog['BeginDate'],str(lt.getElement(b,pos)))['value']) != type(lt.getElement(catalog['Artists'],1)):
            listvalues=mp.get(catalog['BeginDate'],str(lt.getElement(b,pos)))['value']
            
            for a in listvalues['elements']:
                
                resul=ArtworksMediumsbyArtist(catalog,a['DisplayName'])
                if resul != 0:
                    lt.addLast(listArtist,[a,resul])
                else:
                    lt.addLast(listArtist,[a,[0,[],'','',a]])

        pos+=1
    
    ins.sort(listArtist,cmpProlificArtists)

    

    artists=[]
    for i in range(1,n+1):
        artists.append(lt.getElement(listArtist,i))

   
    stop = time.process_time_ns()

    sgs = (stop-start)/1000000000
    print(sgs) 
   
    return artists









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

def cmpArtistConstituentID(artist1, artist2):

    if int(artist1['ConstituentID']) < int(artist2['ConstituentID']):
        return False
    else:
        return True

def cmpArtistBeginDateSublist(artist1, artist2):

    if int(artist1['BeginDate']) < int(artist2['BeginDate']):
        return True
    else:
        return False

def cmpArtworkMedium(artwork1, artwork2):
    if (artwork1["Medium"]) < (artwork2["Medium"]):
        return True
    else:
        return False

def cmpProlificArtists(artist1,artist2):

    a1=artist1[1]
    a2=artist2[1]
    

    if a1[0] > a2[0]:
        return True

    #elif len(artist1[1]) > len(artist2[1]):
     #   return True

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
