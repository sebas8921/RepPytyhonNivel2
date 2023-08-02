import api
import concurrent.futures
import os
from collections import Counter
import tabulate

#CARGA INICIAL DE DATOS

print('Extrayendo los datos del API, espere por favor.......')

infoPersonajes = api.getInfoPersonajes()                    #obtenemos informacion general de personajes
infoUbicaciones = api.getInfoUbicaciones()                  #obtenemos informacion general de personajes
infoEpisodios = api.getInfoEpisodios()                      #obtenemos informacion general de episodios

totalPersonajes = infoPersonajes['info']['count']           #obtenemos el total de personajes existentes
totalPaginasPersonajes = infoPersonajes['info']['pages']    #obtenemos el total de paginas de personajes

totalUbicaciones = infoUbicaciones['info']['count']         #obtenemos el total de ubicaciones existentes
totalPaginasUbicaciones = infoUbicaciones['info']['pages']  #obtenemos el total de paginas de ubicaciones

totalEpisodios = infoEpisodios['info']['count']             #obtenemos el total de episodios existentes
totalPaginasEpisodios = infoEpisodios['info']['pages']      #obtenemos el total de paginas de episodios}

todoslosPersonajes = []                                     #lista que almacenara todos los personajes
todoslosEpisodios = []                                      #lista que almacenara todos los episodios
todaslasUbicaciones = []                                    #lista que almacenara todos los episodios


#creamos una lista para iterar y obtener los personajes de todas las paginas
listaPaginasDePersonajes = []
for id in range(0,totalPaginasPersonajes):
     listaPaginasDePersonajes.append(id+1)


#funcion para obtener los personajes de una pagina especifica
def obtenerPersonajePorPagina(pagina):
    personajesPagina = api.getPersonajesPagina(pagina)
    for personaje in personajesPagina:
        todoslosPersonajes.append(personaje)

#obtenemos todos los personajes utilizando threading
def obtenerTodosLosPersonajes():
     with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        executor.map(obtenerPersonajePorPagina, listaPaginasDePersonajes)

#ejecutamos la obtencion de todos los personajes
obtenerTodosLosPersonajes()

#ordenamos la lista de personajes
todoslosPersonajes.sort(key=lambda llave: llave['id'])

#obtenemos todas la ubicaciones
for contadorPaginas in range (1,totalPaginasUbicaciones+1):
        ubicacionesPagina = api.getUbicacionesPagina(contadorPaginas)
        for ubicacion in ubicacionesPagina:
            todaslasUbicaciones.append(ubicacion) 
            
#obtenemos todos los episodios         
for contadorPaginas in range (1,totalPaginasEpisodios+1):
        episodiosPagina = api.getEpisodiosPagina(contadorPaginas)
        for episodio in episodiosPagina:
            todoslosEpisodios.append(episodio)


print('Extracción de datos del API se realizo de forma exitosa.......')
input('Presione ENTER para continuar...')

#metodo que imprime el mensaje de salida del programa
def salirDelPrograma():
    print('Gracias por utilizar el programa...Hasta pronto!!')

#metodo para imprimir la informacion general de la serie
def imprimirInfoGeneral():
    os.system('cls')
    print('Informacion general de la serie:')
    print('------------------------------------------------')
    print('El total de capitulos emitidos de la serie son: ' + str(totalEpisodios))
    print('El total de personajes contabilizados son: ' + str(totalPersonajes))
    print('El total de ubicaciones de la serie son: ' + str(totalUbicaciones))
    input('Presione ENTER para continuar...')

#metodo para imprimir que se ha elegido una opcion invalida dentro del menu
def opcionInvalida():
    print('ERROR: La opcion elegida no es valida')
    input('Presione ENTER para continuar...')
 
#metodo para imprimir la lista de todos los personajes   
def listarTodosLosPersonajes():
    for personaje in todoslosPersonajes:
            print('id:' +'  ' + str(personaje['id']) + '    ' + 'nombre:' + '   ' + str(personaje['name']) + '    ' + 'especie:' + '   ' + str(personaje['species'])  + '    ' + 'estatus:' + '   ' + str(personaje['status']))
    input('Presione ENTER para continuar...')

#metodo para imprimir la lista de todas las ubicaciones 
def listarTodasLasUbicaciones():
    for ubicacion in todaslasUbicaciones:
            print('id:' +'  ' + str(ubicacion['id']) + '    ' + 'nombre:' + '   ' + str(ubicacion['name']) + '    ' + 'tipo:' + '   ' + str(ubicacion['type']))
    input('Presione ENTER para continuar...')

#metodo para imprimir la lista de todos los episodios
def listarTodosLosEpisodios():
    for episodio in todoslosEpisodios:
            print('id:' +'  ' + str(episodio['id']) + '    ' + 'nombre:' + '   ' + str(episodio['name']) + '    ' + 'fecha de emisión:' + '   ' + str(episodio['air_date']))
    input('Presione ENTER para continuar...')   

#metodo para contabilizar los personajes por status
def personajesPorStatus():
    listaStatus = []
    for personaje in todoslosPersonajes:
        listaStatus.append(personaje['status'])
    dictConteoStatus = Counter(listaStatus)
    datos = dictConteoStatus.items()
    print('estatus  |   cantidad')
    print('---------------------')
    for key,value in datos:
         print(key,'    |',value)
    input('Presione ENTER para continuar...') 

def ubicacionesPorTipo():
    listaTipo = []
    for ubicacion in todaslasUbicaciones:
        listaTipo.append(ubicacion['type'])
    dictConteoTipo = Counter(listaTipo)
    datos = dictConteoTipo.items()
    print('tipo_ubicacion  |   cantidad')
    print('---------------------')
    for key,value in datos:
         print(key,'    |',value)
    input('Presione ENTER para continuar...') 


#MENU PRINCIPAL DEL PROGRAMA
opcionMenu = 0
while opcionMenu != 7:
    os.system('cls')
    print('------------------------------------------------')
    print('API - RICK AND MORTY')
    print('MENU PRINCIPAL')
    print('------------------------------------------------')
    print('1.Informacion general de la serie')
    print('2.Mostrar información general de todos los personajes')
    print('3.Mostrar informacion general de todas las ubicaciones')
    print('4.Mostrar informacion general de todos los episodios')
    print('5.Contabilizar los personajes por su estatus')
    print('6.Contabilizar los ubicaciones por tipo')
    print('7.Salir del programa')
    print('------------------------------------------------')
    opcionMenu = int(input('Digite el numero de la opcion que desea realizar, seguidamente presione la tecla ENTER: '))
    match opcionMenu:
        case 1: 
            imprimirInfoGeneral()
        case 2:
            listarTodosLosPersonajes()
        case 3:
            listarTodasLasUbicaciones()
        case 4:
            listarTodosLosEpisodios()
        case 5:
            personajesPorStatus()
        case 6:
            ubicacionesPorTipo()
        case 7:
            salirDelPrograma()
        case _: 
            opcionInvalida()


#pendientes
#cantidad de ubicaciones por tipo
#cantidad de episodios por año y mes