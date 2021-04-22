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
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import orderedmapstructure as oms
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    catalog = {'ListeningEvents': None,
                'Artists': None,
                'Audio_Songs': None}
    catalog['ListeningEvents'] = lt.newList('SINGLE_LINKED', compareEvents)
    catalog['Artist'] = om.newMap(omaptype='RBT',comparefunction=compareArtists)
    catalog['Audio_Songs'] = om.newMap(omaptype='RBT',comparefunction=compareSongs)

    return catalog    
# Funciones para agregar informacion al catalogo 
def addDateIndex(datentry, event):
    """Revisa si hay una fecha en el catalogo que contenga 
    dicha información, si es así, agrega la información en el valor
    de la llave, y si no es así simplemente adiciona el valor como
    uno nuevo."""
    lst = datentry['lstevents']
    lt.addLast(lst, event)
    EventIndex = datentry['EventIndex']
    eventry = m.get(EventIndex, event['hashtag'])
    if (eventry is None):
        
    
# Funciones para creacion de datos
def newDataEvent(event):
    entry_event = {'created_date': None, 'list_hashtags': None}
    entry_event['created_date'] = m.newMap(numelements=30,
                                            maptype='PROBING',
                                            comparefunction=compareEvents)
    entry_event['list_hashtags'] = lt.newList('SINGLELINKED', compareTags)

    return entry_event

def newHashtag(hashtag, event):
    """
    Crea una entrada en el indice por hashtag, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    hashtag_entry = {''}
#Funciones de comparación
def compareEvents(event_1, event_2):
    """
    Compara dos eventos
    """
    if (event_1 == event_2):
        return 0
    elif event_1 > event_2:
        return 1
    else:
        return -1

def compareArtists(artist_1, artist_2):
    """
    Compara dos artistas
    """
    if (artist_1 == artist_2):
        return 0
    elif artist_1 > artist_2:
        return 1
    else:
        return -1

def compareTrack(song_1, song_2):
    """
    Compara dos pistas
    """
    if (song_1 == song_2):
        return 0
    elif song_1 > song_2:
        return 1
    else:
        return -1

def compareTags(Tag_1, Tag_2):
    """
    Compara dos hashtags
    """
    Tag_1.upper()
    Tag_2.upper()
    if (Tag_1 == Tag_2):
        return 0
    elif Tag_1 > Tag_2:
        return 1
    else:
        return -1
# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
