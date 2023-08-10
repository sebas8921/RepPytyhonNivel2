import api
import concurrent.futures
import os
from collections import Counter
import pandas as pd
import matplotlib.pyplot as plt
import datetime

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
        personaje.pop('origin')
        personaje.pop('location')
        personaje.pop('episode')
        personaje.pop('image')
        personaje.pop('url')
        fecha = datetime.datetime.fromisoformat(personaje['created'])
        año = fecha.year
        mes = fecha.month
        dia = fecha.day
        personaje['year'] = año
        personaje['month'] = mes
        personaje['day'] = dia
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
            ubicacion.pop('residents')
            fecha = datetime.datetime.fromisoformat(ubicacion['created'])
            año = fecha.year
            mes = fecha.month
            dia = fecha.day
            ubicacion['year'] = año
            ubicacion['month'] = mes
            ubicacion['day'] = dia
            todaslasUbicaciones.append(ubicacion) 
            
#obtenemos todos los episodios         
for contadorPaginas in range (1,totalPaginasEpisodios+1):
        episodiosPagina = api.getEpisodiosPagina(contadorPaginas)
        for episodio in episodiosPagina:
            episodio.pop('characters')
            episodio.pop('url')
            fecha = datetime.datetime.fromisoformat(episodio['created'])
            año = fecha.year
            mes = fecha.month
            dia = fecha.day
            episodio['year'] = año
            episodio['month'] = mes
            episodio['day'] = dia
            todoslosEpisodios.append(episodio)
            
df_Personajes = pd.DataFrame(todoslosPersonajes)
df_Personajes['Qty'] = 1
df_Ubicaciones = pd.DataFrame(todaslasUbicaciones)
df_Ubicaciones['Qty'] = 1
df_Episodios = pd.DataFrame(todoslosEpisodios)
df_Episodios['Qty'] = 1

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
    os.system('cls')
    print(df_Personajes.to_string(index=False))
    input('Presione ENTER para continuar...')

#metodo para imprimir la lista de todas las ubicaciones 
def listarTodasLasUbicaciones():
    os.system('cls')
    print(df_Ubicaciones.to_string(index=False))
    input('Presione ENTER para continuar...')

#metodo para imprimir la lista de todos los episodios
def listarTodosLosEpisodios():
    os.system('cls')
    print(df_Episodios.to_string(index=False))
    input('Presione ENTER para continuar...')   

#metodo para obtener una agrupacion de los personajes por status
def personajesPorStatus():
    os.system('cls')
    #se agrupan los datos de personajes por status
    df_PersonajesStatus = df_Personajes.groupby(['status'])['Qty'].sum()
    df_PersonajesStatus.sort_values()    
    plt.bar(df_PersonajesStatus.index, df_PersonajesStatus.values)
    plt.xlabel("status")
    plt.ylabel("cantidad de personajes")
    plt.title("Cantidad de personajes por status")
    plt.show()
    input('Presione ENTER para continuar...') 

#metodo para obtener una agrupacion de las ubicaciones por tipo
def ubicacionesPorDimension():
    os.system('cls')
    #se agrupan los datos de ubicaciones por status
    df_UbicacionesDimension = df_Ubicaciones.groupby(['dimension'])['Qty'].sum()
    plt.bar(df_UbicacionesDimension.index, df_UbicacionesDimension.values)
    plt.xlabel("Dimensiones")
    plt.ylabel("cantidad ubicaciones")
    plt.title("Ubicaciones por dimension")
    plt.show()
    input('Presione ENTER para continuar...')    

#metodo para describir las 3 tablas:
def desribirMuestras():
    os.system('cls')
    print('-------------------------------------------------')
    print('Descripcion de la tabla PERSONAJES')
    print('-------------------------------------------------')
    print(df_Personajes.describe)
    print('-------------------------------------------------')
    print('Descripcion de la tabla UBICACIONES')
    print('-------------------------------------------------')
    print(df_Ubicaciones.describe)
    print('-------------------------------------------------')
    print('Descripcion de la tabla EPISODIOS')
    print('-------------------------------------------------')
    print(df_Episodios.describe)
    input('Presione ENTER para continuar...') 

#metodo para imprimir la cantidad de personajes creados por año:
def personajesCreadosPorAño():
    df_PjsPorAño = df_Personajes.groupby(['year'])['Qty'].sum()
    print(df_PjsPorAño)
    plt.plot(df_PjsPorAño.index,df_PjsPorAño.values)
    plt.xlabel("Años")
    plt.ylabel("Personajes Creados")
    plt.title("Personajes creados por año")
    plt.show()

#metodo que imprime un grafico de pastel para mostrar los personajes por especie
def PersonajesPorEspecie():
    df_PjsPorEspecie = df_Personajes.groupby(['species'])['Qty'].sum()
    plt.pie(df_PjsPorEspecie.values,labels=df_PjsPorEspecie.index, autopct='%1.1f%%')
    plt.title("Distribucion de personajes por especie")
    plt.show()

#MENU PRINCIPAL DEL PROGRAMA
opcionMenu = 0

while opcionMenu != 10:
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
    print('7.Describir los datos de las 3 tablas')
    print('8.Contabilizar los personajes creados por año')
    print('9.Distribucion de personajes por Especie')
    print('10.Salir del programa')
    print('------------------------------------------------')
    try:
        opcionMenu = int(input('Digite el numero de la opcion que desea realizar, seguidamente presione la tecla ENTER: '))
    except:
        print('')
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
            ubicacionesPorDimension()
        case 7:
            desribirMuestras()
        case 8:
            personajesCreadosPorAño()
        case 9:
            PersonajesPorEspecie()
        case 10:
            salirDelPrograma()
        case _: 
            opcionInvalida()
