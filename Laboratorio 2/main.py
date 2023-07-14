import api
import ids
import time
import multiprocessing
import asyncio
import threading
import concurrent.futures

#---------------------------------------------------------------threads--------------------------------------------------

def ImpresionUsariosThread():
    with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
        executor.map(ImprimeUsuario, ids.ids)

#---------------------------------------------------------------asyncio--------------------------------------------------

#impresion de usuario unico como corrutina
async def ImprimeUsuarioAsyncio(idUsuario):
    dictUsuario = {idUsuario:api.getOneUser(idUsuario)}
    print(dictUsuario)

#funcion para ejecutar mediante syncio
async def ImprimeListaAsyncio(ListaUsuarios):
        tareas = []
        for contador in ListaUsuarios:
            tarea = asyncio.ensure_future(ImprimeUsuarioAsyncio(contador))
            tareas.append(tarea)
        await asyncio.gather(*tareas, return_exceptions=True)

#----------------------------------------------------------multiprocess--------------------------------------------------

#funcion para imprimir un unico usuario
def ImprimeUsuario(idUsuario):
    dictUsuario = {idUsuario:api.getOneUser(idUsuario)}
    print(dictUsuario)

#funcion para ejecutar mediante multiprocess
def ImprimeListaMultiprocess():
    with multiprocessing.Pool() as pool:
        pool.map(ImprimeUsuario, ids.ids)

#---------------------------------------------------forma tradicional(Sincronica)----------------------------------------

#funcion para impresion de la lista de forma sincrocnica
def ImprimeListaSincronica():
    for contador in range(0,len(ids.ids)):        
        dictUsuario = {ids.ids[contador]:api.getOneUser(ids.ids[contador])}
        print(dictUsuario)


#---------------------------------------------------Codigo principal de ejecuccion----------------------------------------
if __name__ == "__main__":

    tiempoInicio = time.time()

    ImpresionUsariosThread()

    #asyncio.get_event_loop().run_until_complete(ImprimeListaAsyncio(ids.ids))
    
    #ImprimeListaMultiprocess()
    
    #ImprimeListaSincronica()
    
    tiempoFinal = time.time() -tiempoInicio
    print(f'Tiempo de ejecucción: {tiempoFinal} segundos')





