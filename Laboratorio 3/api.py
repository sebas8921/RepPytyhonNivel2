import requests as req
import json

def getBromaAleatoria():
    url = "https://api.chucknorris.io/jokes/random"
    getResponse = req.get(url)
    if getResponse.status_code == 200:
        datos = getResponse.json()
        return datos["value"]
    else:
        print("ERROR: No fue posible obtener una broma aleatoria")


def getCategorias():
    url = "https://api.chucknorris.io/jokes/categories"
    getResponse = req.get(url)
    if getResponse.status_code == 200:
        return getResponse.json()
    else:
        print("ERROR: No fue posible obtener la lista de categorias")


def getCategoriaEspecifica(categoria):
    url = "https://api.chucknorris.io/jokes/random?category=" + str(categoria)
    getResponse = req.get(url)
    if getResponse.status_code == 200:
        datos = getResponse.json()
        return datos["value"]
    else:
        print("ERROR: No fue posible obtener una broma con la categoria ingresada")