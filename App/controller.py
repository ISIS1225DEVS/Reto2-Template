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
 """

from DISClib.ADT import list as lt
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
def initCatalog(estructuraDatos):
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog(estructuraDatos)
    return catalog


# Funciones para la carga de datos


def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArt(catalog)
    loadArtist(catalog)
   


def loadArt(catalog):
   
    artworksfile = cf.data_dir +  'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile , encoding='utf-8'))
    for artwork in input_file:
        model.addArt(catalog, artwork)


def loadArtist(catalog):
 
    artistsfile = cf.data_dir + 'Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    contador= 0
    for artist in input_file:
        """
        if contador>=50:
            break
        else: 
            model.addArtist(catalog, artist)
            contador+=1
        """
        model.addArtist(catalog, artist)
        contador+=1

def conteo_artistas(artistas, inicial, final):
    return model.get_conteo(artistas, inicial, final)

def primeros_tres(artistas, inicial, final):
    return model.get_primeros(artistas, inicial, final)

def ultimos_tres(artistas, inicial, final):
    return model.get_ultimos(artistas, inicial, final)

def get_obras(catalog, nombre_artista):
    return model.get_obrasxtecnica(catalog, nombre_artista)

def get_info_transporte(arte, nombre_departamento):
    return model.get_transporte(arte, nombre_departamento)

#Requerimiento 2
def Req2(catalog, fechai, fechaf):
    Lista = lt.newList()
    Compras = 0
    for keys in catalog['Art']:   
         listaArte = catalog['Art'][keys]
         if type(listaArte) == list:
            for Artworks in listaArte:
                NewLista = model.AddArtFecha(Artworks, fechai, fechaf, Lista)
                if model.escompra(Artworks):
                    Compras += 1
    size = (lt.size(NewLista))

    a = NewLista['first']['next']['next']['info']
    ainfo = (('Titulo: '+ str(a['Title'])), ('Medio: '+ str(a['Medium'])), (' Fecha: '+ str(a['Date'])), ('Dimensiones: '+ str(a['Dimensions'])))
    b = NewLista['first']['next']['info']
    binfo = (('Titulo: '+ str(b['Title'])), ('Medio: '+ str(b['Medium'])), (' Fecha: '+ str(b['Date'])), ('Dimensiones: '+ str(b['Dimensions'])))
    c = NewLista['first']['info']
    cinfo = (('Titulo: '+ str(c['Title'])), ('Medio: '+ str(c['Medium'])), (' Fecha: '+ str(c['Date'])), ('Dimensiones: '+ str(c['Dimensions'])))
    primeras3 = (ainfo, binfo, cinfo)

    d = NewLista['last']['info']
    ultima = ((('Titulo: '+ str(d['Title'])), ('Medio: '+ str(d['Medium'])), (' Fecha: '+ str(d['Date'])), ('Dimensiones: '+ str(d['Dimensions']))))

    return ((model.OrganizarFecha(NewLista)), (size), Compras, primeras3, ultima )



def Req4(catalog):
    nacionalidades = model.verID(catalog)
    list = model.OrganizarNacionalidad(nacionalidades)
    return list