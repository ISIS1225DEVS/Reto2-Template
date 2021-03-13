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
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import selectionsort as ss
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import mergesort as mg
from DISClib.Algorithms.Sorting import quicksort as qs

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos Array
def newCatalog_Array():
    catalog = {'videos': None,
               'country': None,
               'tagvideos': None,
               'categories': None}
    catalog['videos'] = lt.newList()
    catalog['country'] = lt.newList("ARRAY_LIST",
                                    cmpfunction=cmpcountry)
    catalog['tagvideos'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=cmptags)
    catalog['categories'] = lt.newList('ARRAY_LIST',
                                    cmpfunction=cmpcategories)

    return catalog
#Construcción modelo linked
def newCatalog_Linked():
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para los canales,
    una lista vacia para la fecha de tendencia, el país, las visitas, los likes, 
    los dislikes y adicionalmente el id de la categoría.
    . Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'country': None,
               'tagvideos': None,
               'categories': None}
    catalog['videos'] = lt.newList()
    catalog['country'] = lt.newList("SINGLE_LINKED",
                                    cmpfunction=cmpcountry)
    catalog['tagvideos'] = lt.newList("SINGLE_LINKED",
                                    cmpfunction=cmptags)
    catalog['categories'] = lt.newList("SINGLE_LINKED",
                                    cmpfunction=cmpcategories)
    return catalog


# Funciones para agregar informacion al catalogo
def addVideo(catalog, video):
    # Se adiciona el video a la lista de videos
    lt.addLast(catalog['videos'], video)
    #Se adicionan los tags en la lista de tagvideos
    tagvideo_info = video['tags'].split("|")
    for tag_info in tagvideo_info:
        addTagsVideo(catalog, tag_info, video)
    #Adiciona los países en su respectiva llave
    country = video['country']
    addCountry(catalog, country, video)
    

def addCountry(catalog, n_country, video):
    countries = catalog['country']
    print(countries)
    pos_country = lt.isPresent(countries, n_country)
    if pos_country > 0:
        lt.addLast(countries['videos'], video)
    else: 
        country = newCountry(n_country)
        lt.addLast(countries, video['country'])
    lt.addLast(country['videos'], video)


def addTagsVideo(catalog, n_tag, video):
    tagvideos = catalog['tagvideos']
    pos_tag = lt.isPresent(tagvideos, n_tag)
    if pos_tag > 0:
        videotag = lt.getElement(tagvideos, pos_tag)
    else:
        videotag = newVideoTag(n_tag)
        lt.addLast(tagvideos, videotag)
    lt.addLast(videotag['videos'], video)


def addCategories(catalog, categories_videos):
    category = NewCategories(categories_videos['name'], categories_videos['id'])
    lt.addLast(catalog['categories'], category)


# Funciones para creacion de datos
# Estas funciones son precisamente para hacer la creación 
# De las llaves y sus respectivos valores (llaves vacías, la idea es crear la llave y en las funciones
# de agregar información al catálogo se completan)


def newCountry(n_country):
    country = {'name': "", 'videos': None}
    country['name'] = n_country
    country['videos'] = lt.newList('ARRAY_LIST')
    return country

def newVideoTag(tag_name):
    video_tag = {'name': "", 'videos': None}
    video_tag['name'] = tag_name
    video_tag['videos'] = lt.newList('ARRAY_LIST')
    return video_tag

def NewCategories(name, id):
    categories_videos = {'name': "", 'id': ""}
    categories_videos['name'] = name
    categories_videos['id'] = id
    return categories_videos

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpcountry(country1, country2):
    if (country1.lower() in country2.lower()):
        return 0
    return -1

def cmptags(tag1,tag2):
    if (tag1.lower() in tag2['name'].lower()):
        return 0
    return -1

def cmpcategories(n_category, categories_videos):
    return (n_category == categories_videos['name'])

def cmpVideosByViews(video1, video2):
    if video1['views'] < video2['views']:
        return True
    return False

# Funciones de ordenamiento

def sortVideos(catalog, size, sortType):
    sub_list = lt.subList(catalog['videos'], 0, size)
    start_time = time.process_time()
    if sortType == 1:
        sorted_list = ss.sort(sub_list, cmpVideosByViews)
    elif sortType == 2:
        sorted_list = ins.sort(sub_list, cmpVideosByViews)
    elif sortType == 3:
        sorted_list = sa.sort(sub_list, cmpVideosByViews)
    elif sortType == 4:
        sorted_list = mg.sort(sub_list, cmpVideosByViews)
    else:
        sorted_list = qs.sort(sub_list, cmpVideosByViews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list


def greatestTendency(catalog, n_category):
    temp_list = []
    video_template = {'title': "", 
                      'channel_title': "", 
                      'category_id': "", 
                      'days_trending': []
                      'ammount_of_days': 0}
    for video in catalog['categories']:
        for video_temp in temp_list:
            if video['title'] == video_temp['title']:
                trending_date = video['publish_time'][0:9]
                if trending_date not in video_temp['days_trending']:
                    video_temp['days_trending'].append(trending_date)
                    video_temp['ammount_of_days'] += 1
            else:
                video_template['title'] = video['title']
                video_template['channel_title'] = video['channel_title']
                video_template['category_id'] = video['category_id']
                video_template['days_trending'].append(video['publish_time'][0:9])
                video_template['ammount_of_days'] = 1
    best = None
    days = 0
    for video in temp_list:
        if video['ammount_of_days'] > days:
            days = video['ammount_of_days']
            best = video
    return best