import requests as req

#metodo para obtener la primera pagina de lista de personajes
#imprime ademas el conteo de personajes totales y en cuantas paginas estan distribuidos
def getInfoPersonajes():
    url = "https://rickandmortyapi.com/api/character"
    getResponse = req.get(url)
    if getResponse.status_code == 200:
        return getResponse.json()
    else:
        print("ERROR: No fue posible datos en el metodo getInfoPersonajes")
        
#metodo para obtener la primera pagina de lista de ubicaciones en la serie
#imprime ademas el conteo de ubicaciones totales y en cuantas paginas estan distribuidos
def getInfoUbicaciones():
    url = "https://rickandmortyapi.com/api/location"
    getResponse = req.get(url)
    if getResponse.status_code == 200:
        return getResponse.json()
    else:
        print("ERROR: No fue posible datos en el metodo getInfoUbicaciones")
        
#metodo para obtener la primera pagina de lista de episodios en la serie
#imprime ademas el conteo de episodios totales y en cuantas paginas estan distribuidos        
def getInfoEpisodios():
    url = "https://rickandmortyapi.com/api/episode"
    getResponse = req.get(url)
    if getResponse.status_code == 200:
        return getResponse.json()
    else:
        print("ERROR: No fue posible datos en el metodo getInfoUbicaciones")

# metodo para obtener los personajes de una pagina especifica
# al ser un metodo pesado, utilizaremos asyncio para ejecutar la tarea de forma simultanea sobre las diferentes paginas
def getPersonajesPagina(pagina):
    url = "https://rickandmortyapi.com/api/character/?page=" + str(pagina)
    getResponse = req.get(url)
    if getResponse.status_code == 200:
        return getResponse.json()['results']
    else:
        print("ERROR: No fue posible datos en el metodo getInfoPersonajes")

#metodo para obtener las ubicaciones de una pagina especifica       
def getUbicacionesPagina(pagina):
    url = "https://rickandmortyapi.com/api/location?page=" + str(pagina)
    getResponse = req.get(url)
    if getResponse.status_code == 200:
        return getResponse.json()['results']
    else:
        print("ERROR: No fue posible datos en el metodo getInfoPersonajes")

#metodo para obtener los episodios de una pagina especifica        
def getEpisodiosPagina(pagina):
    url = "https://rickandmortyapi.com/api/episode?page=" + str(pagina)
    getResponse = req.get(url)
    if getResponse.status_code == 200:
        return getResponse.json()['results']
    else:
        print("ERROR: No fue posible datos en el metodo getInfoPersonajes")